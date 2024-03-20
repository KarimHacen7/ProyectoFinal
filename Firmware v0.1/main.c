#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "pico/stdlib.h"
#include "configuration.h"
#include "communication.h"
#include "sampling.h"

#include "hardware/structs/bus_ctrl.h"
#include "hardware/clocks.h"
#include "untriggered_digital.pio.h"
#include "triggered_digital.pio.h"

#define LED_PIN 25

#define PIO_IN_BASE_OPCODE 0x4000
#define PIO_WAIT_0_BASE_OPCODE 0x2000
#define PIO_WAIT_1_BASE_OPCODE 0x2080

const uint32_t samplingFrequenciesLUT[] = {1000,2500,5000,10000,25000,50000,100000,250000,500000,1000000,2500000,5000000,10000000,25000000,50000000,100000000,125000000};

volatile alarm_id_t triggerTimeoutAlarm;

int64_t triggered_timeout_alarm_callback(alarm_id_t id, void *userData)
{
    DataTransferHardware* tempPtr = userData; 
    dma_channel_abort(tempPtr->transferDMAChannel);
    pio_sm_set_enabled(tempPtr->PIOPeripheral, tempPtr->stateMachineInstance, false);
    tempPtr->abortedTransfer = true;
    return 0;
}

void stopTriggerTimeoutAlarm()
{
    cancel_alarm(triggerTimeoutAlarm);
    irq_clear(PIO0_IRQ_0);
    hw_set_bits(&pio0->irq, 1u);
}

int main(void)
{
    gpio_init(LED_PIN);
    gpio_set_dir(LED_PIN, GPIO_OUT);

    uint32_t i = 0;
    USBInput usbInput = { .position = 0, .lastInput = 0, .keepReading = true};
    SamplingSettings samplingSettings = {.mode = Digital, .triggerMode=0, .frequency = 0, .depth = 1, .compareVoltage = 1.65, .sample = false, .timeout=1,.configVoltage  =false };
    DataTransferHardware dth = {.transferDMAChannel = 0, .abortedTransfer = false, .stateMachineInstance = 0, .PIOPeripheral = pio0, .programOffset = 0, .frequencyDivider = 1 };
    uint8_t samplingBuffer[SAMPLING_BUFFER_SIZE] = {'$'};
    strcpy(usbInput.buffer, USB_INPUT_BUFFER_DEFAULT);
    
    stdio_init_all();
    irq_set_exclusive_handler(PIO0_IRQ_0, stopTriggerTimeoutAlarm);
    irq_set_enabled(PIO0_IRQ_0, true);
    pio0_hw->inte0 = PIO_IRQ0_INTE_SM0_BITS;

    initialiseDAC();

    while (true) 
    {
        getInputString(&usbInput);
        
        if(strcmp(usbInput.buffer, USB_INPUT_BUFFER_DEFAULT) != 0)
        {
            getSettingsFromInput(&usbInput, &samplingSettings);

            sleep_ms(100);
            printf("Modo: %d\n", samplingSettings.mode);
            printf("Trigger Mode: %d\n", samplingSettings.triggerMode);
            printf("Canales: %d\n", samplingSettings.channels);
            printf("Trigger Channel %d\n", samplingSettings.triggerChannel);
            printf("Frecuencia: %d\n", samplingSettings.frequency);
            printf("Profundidad: %d\n", samplingSettings.depth);
            printf("Timeout: %f\n", samplingSettings.timeout);
            printf("Voltaje Comp: %.3f\n", samplingSettings.compareVoltage);
            printf("Muestrear?: %d\n", samplingSettings.sample);
        }
        printf(usbInput.buffer);
        printf("\n");
        
        if(samplingSettings.configVoltage)
        {
            writeDACVoltage(samplingSettings.compareVoltage);
            
            samplingSettings.configVoltage = false;
        }


        if(samplingSettings.sample)
        {
            gpio_put(25,1);
            
            setBasicSamplingHardware(&dth);

            if((samplingSettings.mode == Digital) && (samplingSettings.triggerMode == Untriggered))
            {
                dth.programOffset = pio_add_program(dth.PIOPeripheral, &untriggered_digital_program);
                dth.PIOPeripheral->instr_mem[dth.programOffset] = PIO_IN_BASE_OPCODE + samplingSettings.channels;
                if(samplingSettings.frequency == 12 || samplingSettings.frequency == 13 || samplingSettings.frequency == 15)
                {
                    set_sys_clock_khz(100000, true);
                }
                dth.frequencyDivider = (float)clock_get_hz(clk_sys) / (samplingFrequenciesLUT[samplingSettings.frequency]);
                dma_channel_configure(dth.transferDMAChannel, &dth.transferDMAChannelConfig, &samplingBuffer, &dth.PIOPeripheral->rxf[dth.stateMachineInstance], (samplingSettings.depth)*1024, true);
                untriggered_digital_program_init(dth.PIOPeripheral, dth.stateMachineInstance, dth.programOffset, 0, dth.frequencyDivider);
                dma_channel_wait_for_finish_blocking(dth.transferDMAChannel);
            }

            else if((samplingSettings.mode == Digital) && ((samplingSettings.triggerMode >= 1) && (samplingSettings.triggerMode <= 4)))
            {
                
                dth.programOffset = pio_add_program(dth.PIOPeripheral, &triggered_digital_program);
                
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
                triggerTimeoutAlarm = add_alarm_in_ms((samplingSettings.timeout)*1000, triggered_timeout_alarm_callback, (&dth), true);
                dma_channel_configure(dth.transferDMAChannel, &dth.transferDMAChannelConfig, &samplingBuffer, &dth.PIOPeripheral->rxf[dth.stateMachineInstance], (samplingSettings.depth)*1024, true);
                triggered_digital_program_init(dth.PIOPeripheral, dth.stateMachineInstance, dth.programOffset, 0, dth.frequencyDivider);
                dma_channel_wait_for_finish_blocking(dth.transferDMAChannel);
                cancel_alarm(triggerTimeoutAlarm);
            }
            resetBasicSamplingHardware(&dth, &samplingSettings);

            if(dth.abortedTransfer)
            {
                printf(CMD_TRIGGER_TIMEOUT);
                dth.abortedTransfer = false;
            }
            else
            {
                for(i = 0; i < (samplingSettings.depth)*1024; i++)
                {
                    printf("%d\n", samplingBuffer[i]);
                }   
            }
            
            sleep_ms(100);
        }

        strcpy(usbInput.buffer, USB_INPUT_BUFFER_DEFAULT);
        gpio_put(LED_PIN, 0);
        sleep_ms(1000);
    }
}




