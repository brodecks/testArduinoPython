import serial
import csv
import time


PORT = 'COM4' 
BAUD = 9600

ser = serial.Serial(PORT, BAUD)
time.sleep(2) # Pause pour laisser l'Arduino redémarrer

print("Enregistrement en cours... Appuie sur Ctlr+C pour arrêter.")

with open('mesures_arduino.csv', mode='w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Horodatage', 'Distance_cm'])

    try:
        while True:
            if ser.in_waiting > 0: #si un octet est dispo, lire la ligne
                ligne = ser.readline().decode('utf-8').strip()
                if ligne:
                    temps = time.strftime('%H:%M:%S')
                    writer.writerow([temps, ligne])
                    print(f"{temps} -> {ligne} cm")
    except KeyboardInterrupt:
        print("\nEnregistrement terminé. Fichier 'mesures_arduino.csv' créé !")
        ser.close()