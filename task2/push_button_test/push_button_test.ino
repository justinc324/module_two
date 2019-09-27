#define PushButton 15
#define joyX 27
#define joyY 26
#define Switch 17

void setup() {
  Serial.begin(9600);
  // put your setup code here, to run once:
  pinMode(PushButton, INPUT);
  pinMode(Switch, INPUT_PULLUP);

}

int xValue;
int yValue;

int switch_state;
int push_button_state;

int mode = 0;
int prev_state = digitalRead(Switch);

void loop() {

  int xValue = analogRead(joyX);
  int yValue = analogRead(joyY);
  //Serial.print(xValue);
  //Serial.print("\t");
  //Serial.println(yValue);

  switch_state = digitalRead(Switch);
  if (switch_state == LOW && switch_state != prev_state) {
    
    mode = (mode + 1) % 3;
    Serial.print(mode);
    
    prev_state = LOW;
    delay(500);
  }

   if (switch_state == HIGH && switch_state != prev_state) {
    
    mode = (mode + 1) % 3;
    Serial.print(mode);
    
    prev_state = HIGH;
    delay(500);
  }
  
  // prints "1" when the button is pressed
  push_button_state = digitalRead(PushButton);
  if (push_button_state == LOW ) { 
    Serial.print(1);
    delay(500);
  }

}
