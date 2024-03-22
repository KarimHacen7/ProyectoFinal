#include <stdio.h>
#include <stdlib.h>
#include "pico/stdlib.h"
#include "configuration.h"
#include "communication.h"
#include "sampling.h"
#include "hardware/structs/bus_ctrl.h"
#include "hardware/clocks.h"
#include "untriggered_digital.pio.h"
#include "hardware/pio.h"
#include "hardware/dma.h"
#include "hardware/adc.h"

#define BASE_ADC_GPIO_NUMEBER 26
#define ADC_CHANNEL_NUMBER 2

const uint32_t samplingFrequenciesLUT[] = {1000,2500,5000,10000,25000,50000,100000,250000,500000,1000000,2500000,5000000,10000000,25000000,50000000,100000000,125000000};
volatile alarm_id_t triggerTimeoutAlarm;

// Claim State Machine, DMA Channel and configure
void setPIOSamplingHardware(DataTransferHardware* dth)
{
    dth->PIOPeripheral = pio0;
    dth->stateMachineInstance = pio_claim_unused_sm(dth->PIOPeripheral, true);
    dth->transferDMAChannel = dma_claim_unused_channel(true);
    bus_ctrl_hw->priority = BUSCTRL_BUS_PRIORITY_DMA_W_BITS | BUSCTRL_BUS_PRIORITY_DMA_R_BITS;
    dth->transferDMAChannelConfig = dma_channel_get_default_config(dth->transferDMAChannel);
    channel_config_set_transfer_data_size(&dth->transferDMAChannelConfig, DMA_SIZE_8);
    channel_config_set_read_increment(&dth->transferDMAChannelConfig, false);
    channel_config_set_write_increment(&dth->transferDMAChannelConfig, true);
    channel_config_set_dreq(&dth->transferDMAChannelConfig, pio_get_dreq(dth->PIOPeripheral, dth->stateMachineInstance, false));
}

// Set system clock, return SM, DMA Channel and clear PIO program memory
void resetPIOSamplingHardware(DataTransferHardware* dth, SamplingSettings* samplingSettings)
{
    set_sys_clock_khz(125000, true);
    dma_channel_unclaim(dth->transferDMAChannel);
    pio_clear_instruction_memory(dth->PIOPeripheral);
    pio_sm_unclaim(dth->PIOPeripheral, dth->stateMachineInstance);
    samplingSettings->order = None;
}

void setSlowADCSamplingHardware(DataTransferHardware* dth, SamplingSettings* samplingSettings)
{
    adc_gpio_init(BASE_ADC_GPIO_NUMEBER + ADC_CHANNEL_NUMBER);
    adc_init();
    adc_select_input(ADC_CHANNEL_NUMBER);
    adc_fifo_setup(true, true, 1, false, true);
    
    dth->transferDMAChannel = dma_claim_unused_channel(true);
    dth->transferDMAChannelConfig = dma_channel_get_default_config(dth->transferDMAChannel);

    channel_config_set_transfer_data_size(&dth->transferDMAChannelConfig, DMA_SIZE_8);
    channel_config_set_read_increment(&dth->transferDMAChannelConfig, false);
    channel_config_set_write_increment(&dth->transferDMAChannelConfig, true);

    channel_config_set_dreq(&dth->transferDMAChannelConfig, DREQ_ADC);

    if (samplingSettings->frequency == 8)
    {
        adc_set_clkdiv(0);
    }
    else
    {
        adc_set_clkdiv((48000000/(samplingFrequenciesLUT[samplingSettings->frequency]))-1);
    }
}

void resetSlowADCSamplingHardware(DataTransferHardware* dth, SamplingSettings* samplingSettings)
{
    adc_set_clkdiv(0);
    adc_run(false);
    adc_fifo_drain();
    set_sys_clock_khz(125000, true);
    dma_channel_unclaim(dth->transferDMAChannel);
    samplingSettings->order = None;
}

// Used when trigger event does not occur
int64_t triggeredTimeoutAlarmCallback(alarm_id_t id, void *userData)
{
    DataTransferHardware* tempPtr = userData;
    gpio_set_irq_enabled(7, GPIO_IRQ_EDGE_RISE|GPIO_IRQ_EDGE_FALL|GPIO_IRQ_LEVEL_HIGH|GPIO_IRQ_LEVEL_LOW, false);
    dma_channel_abort(tempPtr->transferDMAChannel);
    pio_sm_set_enabled(tempPtr->PIOPeripheral, tempPtr->stateMachineInstance, false);
    tempPtr->abortedTransfer = true;
    cancel_alarm(id);
    return 0;
}

// Start On-Board ADC on trigger event
void slowADCTriggerCallback()
{
    cancel_alarm(triggerTimeoutAlarm); 
    adc_run(true);
    gpio_set_irq_enabled(7, GPIO_IRQ_EDGE_RISE|GPIO_IRQ_EDGE_FALL|GPIO_IRQ_LEVEL_HIGH|GPIO_IRQ_LEVEL_LOW, false);
}

// Stop timeout alarm when data transfer trigger event ocurrs
void stopTriggerTimeoutAlarm()
{
    cancel_alarm(triggerTimeoutAlarm);
    irq_clear(PIO0_IRQ_0);
    hw_set_bits(&pio0->irq, 1u);
}