#include <MPU6050_tockn.h>
#include <Wire.h>
#include <Servo.h>

Servo myServo;

MPU6050 mpu6050(Wire);

int cnt = 0;
void setup() {
  Serial.begin(115200);
  Wire.begin();
  mpu6050.begin();
  mpu6050.calcGyroOffsets(true);
  
  myServo.attach(3);
}

void loop() {
  mpu6050.update();

  float ax = mpu6050.getAccX();
  ax *= 10;
  int ret = map(ax, -10, 10, 0, 180);
  myServo.write(ret);
  delay(20);

  //Serial.print("x: "); Serial.println(ax);
  //Serial.print("ret: "); Serial.println(ret);
}