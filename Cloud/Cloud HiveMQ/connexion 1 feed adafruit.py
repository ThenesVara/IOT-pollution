import lib.capteurs
from lib.pycoproc_1 import *
from lib.mqtt import MQTTClient
from network import WLAN
import pycom
import machine
import time


# led de couleur BLEUE
#pycom.rgbled(0x0080FF)

# initialisation variables pour le capteur de temperature
py = Pycoproc(Pycoproc.PYSENSE)


# prendre la valeur de la temperature et de l'humidité du capteur
# !!! laisser la valeur en décimale/ entière sans indication pour avoir l'historique !!!
#temperature = str(lib.SI7006A20.SI7006A20.temperature)
temperature = lib.capteurs.temperature()
#temperature = '7'

def sub_cb(topic, msg):
    print(msg)

# connexion au routeur
wlan = WLAN(mode=WLAN.STA)
wlan.connect("OL", auth=(WLAN.WPA2, "trouducul"), timeout=5000) #Nom wifi et password

# indique que l'on est connecté au WIFI
while not wlan.isconnected():
    machine.idle()
print("Connected to WiFi\n")
#pycom.rgbled(0x0000FF)
time.sleep(2)

client = MQTTClient("device_id", "io.adafruit.com",user="Flixbrb", password="aio_Zsfe09sRpcEbpVGDrBmznBjK3wDX", port=1883) #votre user adafruit et password
client.connect()

#client.subscribe(topic="Flixbrb/feeds/temperature",qos=0)

# boucle qui envoie les données
while True:
    print("Sending Temp")
    client.publish(topic="Flixbrb/feeds/temperature", msg=temperature)
    client.check_msg()

    #pycom.rgbled(0x000000)
    time.sleep(5) # boucle pour envoyer les données toutes les X secondes
    #pycom.rgbled(0xFF0000) # permet de faire clignoter la led en rouge à chaque envoi de donnée