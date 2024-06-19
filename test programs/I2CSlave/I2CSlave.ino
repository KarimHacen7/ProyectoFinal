#include <Wire.h>

const char string[] = "Hola desde I2C!";
volatile uint8_t stringLen = 0;

volatile uint8_t charSelector = 0;

void setup()
{
  stringLen = sizeof(string)/sizeof(char);
  pinMode(OUTPUT, LED_BUILTIN);
  Wire.begin(4);                // join i2c bus with address #4
  Wire.onReceive(receiveEvent); // register event
  Wire.onRequest(requestEvent);  
}

void loop()
{
}

// function that executes whenever data is received from master
// this function is registered as an event, see setup()
void receiveEvent(int howMany)
{
  while(Wire.available()) // loop through all but the last
  {
    uint8_t c = Wire.read(); // receive byte as a char
  }
  digitalWrite(LED_BUILTIN, !digitalRead(LED_BUILTIN));
}

void requestEvent(int howMany)
{
  while (howMany > 0)
  {
    if (charSelector == stringLen-1)
    {
      charSelector = 0;
    }
    else
    {
      charSelector++;
    }
    Wire.write(string[charSelector]);
    howMany--;
  }
}
