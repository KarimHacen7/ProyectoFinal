//i2c

#include <Wire.h>

void setup()
{
  Wire.begin(); // join i2c bus (address optional for master)
  Wire.setClock(40000);
}

byte x = 0;

void loop()
{

    if (x%2 == 0)
    {
      //Wire.beginTransmission(4); // transmit to device #4       
      //Wire.write(x);             // sends one byte
      //Wire.endTransmission();    // stop transmitting
    }
    else
    {
      Wire.requestFrom(4, 4, true);   // Ask device #4 the 
      while (Wire.available())
      {
         char inChr = Wire.read();
      }
    }
    x++;
    delayMicroseconds(500);
}
