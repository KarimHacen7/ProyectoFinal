/*
This code is intended for testing the Logic and Protocol Analyzer as a UART Tx Line, in an Arduino Mega
*/

//Serial, Tx pin is Digital 18 on the board
void setup() {
  Serial1.begin(250000);
}

void loop() {
  Serial1.println("Hello from UART");
  delay(1);
}
