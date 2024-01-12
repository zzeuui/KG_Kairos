#include <Servo.h>
#include <math.h>

Servo myservo1;
Servo myservo2;
Servo myservo3;

int servoPin1 = 5 ;
int servoPin2 = 6 ;
int servoPin3 = 9 ;

int curr_dx = 0;
int curr_dy= 0;

void setup() {

  Serial.begin(115200);

  pinMode (servoPin1, OUTPUT);
  pinMode (servoPin2, OUTPUT);
  pinMode (servoPin3, OUTPUT);

  myservo1.attach(servoPin1); //위아래
  myservo2.attach(servoPin2); //양옆
  myservo3.attach(servoPin3); //카메라
  
}

void loop() {
  curr_dx = myservo2.read(); 
  curr_dy = myservo1.read();

  String ret = "";
  ret = String(curr_dx) + ':' + String(curr_dy);

  if(Serial.available()){

    String data = Serial.readString();

    int a = data.indexOf("a");
    int b = data.indexOf("b");
    int c = data.indexOf("c");
    delay(500);

    String dx = data.substring(a+1, b);
    String dy = data.substring(b+1, c);
    
    int dxx = dx.toInt();
    int dyy = dy.toInt();

    int nt_x=curr_dx+dxx;
    int nt_y=curr_dy+dyy;

    ret = ret + ':' + String(curr_dx);
    ret = ret + ':' + String(curr_dy);

    myservo1.write(nt_x);
    myservo2.write(nt_y);

    curr_dx=nt_x;
    curr_dy=nt_y;

    ret = ret + ':' + String(curr_dx);
    ret = ret + ':' + String(curr_dy);

    Serial.println(ret);
  }
  else{
    Serial.println("fail");
    delay(500);
  }
}
