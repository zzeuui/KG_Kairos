
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);

  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
}

void loop() {

  while(Serial.available()){
    Serial.println("start");
    String data = Serial.readString();
    int start = data.indexOf("a");
    int mid = data.indexOf("b");
    int end = data.indexOf("c");

    String direction = data.substring(start+1, mid);
    String speed = data.substring(mid+1, end);

    if(direction=="1"){ right(speed.toInt(), 3000);}
    else if(direction=="2"){ left(speed.toInt(), 3000);}
    else{ pause(); }
  }
}

void right(int speed, int time){
  analogWrite(9, 0);
  analogWrite(10, speed);
  delay(time);
}

void left(int speed, int time){
  analogWrite(9, speed);
  analogWrite(10, 0);
  delay(time);
}

void pause(){
  analogWrite(10, 0);
  analogWrite(9, 0);
}