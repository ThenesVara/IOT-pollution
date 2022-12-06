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

# led de couleur BLEUE
pycom.rgbled(0x000020)
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
# connexion au broker MQTT Adafruit
topic=["PFE_Pycom/feeds/temperature", "PFE_Pycom/feeds/lumiere", "PFE_Pycom/feeds/altitude", "PFE_Pycom/feeds/humidite", "PFE_Pycom/feeds/control"]

client = MQTTClient("Pycom", "io.adafruit.com", user="PFE_Pycom", password="aio_WoPB32roIJPXq6uKkwBlVHePiKiu", port=1883)
client.set_callback(sub_cb) # definition de la fonction de callback pour le topic control
client.connect()
client.subscribe(topic=topic[4]) # subscribe au topic control
print("Connected")

#-----------------------------------------------------------------------
# boucle qui envoie les valeurs sur adafruit.com

cycles = 0 # initialisation des cycles

while True:
    # prendre la valeur des capteurs
    data=[capteurs.temperature(), capteurs.lux(), capteurs.altitude(), capteurs.humidity()]

    for i in range(4):
        pycom.rgbled(0x000000)
        client.publish(topic=topic[i],msg=data[i])
        client.check_msg() # regarder quels messages ont été envoyé
        print("Message envoye a : " + topic[i] + " | Valeur = " + data[i])
        pycom.rgbled(0x200000)
        time.sleep(1)
        # attente pour s'assurer de l'envoie des valeurs
    
    cycles += 1   # comptage des cycles

    pycom.rgbled(0x000020)
    time.sleep(5) # temps avant de recommencer la boucle
  
