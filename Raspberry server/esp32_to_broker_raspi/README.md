# MQTT Network for data Exchange - Raspberry Pi & ESP32 Microcontrollers

https://github.com/jiteshsaini/mqtt-demo

## Code

### Raspberry

- rpi_mqtt_clients (Raspberry Pi code) :

client_esp_sub.py :

Souscrit à tous les topics (de la raspberry et de l'esp32). Les données reçus sont affichés sur le terminal. 

### ESP32 

#### Arduino

esp32_clients (ESP 32 code) : esp_publish_raspi_broker_mqtt.ino

Envoi des données au broker mqtt de la raspberry. 

#### Micropython
esp_micropython_data_to_broker_raspi_mqtt.py

Envoi des données au broker mqtt de la raspberry. 



## BROKER MQTT raspberry

### Raspberry 

#### Librairies

- Mosquitto :

```
sudo apt install -y mosquitto
sudo apt install -y mosquitto-clients
```

- Paho-mqtt :

```
sudo pip3 install paho-mqtt
```

- pip (if needed):

```
sudo apt install python3-pip
```


#### Start / stop mosquitto broker

```
sudo systemctl start mosquitto
sudo systemctl start mosquitto.service
sudo systemctl stop mosquitto.service
sudo systemctl restart mosquitto.service
```
Verifier l'etat du broker mqtt :
```
sudo systemctl status mosquitto
```
#### Activer moquitto-client

-> problème rencontré : https://stackoverflow.com/questions/24556160/mosquitto-client-obtain-refused-connection?fbclid=IwAR0WUCksy6o98-WXznslFZKJHkOA5ck3pmP6M_8lMOtzQn6aqq0ffJl-Jwc

-> Solution :

Modifier fichier mosquitto

```
cd /etc/mosquitto/
```

Modifier le fichier :

```
sudo nano moquitto.conf
```

Ajouter les lignes suivantes sur le fichier :

```
allow_anonymous true
listener 1883 0.0.0.0
```

Faire : Ctrl + X puis O. Cliquer sur la touche entrée. Le fichier a été modifié.

Relancer mosquitto :

```
sudo service mosquitto restart
```

