#include <Servo.h>
Servo monServo;
String donnees = "";
void setup() {
  Serial.begin(9600);
  monServo.attach(9); // D9 connecté au fil orange (signal) du SG92R
}
void loop() {
  // Lecture série
  while (Serial.available()) {
    char c = Serial.read();
    if (c == '\n') {
      int angle = donnees.toInt();   // Conversion string → int
      monServo.write(angle);         // Positionner le servo
      donnees = "";                  // Réinitialiser la chaîne
    } else {
      donnees += c; // Construction du message
    }
  }
}
