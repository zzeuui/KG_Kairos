#include <SoftwareSerial.h>

//motor
#define A_1A 6
#define A_1B 5
#define B_1A 10
#define B_1B 9

//ultra sensor
#define trig 2
#define echo 3

// bluetooth
#define blueTX 8wweedeswqwww gn bv 
#define blueRX 7 
SoftwareSerial HC06(blueTX, blueRX);

#include <Arduino.h> 
#include <U8x8lib.h>

#ifdef U8X8_HAVE_HW_SPI
#include <SPI.h>
#endif

U8X8_SSD1306_128X64_ALT0_HW_I2C u8x8(/* reset=*/ U8X8_PIN_NONE);

int speed = 255;

void setup() {
  Serial.begin(9600);

  //motor
  pinMode(A_1A, OUTPUT); pinMode(A_1B, OUTPUT);
  pinMode(B_1A, OUTPUT); pinMode(B_1B, OUTPUT);

  //ultra sensor
  pinMode(trig, OUTPUT); pinMode(echo, INPUT);

  //bluetooth
  HC06.begin(9600);

  u8x8.begin();
  
}

void loop() {
  u8x8.setFont(u8x8_font_px437wyse700b_2x2_r);

  char com = bluetooth();
  Serial.print("com: "); Serial.println(com);
  u8x8.drawString(0, 2, "command");
  if(com=='u'){
    user_mode();
    Serial.println("user");
  }
  else if(com=='a'){
    while(!(HC06.available())){
      u8x8.drawString(0, 2, "auto");
      Serial.println("auto");
      float distance = get_distance();
      right_path(distance);

    }
  }
  else if(com=='e'){
    u8x8.drawString(0, 2, "exit");
    Serial.println("exit");
    stop(5000);
  }
}

//user mode
void user_mode(){
  char com = 0;
  while(com != 'e'){
    com = bluetooth();
    u8x8.drawString(0, 2, "user");
    if(com=='f'){
      u8x8.drawString(0, 2, "for");
      while(!(HC06.available())){
        forward(0);
        Serial.println("for");
      }
    }
    else if(com=='b'){
      u8x8.drawString(0, 2, "bak");
      while(!(HC06.available())){
        backward(0);
        Serial.println("bak");
      }
    }
    else if(com=='r'){
      u8x8.drawString(0, 2, "rig");
      while(!(HC06.available())){
        turnright(0);
        Serial.println("rig");
      }
    }
    else if(com=='l'){
      u8x8.drawString(0, 2, "left");
      while(!(HC06.available())){
        turnleft(0);
        Serial.println("lef");
      }
    }
  }
  stop(0);
}

//func of motor
void right_path(int distance){
  int time = 500;

  if (distance < 15){
    //Serial.println("turn right");
    turnright(time);
  }
  else{
    //Serial.println("forward");
    forward(time);
  }
}

void forward(int time){
  analogWrite(B_1A, 0); analogWrite(B_1B, speed);
  analogWrite(A_1A, speed); analogWrite(A_1B, 0);
  delay(time);
}

void backward(int time){
  analogWrite(B_1A, speed); analogWrite(B_1B, 0);
  analogWrite(A_1A, 0); analogWrite(A_1B, speed);
  delay(time);
}

void turnleft(int time){
  analogWrite(B_1A, speed); analogWrite(B_1B, 0);
  analogWrite(A_1A, speed); analogWrite(A_1B, 0);
  delay(time);
}

void turnright(int time){
  analogWrite(B_1A, 0); analogWrite(B_1B, speed);
  analogWrite(A_1A, 0); analogWrite(A_1B, speed);
  delay(time);
}

void stop(int time){
  analogWrite(B_1A, 0); analogWrite(B_1B, 0);
  analogWrite(A_1A, 0); analogWrite(A_1B, 0);
  Serial.println("stop");
  delay(time);
}

//func of bluetooth
char bluetooth(){
  char ret = 0;
  if(Serial.available()){
    ret = Serial.read();
    HC06.write(ret);
  }
  if(HC06.available()){
    ret = HC06.read();
    Serial.write(ret);
  }
  return ret;
}

//ultra sensor
float get_distance() {
  // 트리거 핀에 10us 동안 신호를 보냅니다.
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);

  // 에코 핀에서 신호가 반사되어 돌아오는 시간을 측정합니다.
  float duration = pulseIn(echo, HIGH);

  // 거리를 계산합니다.
  float distance = (duration * 340) / 2 / 10000;

  return distance;
}
