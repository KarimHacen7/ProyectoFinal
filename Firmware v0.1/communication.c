#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "pico/stdlib.h"
#include "hardware/spi.h"

#include "configuration.h"
#include "communication.h"

#define USB_INPUT_BUFFER_SIZE 12
#define USB_INPUT_BUFFER_DEFAULT "-----------"

#define DAC_SPI_RX_PIN 16
#define DAC_SPI_CS_PIN 17
#define DAC_SPI_SCK_PIN 18
#define DAC_SPI_TX_PIN 19

volatile bool inputTimedOut = false;

int64_t input_timeout_alarm_callback(alarm_id_t id, void *userData)
{
    inputTimedOut = true;
    return 0;
}

/*
This function recieves a USBInput pointer, pointing to the struct that represents
the commands from the GUI. Length, beginning and ending characters are verified
    If the buffer has a random character different from '#' (which indicates the start of a command), it will empty the buffer
    If the buffer is empty, it will return
    If the buffer is overflown with a command, it will disregard the command and transmit a NACK
    If the command takes more than 2 seconds to present a ';' (which indicates the end of a command), it will disregard the command and transmit TIMEDOUT
*/
void getInputString(USBInput* usbInput)
{
    alarm_id_t timeoutAlarm;
    usbInput->lastInput = getchar_timeout_us(50);
    if(usbInput->lastInput == '#')
    {   // store it and begin looping, expecting more chars as a command
        usbInput->buffer[0] = '#';
        usbInput->keepReading = true;
        inputTimedOut = false;
        // set alarm
        timeoutAlarm = add_alarm_in_ms(2000, input_timeout_alarm_callback, (&usbInput), true);
        if(timeoutAlarm == -1)
        {
            printf(CMD_ERROR);
            printf("Unable to get an alarm for input timeout clock");
        }
        while(usbInput->keepReading && !inputTimedOut)
        {   
            usbInput->lastInput = getchar_timeout_us(50);
            if(usbInput->lastInput != 255) // if we got something, store and continue looping 
            {
                usbInput->position++;
                if(usbInput->position > (USB_INPUT_BUFFER_SIZE-1)) // if the message is bigger than the buffer, exit
                {
                    cancel_alarm(timeoutAlarm); // stop alarm
                    usbInput->keepReading = false; 
                    usbInput->position = 0;
                    strcpy(usbInput->buffer, USB_INPUT_BUFFER_DEFAULT);
                    printf(CMD_OVERFLOW);
                    while(usbInput->lastInput != 255)
                    {
                        usbInput->lastInput = getchar_timeout_us(50); // empty buffer
                        
                    }
                    return;
                } 
                else
                {
                    usbInput->buffer[usbInput->position] = usbInput->lastInput; // unless its a semicolon, then stop looping and start decoding
                    if(usbInput->lastInput == ';')
                    {
                        cancel_alarm(timeoutAlarm); // stop alarm
                        usbInput->keepReading = false; 
                        usbInput->position = 0;
                        printf(CMD_ACKNOWLEDGE);
                        return;
                    }
                }
            }
        }
        if(inputTimedOut)
        {
            usbInput->keepReading = false; 
            usbInput->position = 0;
            strcpy(usbInput->buffer, USB_INPUT_BUFFER_DEFAULT);
            printf(CMD_TIMEOUT);
        }
        
    }
    else if(usbInput->lastInput == 255) // ignore
    {
        usbInput->keepReading = false; 
        usbInput->position = 0;
        strcpy(usbInput->buffer, USB_INPUT_BUFFER_DEFAULT);
        return;
    }
    else
    {
        while(usbInput->lastInput != 255)
        {
            usbInput->lastInput = getchar_timeout_us(50); // empty buffer
            
        }
        usbInput->keepReading = false; 
        usbInput->position = 0;
        strcpy(usbInput->buffer, USB_INPUT_BUFFER_DEFAULT);
        printf(CMD_ERROR);
    }

}


static inline void CSSelect() {
    asm volatile("nop \n nop \n nop");
    gpio_put(DAC_SPI_CS_PIN, 0);  // Active low
    asm volatile("nop \n nop \n nop");
}

static inline void CSDeselect() {
    asm volatile("nop \n nop \n nop");
    gpio_put(DAC_SPI_CS_PIN, 1);
    asm volatile("nop \n nop \n nop");
}


void writeDACVoltage(float value) {
    uint16_t calc = 0; // B15=B14=0
	uint8_t buffer[2];
	
	if (value < 0){value = 0;}
	if (value > 3.3){value = 3.3;}
	
	calc |= (1<<(12)); 	// SHDN=1
	
	if (value <= 2.048)
	{
		calc |= (1<<(13));	// GA=1
		calc = calc + (uint16_t) (value*(4096/2.048));
	}
	else
	{
		calc &= ~(1<<(13));	// GA=0
		calc = calc + (uint16_t) (value*(4096/(2.048*2)));
	}

	//printf("%d\n", calc);
	buffer[1] = (uint8_t)calc;
	buffer[0] = (uint8_t)(calc >> 8);
	
    CSSelect();
	
    spi_write_blocking(spi_default, buffer, 2);
	
    CSDeselect();
    sleep_ms(20);
	return;
}

void initialiseDAC()
{
    //Use SPI0 at 0.5MHz.
    spi_init(spi_default, 500 * 1000);
    
    gpio_set_function(DAC_SPI_SCK_PIN, GPIO_FUNC_SPI);
    gpio_set_function(DAC_SPI_TX_PIN, GPIO_FUNC_SPI);

    // Chip select is active-low, so we'll initialise it to a driven-high state
    gpio_init(DAC_SPI_CS_PIN);
    gpio_set_dir(DAC_SPI_CS_PIN, GPIO_OUT);
    gpio_put(DAC_SPI_CS_PIN, 1);

    writeDACVoltage(1.65);
}
