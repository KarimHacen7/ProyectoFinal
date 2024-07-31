#include <SPI.h>

void setup(void)
{
  digitalWrite(SS, HIGH);  


  SPI.begin();
  
  SPI.beginTransaction(SPISettings(4000000, MSBFIRST, SPI_MODE0));
  // Ajusta la velocidad de comunicaciones a 1000KHz
  SPI.setClockDivider(SPI_CLOCK_DIV16);
}


void loop(void)
{
  char enviarByte;

  digitalWrite(SS, LOW);

  for (const char *msg = "Hello from SPI!" ; enviarByte = *msg; msg++)
    SPI.transfer(enviarByte);

  digitalWrite(SS, HIGH);

  delay(1);
}
