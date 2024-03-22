#include <stdio.h>
#include <stdlib.h>
#include "pico/stdlib.h"
#include "configuration.h"
#include "hardware/structs/bus_ctrl.h"
#include "hardware/pio.h"
#include "hardware/dma.h"
#include "untriggered_digital.pio.h"

#ifndef SAMPLING_H
#define SAMPLING_H

#define SAMPLING_BUFFER_SIZE (1024*192) // array size, equivalent to 3 internal SRAM banks

typedef struct
{
    volatile int transferDMAChannel;
    volatile bool abortedTransfer;
    volatile PIO PIOPeripheral;
    uint stateMachineInstance;
    uint programOffset;
    dma_channel_config transferDMAChannelConfig;
    float frequencyDivider;
}DataTransferHardware;

void setPIOSamplingHardware(DataTransferHardware* dth);
void resetPIOSamplingHardware(DataTransferHardware* dth, SamplingSettings* samplingSettings);
void setSlowADCSamplingHardware(DataTransferHardware* dth, SamplingSettings* samplingSettings);
void resetSlowADCSamplingHardware(DataTransferHardware* dth, SamplingSettings* samplingSettings);

int64_t triggeredTimeoutAlarmCallback(alarm_id_t id, void *userData);
void slowADCTriggerCallback();
void stopTriggerTimeoutAlarm();


#endif