volatile uint8_t data = 0;

ISR(SPI_STC_vect)
{
  data = SPDR;
  
  SPDR = 'a';
}

void SPI_SlaveInit(void)
{
  /* Set MISO output, all others input */
  DDRB = (1<<DDB4); // pin 12 in arduino nano

  //      Interrupt Enable|SPI Enable|MSB First|SPI Slave|CLK Pol 0 |CLK Pha 0 | CLK BITS IGNORED
  SPCR = (1<<SPIE)        |(1<<SPE)  |(0<<DORD)|(0<<MSTR)|(0<<CPOL) |(0<<CPHA);
  
  sei();
}

int main (void)
{
  SPI_SlaveInit();
  while (true);
}
