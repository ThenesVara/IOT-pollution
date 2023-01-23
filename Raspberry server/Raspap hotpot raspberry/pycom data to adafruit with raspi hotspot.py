from mqtt import MQTTClient
from network import WLAN
import machine
import pycom
import time

def settimeout(duration): pass

# connexion au Hotspot de la raspberry Pi
wlan = WLAN(mode=WLAN.STA)

nets = wlan.scan()
for net in nets:
    if net.ssid == 'Thenes': #Mettre votre wifi
        print('Network found!')
        wlan.connect(net.ssid, auth=(net.sec, 'thenesoppo'), timeout=5000) #Mettre votre mot de passe
        #pycom.rgbled(0xff00) 
        while not wlan.isconnected():
            machine.idle() # save power while waiting
        print('WLAN connection succeeded!')
        break

client = MQTTClient("joe", "192.168.200.222", port=1883)
client.settimeout = settimeout
client.connect()

client.publish("hello/world", "My publication")