// Basic demo for accelerometer readings from Adafruit MPU6050

#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>
#include <String.h>

Adafruit_MPU6050 mpu;

int one_iter = 0;
int cnt = 0;

String mode = "done";

void setup(void) {
  Serial.begin(115200);
  while (!Serial)
    delay(10); // will pause Zero, Leonardo, etc until serial console opens

  Serial.println("Adafruit MPU6050 test!");

  // Try to initialize!
  if (!mpu.begin()) {
    Serial.println("Failed to find MPU6050 chip");
    while (1) {
      delay(10);
    }
  }
  Serial.println("MPU6050 Found!");

  mpu.setAccelerometerRange(MPU6050_RANGE_8_G);
  mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);
  
  delay(100);
}

void loop() {

  if(Serial.available()){
    mode = Serial.readString();
    Serial.println(mode);
  }
  /* Get new sensor events with the readings */
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);

  float x = g.gyro.x;
  float y = g.gyro.y;
  float z = g.gyro.z;

  if(mode.equals("run")||mode.equals("jump")){
    move(x, y, z);
  }
  else if(mode.equals("init")){
    one_iter = 0;
    cnt = 0;
  }
}

void move(int x, int y, int z){
  if(abs(x) > 1 || abs(y) > 1 || abs(z) > 1){
    one_iter++;
    delay(300);
  }
  if(one_iter==1&&mode.equals("jump")){
    cnt_init();
  }
  else if(one_iter==2&&mode.equals("run")){
    cnt_init();
  }
  delay(300);
}

void cnt_init(){
  cnt++;
  one_iter=0;
  Serial.println(cnt);
}