//i2c

#include <Wire.h>

void setup()
{
  Wire.begin(); // join i2c bus (address optional for master)
  Wire.setClock(100000);
}

byte x = 0;

void loop()
{

    Wire.requestFrom(4, 4, true);   // Ask device #4 the 
    while (Wire.available())
    {
       char inChr = Wire.read();
    }
    delayMicroseconds(500);
}
