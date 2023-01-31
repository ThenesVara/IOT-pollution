from mqtt import MQTTClient
from network import WLAN
import machine
import pycom
import time

temperature = '5'


def sub_cb(topic, msg):
    print(topic,msg)

#Connecte au wifi
wlan = WLAN(mode=WLAN.STA)
wlan.connect("Thenes", auth=(WLAN.WPA2, "thenesoppo"), timeout=5000) #Nom wifi et password
while not wlan.isconnected():
    machine.idle()
print("Connected to WiFi\n")


# Adress IP du wifi sur la raspi -> command sur le terminal : hostname -I 
# raspi et esp sur le meme reseau
client = MQTTClient("device_id", "192.168.171.144", port=1883)

client.set_callback(sub_cb) # definition de la fonction de callback pour le topic control
client.connect()

# Topic(s) auquel il souscrit
client.subscribe(topic="esp32/sensor1")

while True:
    print("Sending ON")
    client.publish(topic="esp32/sensor1", msg=temperature)
    time.sleep(1)
    print("Sending OFF")
    client.check_msg()
    time.sleep(1)