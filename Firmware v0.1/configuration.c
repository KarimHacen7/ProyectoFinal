#include <stdio.h>
#include <stdlib.h>
#include "pico/stdlib.h"

#include "configuration.h"
#include "communication.h"

/*
This function verifies the syntax of a command recieved through usb. 
If verification is passed, it will load settings in the appropiate structure.
Ii verification is not passed, it will disregard the command and send a BAD COMMAND message.
*/
void getSettingsFromInput(USBInput* usbInput, SamplingSettings* samplingSettings)
{
    bool badCommand = false;
    uint8_t id = 0;
    SamplingSettings temp = (*samplingSettings);
    if((usbInput->buffer[1] == 'D' || usbInput->buffer[1] == 'A' ) && usbInput->buffer[10] == ';')
    {
        for(int i = 2; i <= 9; i++)
        {
            if(usbInput->buffer[i] < '0' || usbInput->buffer[i] > '9')
            {
                badCommand = true;   id=1;
                break;                  //exit the for loop 
            }   
        }
    }
    else if (usbInput->buffer[1] == 'C')
    {
        if(usbInput->buffer[2] == 'V' && usbInput->buffer[6] == ';')
        {
            for(int i = 3; i <= 5; i++)
            {
                if(usbInput->buffer[i] < '0' || usbInput->buffer[i] > '9')
                {
                    badCommand = true;   id=2;
                    break;                  //exit the for loop 
                }   
            }
        }
        else if(usbInput->buffer[2] == 'T'  && usbInput->buffer[7] == ';')
        {
            for(int i = 3; i <= 6; i++)
            {
                if(usbInput->buffer[i] < '0' || usbInput->buffer[i] > '9')
                {
                    badCommand = true;   id=3;
                    break;                  //exit the for loop 
                }   
            }
        }
        else
        {
            badCommand = true; id=4;
        }
    }
    else
    {
        badCommand = true; id=5;
    }
    if(badCommand)
    {
        printf(CMD_BAD_COMMAND);
        printf("%d", id);
        return;
    }

    switch(usbInput->buffer[1])
    {
        /*  #ABCDEFGHI;
            A: D, Muestreo Digital
            B: 0-4, Modo de Gatillado, 0 para no gatillado
            C: Canal de gatillado 1-8
            D: 8, 4, 2, 1, Canales 
            EF: 00-16, Frecuencia de Muestreo, ver tabla de verdad
            GHI: 000-192, Profundidad de Muestreo, en KiB*/
        case 'D':
            temp.mode = Digital;
            
            if(usbInput->buffer[2] < '0' || usbInput->buffer[2] > '4')
            {
                badCommand = true; id=6;
                break;
            }
            else
            {
                temp.triggerMode = (usbInput->buffer[2]-'0');
            }

            if(usbInput->buffer[3] < '1' || usbInput->buffer[3] > '8')
            {
                badCommand = true; id=7;
                break;
            }
            else
            {
                temp.triggerChannel = (usbInput->buffer[3]-'0');
            }
            
            if(usbInput->buffer[4] == '1' || usbInput->buffer[4] == '2' || usbInput->buffer[4] == '4' || usbInput->buffer[4] == '8')
            {
                temp.channels = (usbInput->buffer[4]-'0');
            }
            else
            {
                badCommand = true; id=8;
                break;
            }          

            if(temp.triggerChannel > temp.channels)
            {
                badCommand = true; id=9;
                break;
            }

            temp.frequency = (10*(usbInput->buffer[5]-'0'))+(usbInput->buffer[6]-'0');
            if(temp.frequency > 16)
            {
                badCommand = true; id=10;
                break;
            }

            temp.depth = (100*(usbInput->buffer[7]-'0'))+(10*(usbInput->buffer[8]-'0'))+(usbInput->buffer[9]-'0');
            if(temp.depth > 192)
            {
                badCommand = true; id=11;
                break;
            }
        break;
        case 'A':
            temp.mode = Analog;

            if(usbInput->buffer[2] < '0' || usbInput->buffer[2] > '4')
            {
                badCommand = true; id=12;
                break;
            }
            else
            {
                temp.triggerMode = (usbInput->buffer[2]-'0');
            }
            
            if(usbInput->buffer[3] != '8' )
            {
                badCommand = true; id=13;
                break;
            }
            else
            {
                temp.triggerChannel = (usbInput->buffer[3]-'0');
            }
            
            if(usbInput->buffer[4] == '1')
            {
                temp.channels = 1;
            }
            else
            {
                badCommand = true; id=14;
                break;
            }
            
            temp.frequency = (10*(usbInput->buffer[5]-'0'))+(usbInput->buffer[6]-'0');
            if(temp.frequency > 13)
            {
                badCommand = true;id=15;
                break;
            }

            temp.depth = (100*(usbInput->buffer[7]-'0'))+(10*(usbInput->buffer[8]-'0'))+(usbInput->buffer[9]-'0');
            if(temp.depth > 192)
            {
                badCommand = true; id=16;
                break;
            }

            break;  
        case 'C':
            
            if(usbInput->buffer[2] == 'V')
            {
                temp.compareVoltage = (1*(usbInput->buffer[3]-'0'))+((0.1)*(usbInput->buffer[4]-'0'))+((0.01)*(usbInput->buffer[5]-'0'));
                temp.order = Voltage;
                if(temp.compareVoltage < 0 || temp.compareVoltage > 3.3)
                {
                    badCommand = true;id=17;
                    break;
                }
            }
            else if (usbInput->buffer[2] == 'T')
            {
                temp.timeout = (10*(usbInput->buffer[3]-'0'))+(1*(usbInput->buffer[4]-'0'))+(0.1*(usbInput->buffer[5]-'0'))+(0.01*(usbInput->buffer[6]-'0'));
                temp.order = Timeout;
                if(temp.timeout < 0 || temp.timeout > 100)
                {
                    badCommand = true;id=18;
                    break;
                }
            }
            break;
        default:
            printf(CMD_BAD_COMMAND);
            break;  
    }
    if(badCommand)
    {
        printf(CMD_BAD_COMMAND);
        printf("%d", id);
        return;
    }
    if(temp.order == Timeout)
    {
        temp.order = None;
        (*samplingSettings) = temp;
    }
    else if(temp.order == Voltage )
    {
        (*samplingSettings) = temp;
    }
    else
    {
        temp.order = Sample;
        (*samplingSettings) = temp;
    }
        
}