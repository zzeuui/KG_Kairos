#include <SoftwareSerial.h>

#define blueTX 8
#define blueRX 7

char ser = 0;
char ble = 0;

SoftwareSerial HC06(blueTX, blueRX);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  HC06.begin(9600);
}

void func(){
  if(Serial.available()){
    ser = Serial.read();
    HC06.write(ser);
  }
  if(HC06.available()){
    ble = HC06.read();
    Serial.write(ble);
  }
}
void loop() {
  // put your main code here, to run repeatedly:
  func();
}
