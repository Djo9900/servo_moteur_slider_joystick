#include <Servo.h>  // Inclusion de la bibliothèque Servo
Servo monServo;     // Création d'un objet Servo
const int joyX = A0; // Broche analogique utilisée pour lire l'axe X du joystick
void setup() {
  Serial.begin(9600);   // Initialisation de la communication série (pour Python)
  monServo.attach(9);   // Le servo est connecté à la broche numérique D9
}
void loop() {
  int val = analogRead(joyX);             // Lire la position horizontale du joystick (0 à 1023)
  int angle = map(val, 0, 1023, 0, 180);  // Convertir la valeur lue en angle (0° à 180°)
  Serial.println(angle);  // Envoyer la valeur de l'angle au port série (pour affichage ou interface Python)
  monServo.write(angle);  // Appliquer l'angle au servo pour le faire tourner
  delay(50);              // Pause de 50 ms pour lisser le signal (éviter les secousses)
}
