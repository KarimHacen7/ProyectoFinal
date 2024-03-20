#include <stdio.h>
#include <stdlib.h>
#include "pico/stdlib.h"
#include "communication.h" 

#ifndef CONFIGURATION_H
#define CONFIGURATION_H

enum samplingModes {Digital=1, Analog=2};
enum triggerModes {Untriggered=0, Rising=1, Falling=2, LowLevel=3, HighLevel=4};

typedef struct
{
    enum samplingModes mode;
    enum triggerModes triggerMode;
    uint8_t channels;
    uint8_t triggerChannel;
    uint8_t frequency;
    uint8_t depth;
    float timeout;
    float compareVoltage;
    bool sample;
    bool configVoltage;
}SamplingSettings;

void getSettingsFromInput(USBInput* usbInput, SamplingSettings* samplingSettings);
void configureVoltageReference(SamplingSettings* samplingSettings);
void configureTriggerTimeout(SamplingSettings* samplingSettings);

#endif