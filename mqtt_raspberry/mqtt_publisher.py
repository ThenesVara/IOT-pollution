'''Publie donnees sur l'adresse IP en mqtt
-> fonctionne que si connecté au meme réseau

'''

import paho.mqtt.client as paho

#adresse ip de ou on envoi les donnees
broker="192.168.200.180"
port=1883

def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass

client1= paho.Client("test")                           #create client object
client1.on_publish = on_publish                          #assign function to callback
client1.connect(broker,port)                                 #establish connection
ret= client1.publish("test","on")                   #publish
