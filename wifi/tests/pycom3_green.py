# Exemple qui envoie des données des capteurs de la Pysense sur Adafruit en MQTT via Wifi
# Nécessite le fichier capteurs.py
# Go to your adafruit account ;)
#-----------------------------------------------------------------------
from mqtt import MQTTClient
from network import WLAN
import machine
import time
import pycom
import capteurs
#-----------------------------------------------------------------------

# led de couleur VERTE
pycom.rgbled(0x002000)
print("Starting ...")

# definition fonction pour répondre aux messages d'adafruit
def sub_cb(topic, msg):
    print(topic,msg)
    if msg == b'1':
        nb_cycles= str(cycles)
        print('Nombre de cycles : '+ nb_cycles)
        client.publish(topic="PFE_Pycom/feeds/cycles",msg=nb_cycles) # renvoie sur adafruit le nombre de cycles
        client.check_msg()

#-----------------------------------------------------------------------
# connexion WIFI

wlan = WLAN(mode=WLAN.STA)
wlan.connect("iPhone de Axel", auth=(WLAN.WPA2, "40Gopourtoi"), timeout=5000) #Nom wifi et password

while not wlan.isconnected():
    machine.idle()
print("Connected to WiFi\n")
pycom.rgbled(0x002000)
time.sleep(2)

#-----------------------------------------------------------------------
# boucle qui envoie les valeurs sur adafruit.com

cycles = 0 # initialisation des cycles

while True:

    print("Starting to Upload")
    client = MQTTClient("Pycom_Green", "io.adafruit.com", user="PFE_Pycom", password="aio_WoPB32roIJPXq6uKkwBlVHePiKiu", port=1883)
    client.connect()
    print("Connected")

    pycom.rgbled(0x000000)
    client.publish(topic="PFE_Pycom/feeds/pycoms",msg='Salle 3 : 13 C')
    client.check_msg() # regarder quels messages ont été envoyé
    print("Message envoye valeur | Salle 3 : 13 C ")
    pycom.rgbled(0xF00000)
    time.sleep(1)
    # attente pour s'assurer de l'envoie des valeurs

    client.disconnect()
    print("Disconnected")

    cycles += 1   # comptage des cycles

    pycom.rgbled(0x002000)
    time.sleep(20) # temps avant de recommencer la boucle
  
