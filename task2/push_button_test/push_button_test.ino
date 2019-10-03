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

// default values to calibrate joystic
int xLow = 1000;
int xHigh = 0;
int yLow = 1000;
int yHigh = 0;

// calibrate the joystick 
void calibrate_joystick() {

  int x = analogRead(joyX);
  int y = analogRead(joyY);
  
  if (x < xLow) {
    xLow = x;
    Serial.println(xLow);
   }
  else if (x > xHigh) {
    xHigh = x;
    Serial.println(xHigh);
   }

   if (y < yLow) {
    yLow = y;
    Serial.println(yLow);
   }
  else if (y > yHigh) {
    yHigh = y;
    Serial.println(yHigh);
   }

}

void loop() {

  calibrate_joystick();

  int xValue = analogRead(joyX);
  int yValue = analogRead(joyY);

  if (xValue == xLow) {
    Serial.println("LEFT");
    delay(500);
   }
   else if (xValue == xHigh) {
    Serial.println("RIGHT");
    delay(500);
   }
  
   else if (yValue == yHigh) {
    Serial.println("DOWN"); // orientation seems flipped
    delay(500);
   }

   else if (yValue == yLow) {
    Serial.println("UP"); // orientation seems flipped
    delay(500);
    }
  //Serial.print(xValue);
  //Serial.print("\t");
  //Serial.println(yValue);

  switch_state = digitalRead(Switch);
  if (switch_state == LOW && switch_state != prev_state) {
    
    mode = (mode + 1) % 3;
    Serial.println(mode);
    
    prev_state = LOW;
    delay(500);
  }

   if (switch_state == HIGH && switch_state != prev_state) {
    
    mode = (mode + 1) % 3;
    Serial.println(mode);
    
    prev_state = HIGH;
    delay(500);
  }
  
  // prints "1" when the button is pressed
  push_button_state = digitalRead(PushButton);
  if (push_button_state == LOW ) { 
    Serial.println(-1);
    
    if (mode == 0) {
      delay(2000);
     }
    else {
     delay(500);
    }
  }

}
