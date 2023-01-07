#publier en mqtt les topics a, b, c 

import paho.mqtt.client as paho
import time

import numpy as np


'''PARAMETRES MQTT'''
#temps pendant lequel il envoit les positions
timer = 20

#adresse ip de où on envoi les donnees
broker="192.168.200.180" #192.168.200.180
port=1883

#create client object : topic name
client1= paho.Client("a")
client2= paho.Client("b")
client3= paho.Client("c")

#establish connection
client1.connect(broker,port)
client2.connect(broker,port)
client3.connect(broker,port)


while timer > 1:
    ret= client1.publish("a", int(1))#publish temperature
    time.sleep(0.3)
    ret2= client2.publish("b", float(2.5))#publish temperature
    time.sleep(0.3)
    ret3= client3.publish("c", float(2.1))#publish temperature
    time.sleep(0.3)
      
    print("Publie","a,b,c")
    print('timer:',timer)
        
    time.sleep(2) #attend x secs avant de republier
    timer -=2