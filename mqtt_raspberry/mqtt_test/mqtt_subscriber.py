''' S'abonne en mqtt aux topics a,b,c'''

import paho.mqtt.client as mqtt



def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe([("a", 1), ("b", 1), ("c", 1)])



def on_message(client, userdata, message):

    print("Message received: " + message.topic + " : " + str(message.payload))

    




broker_address = "localhost"  # Broker address #10.3.141.71 adresse ip de mon pc
port = 1883  # Broker port

#protocole TLS : securisé ----------- > https://www.frugalprototype.com/mqtt-tls/

#user = "rir"      #Connection username
#password = "rir"  #Connection password

client = mqtt.Client()  # create new instance

client.on_connect = on_connect  # attach function to callback
client.on_message = on_message  # attach function to callback
#client.username_pw_set(username = user, password = password)    #set username and password

client.connect(broker_address, port=port)  # connect to broker

client.loop_forever()