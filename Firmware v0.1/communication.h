#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "pico/stdlib.h"

#ifndef COMMUNICATION_H
#define COMMUNICATION_H

#define CMD_ACKNOWLEDGE "#ACK;"
#define CMD_OVERFLOW "#OVERFLOW;"
#define CMD_TIMEOUT "#TIMEOUT;"
#define CMD_BEGIN "#BEGIN;"
#define CMD_END "#END;"
#define CMD_ERROR "#ERROR;"
#define CMD_BAD_COMMAND "#BADCOMMAND;"
#define CMD_TRIGGER_TIMEOUT "#TRIGTIMEOUT;"
#define CMD_HARD_RESET "#HARDRESET;"

#define USB_INPUT_BUFFER_SIZE 12
#define USB_INPUT_BUFFER_DEFAULT "-----------"

typedef struct {
    uint8_t buffer[USB_INPUT_BUFFER_SIZE];
    uint8_t position;
    uint8_t lastInput;
    bool keepReading;
}USBInput;

void getInputString(USBInput* usbInput);

void initialiseDAC();
void writeDACVoltage(float value);

#endif