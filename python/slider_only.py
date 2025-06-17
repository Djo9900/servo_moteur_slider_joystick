import tkinter as tk
import serial
import time

# Connexion au port série
try:
    arduino = serial.Serial('COM3', 9600, timeout=1)  # Remplace COM3 si nécessaire
    time.sleep(2)
except:
    print("Erreur d'ouverture du port")
    arduino = None

# Création de la fenêtre Tkinter
fenetre = tk.Tk()
fenetre.title("Contrôle Servo via Slider")

# Création du slider
slider = tk.Scale(fenetre, from_=0, to=180, orient=tk.HORIZONTAL,
                  label="Position Servo", length=400)
slider.set(90)
slider.pack(padx=20, pady=20)
# Fonction appelée quand le slider change
def envoyer_commande(val):
    if arduino:
        commande = f"{val}\n"
        arduino.write(commande.encode())

# Mise à jour du servo lors du mouvement du slider
slider.config(command=envoyer_commande)

# Lancer l’interface
fenetre.mainloop()
