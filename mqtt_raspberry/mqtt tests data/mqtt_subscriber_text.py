''' S'abonne en mqtt aux topics, recupere donnees et ecris sur un fichier txt'''

import paho.mqtt.client as mqtt
from datetime import datetime


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe([("test1", 1), ("test2", 1)])


def on_message(client, userdata, message):
    print("Message received: " + message.topic + " : " + str(message.payload))

    dateandtime = str(datetime.now())
    #si ce topic
    if message.topic == 'test1':
        #dans le fichier ci dessous -> ecris message
        with open('mqtt_update.txt', 'a+') as f:
            f.write("received topic temperature :")
            f.write(dateandtime)
            f.write(" : ")
            f.write(str(message.payload))
            f.write("\n")

    if message.topic == 'test2':
        #dans le fichier ci dessous -> ecris message
        with open('mqtt_update.txt', 'a+') as f:
            f.write("received topic pollution :")
            f.write(dateandtime)
            f.write(" : ")
            f.write(str(message.payload))
            f.write("\n")




broker_address = "localhost"  # Broker address
port = 1883  # Broker port

client = mqtt.Client()  # create new instance
client.on_connect = on_connect  # attach function to callback
client.on_message = on_message  # attach function to callback

client.connect(broker_address, port=port)  # connect to broker

client.loop_forever()