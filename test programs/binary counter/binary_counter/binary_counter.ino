//storage variables
volatile uint8_t index = 0;

void setup() {
  cli();//stop interrupts
  
  DDRA = 0xFF; //set pins as outputs
  
  TCCR4A = 0;  // set entire TCCR1A register to 0
  TCCR4B = 0;
  TCCR4B |= (1 << WGM12) | (1 << CS10);// turn on CTC mode and Set CS10 bits for 1 prescaler
  TCNT4  = 0;  //initialize counter value to 0
  
   OCR4A = 63; // Square of 500 [KHz]
  // OCR4A = 31; // Square of 1 [MHz], not able to execute ISR quickly enough
  // enable timer compare interrupt
  TIMSK4 |= (1 << OCIE4A);
  sei();//allow interrupts
}

ISR(TIMER4_COMPA_vect) {
  index++;
  PORTA = index;
}

void loop() {
  //do other things here
  
}
