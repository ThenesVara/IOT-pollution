from network import WLAN
from lib.umqtt import MQTTClient
import machine
import time

def settimeout(duration): 
     pass

wlan = WLAN(mode=WLAN.STA)
wlan.antenna(WLAN.EXT_ANT)
wlan.connect("OL", auth=(WLAN.WPA2, "trouducul"), timeout=5000)

while not wlan.isconnected(): 
     machine.idle()

print("Connected to Wifi\n")
# client = MQTTClient("Felix", "broker.hivemq.com", port=8884)
client = MQTTClient("Felix", "broker.hivemq.com")
client.settimeout = settimeout
# client.disconnect()
client.connect()

while True:
     print("Sending ON")
     client.publish("/lights", "ON")
     time.sleep(1)
     print("Sending OFF")
     client.publish("/lights", "OFF")
     time.sleep(1)
