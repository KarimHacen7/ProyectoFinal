/*
This code is intended for testing the Logic and Protocol Analyzer as a UART Rx Line, in an Arduino Nano
*/

//Serial, Tx pin is TX1 on the board
void setup() {
  Serial.begin(250000, SERIAL_8E1);
}

void loop() {
  char incomingByte = 0;
  uint8_t bufferIndex = 0;
  if (Serial.available() > 0) {
    incomingByte = Serial.read();
    Serial.print(incomingByte);   
  }
}
