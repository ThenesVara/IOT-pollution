import paho.mqtt.client as paho
import time
from datetime import datetime


#adresse ip de où on envoi les donnees
broker="192.168.200.180"
port=1883


#create client object
client1= paho.Client("test1")
client2= paho.Client("test2")
         
client1.connect(broker,port)
client2.connect(broker,port)#establish connection



for i in range (5):
    ret= client1.publish("test1",i)#publish temperature
    print(datetime.now(),"data 1 published \n")
    time.sleep(0.1)
    
    ret2= client2.publish("test2", 28.1+i)#publish pollution
    print(datetime.now(),"data 2 published \n")
    
    time.sleep(0.1)


    
