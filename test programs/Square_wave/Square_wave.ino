void setup() {
  // put your setup code here, to run once:
  DDRA = 0xFF;
}

void loop() {
  // put your main code here, to run repeatedly:
  PORTA = 0x00;
  asm("nop");
  asm("nop");
  asm("nop");
  asm("nop");
  asm("nop");
  //delay(1);
  PORTA = 0xFF;
  asm("nop");
  asm("nop");
  asm("nop");
  asm("nop");
  asm("nop");
  //delay(1);
}
