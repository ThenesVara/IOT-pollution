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
temperature = str("{0:.1f}".format((dht.temperature()))) + " deg C"


def sub_cb(topic, msg):
    print(msg)


# connexion au routeur
wlan = WLAN(mode=WLAN.STA)
wlan.connect("Nomwifi", auth=(WLAN.WPA2, "password"), timeout=5000) #Nom wifi et password

while not wlan.isconnected():
    machine.idle()
print("Connected to WiFi\n")


client = MQTTClient("device_id", "io.adafruit.com",
                    user="PFE_Pycom", password="aio_WoPB32roIJPXq6uKkwBlVHePiKiu", port=1883) #votre user adafruit et password

client.set_callback(sub_cb)
client.connect()
client.subscribe(topic="PFE_Pycom/feeds/temperature")

while True:
    print("Sending Temp")
    client.publish(topic="PFE_Pycom/feeds/temperature", msg=temperature)
    client.check_msg()

    time.sleep(10) #envoi data après X secondes
