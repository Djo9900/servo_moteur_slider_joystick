import tkinter as tk
import serial
import threading
import time

# Connexion au port série
try:
    arduino = serial.Serial('COM3', 9600, timeout=1)  
    time.sleep(2)  # Laisser le temps à l'Arduino de redémarrer
except:
    print("Erreur d'ouverture du port série")
    arduino = None

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Contrôle Servo avec Joystick")

# Slider graphique pour afficher la valeur lue
slider = tk.Scale(fenetre, from_=0, to=180, orient=tk.HORIZONTAL,
                  label="Position du Servo (par Joystick)", length=400)
slider.set(90)
slider.pack(padx=20, pady=20)

# Fonction exécutée en parallèle pour lire les données série
def lire_joystick():
    while True:
        if arduino and arduino.in_waiting:
            try:
                ligne = arduino.readline().decode().strip()
                if ligne.isdigit():
                    valeur = int(ligne)
                    if 0 <= valeur <= 180:
                        slider.set(valeur)
                        # (Optionnel) renvoyer la commande à l'Arduino
                        arduino.write(f"{valeur}\n".encode())
            except Exception as e:
                print(f"Erreur lecture série : {e}")

# Lancer le thread en arrière-plan
threading.Thread(target=lire_joystick, daemon=True).start()

# Démarrer l’interface
fenetre.mainloop()

