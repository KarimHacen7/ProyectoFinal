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

#define PIO_IN_BASE_OPCODE 0x4000

//extern uint8_t samplingBuffer[SAMPLING_BUFFER_SIZE] = {'$'};

void setBasicSamplingHardware(DataTransferHardware* dth)
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

void resetBasicSamplingHardware(DataTransferHardware* dth, SamplingSettings* samplingSettings)
{
    set_sys_clock_khz(125000, true);
    dma_channel_unclaim(dth->transferDMAChannel);
    pio_sm_unclaim(dth->PIOPeripheral, dth->stateMachineInstance);
    samplingSettings->sample = false;
}


void configureVoltageReference(SamplingSettings* samplingSettings);
