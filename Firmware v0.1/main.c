#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "pico/stdlib.h"
// Required to use RP2040's various hardware modules
#include "hardware/structs/bus_ctrl.h"
#include "hardware/structs/vreg_and_chip_reset.h"
#include "hardware/clocks.h"
#include "hardware/adc.h"
#include "hardware/gpio.h"
// PIO Helper functions
#include "untriggered_digital.pio.h"
#include "triggered_digital.pio.h"
#include "untriggered_analog.pio.h"
#include "triggered_analog.pio.h"
// Files with other functionality
#include "configuration.h"
#include "communication.h"
#include "sampling.h"

#define LED_PIN 25

#define PIO_IN_BASE_OPCODE 0x4000
#define PIO_WAIT_0_BASE_OPCODE 0x2000
#define PIO_WAIT_1_BASE_OPCODE 0x2080

extern const uint32_t samplingFrequenciesLUT[];
extern volatile alarm_id_t triggerTimeoutAlarm;

int main(void)
{
    // usbInput, samplingSettings and dth are structures that represent hardware and variables use for different purposes in the program
    // Check their definitions for more information about them, in their respective header files
    // samplingBuffer is where the samples will be stored after capture
    uint32_t i = 0;
    uint32_t TEMPSKERE = 0;
    USBInput usbInput = { .position = 0, .lastInput = 0, .keepReading = true};
    strcpy(usbInput.buffer, USB_INPUT_BUFFER_DEFAULT);
    SamplingSettings samplingSettings = {.mode = Digital, .triggerMode=0, .frequency = 0, .depth = 1, .compareVoltage = 1.65, .timeout=1,.order = None };
    DataTransferHardware dth = {.transferDMAChannel = 0, .abortedTransfer = false, .stateMachineInstance = 0, .PIOPeripheral = pio0, .programOffset = 0, .frequencyDivider = 1 };
    uint8_t samplingBuffer[SAMPLING_BUFFER_SIZE] = {'$'};
    // Begin USB comms
    stdio_init_all();
    // Check if reset cause was reset button (used for halting sampling)
    if(vreg_and_chip_reset_hw->chip_reset & (1 << 16))
    {
        printf(CMD_HARD_RESET);
    }
    // LED Indicator
    gpio_init(LED_PIN);
    gpio_set_dir(LED_PIN, GPIO_OUT);
    // Required for Trigger timeouts
    irq_set_exclusive_handler(PIO0_IRQ_0, stopTriggerTimeoutAlarm);
    irq_set_enabled(PIO0_IRQ_0, true);
    pio0_hw->inte0 = PIO_IRQ0_INTE_SM0_BITS;
    // Set compare voltage to 1.65[V]
    initialiseDAC();
    while (true) 
    {
        getInputString(&usbInput);
        // If we got a command, set the syntax and configurate accordingly
        if(strcmp(usbInput.buffer, USB_INPUT_BUFFER_DEFAULT) != 0)
        {
            getSettingsFromInput(&usbInput, &samplingSettings);
            sleep_ms(100);
        }
        // Decision Making
        if(samplingSettings.order == None)
        {
            continue;
        }
        // Change the Compare Voltage
        else if(samplingSettings.order == Voltage)
        {
            writeDACVoltage(samplingSettings.compareVoltage);
            samplingSettings.order = None;
        }
        // Sample
        else if(samplingSettings.order == Sample)
        {
            // Check if sampling is made through On-Board ADC or PIO
            if(samplingSettings.mode == Analog && samplingSettings.frequency <=8)
            {
                // Configure hardware, ADC + DMA to move the data to memory
                setSlowADCSamplingHardware(&dth, &samplingSettings);
                dma_channel_configure(dth.transferDMAChannel, &dth.transferDMAChannelConfig,samplingBuffer,&adc_hw->fifo,(samplingSettings.depth)*1024,true);
                if(samplingSettings.triggerMode == Untriggered)
                {   
                    // Sample immediately
                    adc_run(true);
                    dma_channel_wait_for_finish_blocking(dth.transferDMAChannel);
                }
                else
                {
                    // Or set an IRQ and its callback to trigger begin ADC Sampling
                    switch (samplingSettings.triggerMode)
                    {
                        case 1:
                            gpio_set_irq_enabled_with_callback(7, GPIO_IRQ_EDGE_RISE, true, &slowADCTriggerCallback);
                            break;
                        case 2:
                            gpio_set_irq_enabled_with_callback(7, GPIO_IRQ_EDGE_FALL, true, &slowADCTriggerCallback);
                            break;
                        case 3:
                            gpio_set_irq_enabled_with_callback(7, GPIO_IRQ_LEVEL_LOW, true, &slowADCTriggerCallback);
                            break;
                        case 4:
                            gpio_set_irq_enabled_with_callback(7, GPIO_IRQ_LEVEL_HIGH, true, &slowADCTriggerCallback);
                            break;
                        default:
                            break;
                    }
                    triggerTimeoutAlarm = add_alarm_in_ms((samplingSettings.timeout)*1000, triggeredTimeoutAlarmCallback, (&dth), true);
                    dma_channel_wait_for_finish_blocking(dth.transferDMAChannel);
                    cancel_alarm(triggerTimeoutAlarm);
                }
                resetSlowADCSamplingHardware(&dth, &samplingSettings);
            }
            else
            {
                setPIOSamplingHardware(&dth);
                if((samplingSettings.mode == Digital) && (samplingSettings.triggerMode == Untriggered))
                {
                    // Load PIO Assembly
                    dth.programOffset = pio_add_program(dth.PIOPeripheral, &untriggered_digital_program);
                    // Change Machine Code value on program memory to change how many channels are sampled
                    dth.PIOPeripheral->instr_mem[dth.programOffset] = PIO_IN_BASE_OPCODE + samplingSettings.channels;
                    // If required, perform a system underclock to avoid using jittery decimal frequency divider
                    if(samplingSettings.frequency == 12 || samplingSettings.frequency == 13 || samplingSettings.frequency == 15)
                    {
                        set_sys_clock_khz(100000, true);
                    }
                    dth.frequencyDivider = (float)clock_get_hz(clk_sys) / (samplingFrequenciesLUT[samplingSettings.frequency]);
                    // Setup DMA Channel and begin clocked (using DREQ) data transfer
                    dma_channel_configure(dth.transferDMAChannel, &dth.transferDMAChannelConfig, &samplingBuffer, &dth.PIOPeripheral->rxf[dth.stateMachineInstance], (samplingSettings.depth)*1024, true);
                    // Begin Sampling
                    untriggered_digital_program_init(dth.PIOPeripheral, dth.stateMachineInstance, dth.programOffset, 0, dth.frequencyDivider);
                    // Acts as: while (transferIsFinished) {nop();}
                    dma_channel_wait_for_finish_blocking(dth.transferDMAChannel);
                }
                else if((samplingSettings.mode == Digital) && ((samplingSettings.triggerMode >= 1) && (samplingSettings.triggerMode <= 4)))
                {
                    dth.programOffset = pio_add_program(dth.PIOPeripheral, &triggered_digital_program);
                    // Change Machine Code value on program memory to change trigger event
                    switch (samplingSettings.triggerMode)
                    {
                        case 1:
                            dth.PIOPeripheral->instr_mem[dth.programOffset] = (PIO_WAIT_0_BASE_OPCODE+(samplingSettings.triggerChannel-1));
                            dth.PIOPeripheral->instr_mem[dth.programOffset+1] = (PIO_WAIT_1_BASE_OPCODE+(samplingSettings.triggerChannel-1));
                            break;
                        case 2:
                            dth.PIOPeripheral->instr_mem[dth.programOffset] = (PIO_WAIT_1_BASE_OPCODE+(samplingSettings.triggerChannel-1));
                            dth.PIOPeripheral->instr_mem[dth.programOffset+1] = (PIO_WAIT_0_BASE_OPCODE+(samplingSettings.triggerChannel-1));
                            break;
                        case 3:
                            dth.PIOPeripheral->instr_mem[dth.programOffset] = (PIO_WAIT_0_BASE_OPCODE+(samplingSettings.triggerChannel-1));
                            dth.PIOPeripheral->instr_mem[dth.programOffset+1] = (PIO_WAIT_0_BASE_OPCODE+(samplingSettings.triggerChannel-1));
                            break;
                        case 4:
                            dth.PIOPeripheral->instr_mem[dth.programOffset] = (PIO_WAIT_1_BASE_OPCODE+(samplingSettings.triggerChannel-1));
                            dth.PIOPeripheral->instr_mem[dth.programOffset+1] = (PIO_WAIT_1_BASE_OPCODE+(samplingSettings.triggerChannel-1));
                            break;
                        default:
                            break;
                    }
                    if(samplingSettings.frequency == 12 || samplingSettings.frequency == 13 || samplingSettings.frequency == 15)
                    {
                        set_sys_clock_khz(100000, true);
                    }
                    dth.frequencyDivider = (float)clock_get_hz(clk_sys) / (samplingFrequenciesLUT[samplingSettings.frequency]);
                    // Add timeout alarm
                    triggerTimeoutAlarm = add_alarm_in_ms((samplingSettings.timeout)*1000, triggeredTimeoutAlarmCallback, (&dth), true);
                    dma_channel_configure(dth.transferDMAChannel, &dth.transferDMAChannelConfig, &samplingBuffer, &dth.PIOPeripheral->rxf[dth.stateMachineInstance], (samplingSettings.depth)*1024, true);
                    triggered_digital_program_init(dth.PIOPeripheral, dth.stateMachineInstance, dth.programOffset, 0, dth.frequencyDivider);
                    dma_channel_wait_for_finish_blocking(dth.transferDMAChannel);
                    // And stop if sample is completed
                    cancel_alarm(triggerTimeoutAlarm);
                }
                else if ((samplingSettings.mode == Analog) && (samplingSettings.triggerMode == Untriggered))
                {
                    dth.programOffset = pio_add_program(dth.PIOPeripheral, &untriggered_analog_program);
                    if(samplingSettings.frequency == 12)
                    {
                        set_sys_clock_khz(100000, true);
                    }
                    dth.frequencyDivider = (float)clock_get_hz(clk_sys) / (2*(samplingFrequenciesLUT[samplingSettings.frequency]));
                    dma_channel_configure(dth.transferDMAChannel, &dth.transferDMAChannelConfig, &samplingBuffer, &dth.PIOPeripheral->rxf[dth.stateMachineInstance], (samplingSettings.depth)*1024, true);
                    untriggered_analog_program_init(dth.PIOPeripheral, dth.stateMachineInstance, dth.programOffset, 8, 16, dth.frequencyDivider);
                    dma_channel_wait_for_finish_blocking(dth.transferDMAChannel);
                }
                else 
                {
                    dth.programOffset = pio_add_program(dth.PIOPeripheral, &triggered_analog_program);
                    gpio_put(25,1);
                    switch (samplingSettings.triggerMode)
                    {
                        case 1:
                            dth.PIOPeripheral->instr_mem[dth.programOffset] = (PIO_WAIT_0_BASE_OPCODE+(samplingSettings.triggerChannel-1));
                            dth.PIOPeripheral->instr_mem[dth.programOffset+1] = (PIO_WAIT_1_BASE_OPCODE+(samplingSettings.triggerChannel-1));
                            break;
                        case 2:
                            dth.PIOPeripheral->instr_mem[dth.programOffset] = (PIO_WAIT_1_BASE_OPCODE+(samplingSettings.triggerChannel-1));
                            dth.PIOPeripheral->instr_mem[dth.programOffset+1] = (PIO_WAIT_0_BASE_OPCODE+(samplingSettings.triggerChannel-1));
                            break;
                        case 3:
                            dth.PIOPeripheral->instr_mem[dth.programOffset] = (PIO_WAIT_0_BASE_OPCODE+(samplingSettings.triggerChannel-1));
                            dth.PIOPeripheral->instr_mem[dth.programOffset+1] = (PIO_WAIT_0_BASE_OPCODE+(samplingSettings.triggerChannel-1));
                            break;
                        case 4:
                            dth.PIOPeripheral->instr_mem[dth.programOffset] = (PIO_WAIT_1_BASE_OPCODE+(samplingSettings.triggerChannel-1));
                            dth.PIOPeripheral->instr_mem[dth.programOffset+1] = (PIO_WAIT_1_BASE_OPCODE+(samplingSettings.triggerChannel-1));
                            break;
                        default:
                            break;
                    }
                    if(samplingSettings.frequency == 12)
                    {
                        set_sys_clock_khz(100000, true);
                    }
                    dth.frequencyDivider = (float)clock_get_hz(clk_sys) / (2*(samplingFrequenciesLUT[samplingSettings.frequency]));
                    triggerTimeoutAlarm = add_alarm_in_ms((samplingSettings.timeout)*1000, triggeredTimeoutAlarmCallback, (&dth), true);
                    dma_channel_configure(dth.transferDMAChannel, &dth.transferDMAChannelConfig, &samplingBuffer, &dth.PIOPeripheral->rxf[dth.stateMachineInstance], (samplingSettings.depth)*1024, true);
                    triggered_analog_program_init(dth.PIOPeripheral, dth.stateMachineInstance, dth.programOffset, 8, 16, dth.frequencyDivider);
                    dma_channel_wait_for_finish_blocking(dth.transferDMAChannel);
                    cancel_alarm(triggerTimeoutAlarm);
                }
                resetPIOSamplingHardware(&dth, &samplingSettings);
            }
            if(dth.abortedTransfer)
            {
                printf(CMD_TRIGGER_TIMEOUT);
                dth.abortedTransfer = false;
            }
            else
            {   // Print results
                //printf(CMD_BEGIN);
                for(i = 0; i < (samplingSettings.depth)*1024; i++)
                {
                    printf("%c", *(samplingBuffer+i));
                }
                printf(CMD_END);
                stdio_flush();   
            }
            sleep_ms(100);
        }
        strcpy(usbInput.buffer, USB_INPUT_BUFFER_DEFAULT);
        gpio_put(LED_PIN, 0);
        cancel_alarm(triggerTimeoutAlarm); // Just in case
        sleep_ms(100);
    }
}
