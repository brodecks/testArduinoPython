import serial
import csv
import time

# Remplace 'COM3' par le port de ton Arduino (ex: 'COM4' ou '/dev/cu.usbmodem...' sur Mac)
PORT = 'COM4' 
BAUD = 9600

ser = serial.Serial(PORT, BAUD)
time.sleep(2) # Pause pour laisser l'Arduino redémarrer

print("Enregistrement en cours... Appuie sur Ctlr+C pour arrêter.")

with open('mesures_arduino.csv', mode='w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Horodatage', 'Distance_cm']) # En-têtes

    try:
        while True:
            if ser.in_waiting > 0:
                ligne = ser.readline().decode('utf-8').strip()
                if ligne:
                    temps = time.strftime('%H:%M:%S')
                    writer.writerow([temps, ligne])
                    print(f"{temps} -> {ligne} cm")
    except KeyboardInterrupt:
        print("\nEnregistrement terminé. Fichier 'mesures_arduino.csv' créé !")
        ser.close()