# This example will send a message to a topic on the Adafruit MQTT broker and then also subscribe to the same topic,
# in order to show how to use the subscribe functionality.

# Go to your adafruit account : io.adafruit.com/PFE/feeds/temperature
#-----------------------------------------------------------------------
from SI7006A20 import SI7006A20
from LTR329ALS01 import LTR329ALS01
from pycoproc_1 import *
from mqtt import MQTTClient
from network import WLAN
import machine
import time

#-----------------------------------------------------------------------

# led de couleur BLEUE
pycom.rgbled(0x0080FF)

# initialisation variables pour le capteur de temperature et de lumière
py = Pycoproc(Pycoproc.PYSENSE)
dht = SI7006A20(py)
li = LTR329ALS01(py)

def sub_cb(topic, msg):
    print(msg)

#-----------------------------------------------------------------------

# connexion au routeur
wlan = WLAN(mode=WLAN.STA)
wlan.connect("iPhone de Axel", auth=(WLAN.WPA2, "40Gopourtoi"), timeout=5000) #Nom wifi et password

# indique que l'on est connecté au WIFI
while not wlan.isconnected():
    machine.idle()
print("Connected to WiFi\n")
pycom.rgbled(0x00FF00)
time.sleep(2)

#-----------------------------------------------------------------------

# création client pour l'envoi des 2 valeurs des 2 capteurs
client = MQTTClient("device_id", "io.adafruit.com", user="PFE_Pycom", password="aio_WoPB32roIJPXq6uKkwBlVHePiKiu", port=1883) #votre user adafruit et password
client.connect()

#-----------------------------------------------------------------------

# boucle qui envoie les valeurs sur adafruit.com
while True:
    
    # partie pour la temperature 
    print("Sending Temp")
    temperature = str("{0:.1f}".format((dht.temperature()))) # prendre la valeur du capteur
    print("la temperature est : ", temperature) 
    client.publish(topic="PFE_Pycom/feeds/temperature", msg=temperature) # envoie de la valeur du capteur
    pycom.rgbled(0xFFD700) # couleur jaune : valeur envoyé
    
    # attente pour s'assurer de l'envoie des valeurs
    time.sleep(2)

    # partie pour la lumière
    print("Sending Lux")
    li_data = li.light()# prendre les valeurs du capteur
    lumiere = str(li_data[0])# prendre la valeur du capteur intéressante
    print("la lumiere est de : ", lumiere)
    client.publish(topic="PFE_Pycom/feeds/lumiere", msg=lumiere) # envoie de la valeur du capteur
    pycom.rgbled(0xFF0000) # couleur rouge : valeur envoyé
    
    time.sleep(5) # temps avant de recommencer la boucle
  
