#include <Servo.h>
Servo monServo;
void setup() {
  monServo.attach(9);  // Broche de signal du servo (SG92R)
}
void loop() {
  // --- État 1 : ARRÊT ---
  monServo.write(90);      // Signal d'arrêt pour servo à rotation continue  1500 ms
  delay(3000);             // Attendre 3 secondes
  // --- État 2 : MARCHE AVANT ---
  monServo.write(180);     // Rotation dans un sens (avant) 2500 ms
  delay(3000);             // Attendre 3 secondes
  // --- État 3 : MARCHE ARRIÈRE ---
  monServo.write(0);       // Rotation dans l'autre sens (arrière)  500 ms
  delay(3000);             // Attendre 3 secondes
}
