# This example will send a message to a topic on the Adafruit MQTT broker and then also subscribe to the same topic,
# in order to show how to use the subscribe functionality.

# Go to your adafruit account : io.adafruit.com/PFE/feeds/temperature

from SI7006A20 import SI7006A20
from pycoproc_1 import *
from mqtt import MQTTClient
from network import WLAN
import machine
import time

# led de couleur BLEUE
pycom.rgbled(0x0080FF)

# initialisation variables pour le capteur de temperature
py = Pycoproc(Pycoproc.PYSENSE)
dht = SI7006A20(py)

# prendre la valeur de la temperature et de l'humidité du capteur
# !!! laisser la valeur en décimale/ entière sans indication pour avoir l'historique !!!
temperature = str("{0:.1f}".format((dht.temperature())))


def sub_cb(topic, msg):
    print(msg)


# connexion au routeur
wlan = WLAN(mode=WLAN.STA)
wlan.connect("Nomwifi", auth=(WLAN.WPA2, "password"), timeout=5000) #Nom wifi et password

# indique que l'on est connecté au WIFI
while not wlan.isconnected():
    machine.idle()
print("Connected to WiFi\n")
pycom.rgbled(0x0000FF)
time.sleep(2)


client = MQTTClient("device_id", "io.adafruit.com",
                    user="PFE_Pycom", password="aio_WoPB32roIJPXq6uKkwBlVHePiKiu", port=1883) #votre user adafruit et password

client.set_callback(sub_cb)
client.connect()
client.subscribe(topic="PFE_Pycom/feeds/temperature")

# boucle qui envoie les données
while True:
    print("Sending Temp")
    client.publish(topic="PFE_Pycom/feeds/temperature", msg=temperature)
    client.check_msg()

    pycom.rgbled(0x000000)
    time.sleep(5) # boucle pour envoyer les données toutes les X secondes
    pycom.rgbled(0xFF0000) # permet de faire clignoter la led en rouge à chaque envoi de donnée
