''' Raspberry : - en hotspot
                - connecté en ethernet (ou autre à internet)
    l'esp32 se connecte au hotspot de la raspberry pour envoyer des données à adafruit
'''

from mqtt import MQTTClient
from network import WLAN
import machine
import pycom
import time

#envoi une valeur fixe
temperature = '5'

def sub_cb(topic, msg):
    print(topic,msg)

    
# Connexion à internet    
wlan = WLAN(mode=WLAN.STA)
wlan.connect("RIRraspberry", auth=(WLAN.WPA2, "Raspberrypi"), timeout=5000) #Nom wifi et password

while not wlan.isconnected():
    machine.idle()
print("Connected to WiFi\n")

# MQTT
client = MQTTClient("device_id", "io.adafruit.com",
                    user="Thenes", password="aio_EuCI24nsMnvcoWK9tBn2a1Amwokc", port=1883)

client.set_callback(sub_cb) # definition de la fonction de callback pour le topic control
client.connect()
client.subscribe(topic="Thenes/feeds/temperature")

while True:
    print("Sending ON")
    client.publish(topic="Thenes/feeds/temperature", msg=temperature) #message publié au topic indiqué
    time.sleep(5)
    print("Sending OFF")
    client.check_msg()
    time.sleep(5)
