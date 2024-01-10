
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(3, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int state = digitalRead(3);

  Serial.print("value: "); Serial.println(state);
}
