#include <MPU6050_tockn.h>
#include <Wire.h>

MPU6050 mpu6050(Wire);

int cnt = 0;
void setup() {
  Serial.begin(9600);
  Wire.begin();
  mpu6050.begin();
  mpu6050.calcGyroOffsets(true);

  pinMode(11, OUTPUT);
}

void loop() {
  digitalWrite(11, LOW);

  mpu6050.update();

  float ret = 0;
  float ax = mpu6050.getAccX();
  float ay = mpu6050.getAccY();
  float az = mpu6050.getGyroZ();

  ret = pow(ax*ax + ay*ay + az*az, 0.5);
  //Serial.print("ret: "); Serial.println(ret);

  if(ret > 100){
    cnt++;
    Serial.print("ret: "); Serial.println(ret);
    Serial.print("cnt: "); Serial.println(cnt);

    digitalWrite(11, HIGH);
    delay(1000);
  }

}