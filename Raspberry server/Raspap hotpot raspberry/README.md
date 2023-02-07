# Pycom - raspberry pi

# Code

## Adafruit

- pycom data to adafruit with raspi hotspot.py :

La raspberry pi est en hotspot (en ethernet). L'esp32/pycom se connecte à l'hotspot de la raspberry pour envoyer des informations à adafruit.

- csv_data_courbes_excel : enregistrer les données d'adafruit en csv en .xlsx (excel) puis tracer les courbes en python.

## Local

- esp_micropython_data_to_broker_raspi_mqtt.py :

La raspberry pi est en hotspot (en local). L'esp32/pycom se connecte à l'hotspot de la raspberry pour envoyer des informations à la raspberry (en local).

- client_raspi_sub_to_esp32.py :

La raspberry s'abonne aux topics et récupère les données (en local) de l'esp32.

# Tutoriel - RASPAP Hotspot raspberry Pi

Tutoriel mise en place du hotspot de la raspberry : 
- https://raspap.com/#quick

- Vidéo tutoriel : https://www.youtube.com/watch?v=QWP81nG9zH0&ab_channel=Devyan

## Instructions sur la raspberry:
```
sudo apt-get update
sudo apt-get full-upgrade
sudo reboot
```
Install Raspap :
```
curl -sL https://install.raspap.com | bash
```

## Connexion avec un ordinateur sur le hotspot de la raspberry:

Pour la première connexion (setup) : 

![1](https://user-images.githubusercontent.com/114569016/210551508-2874c79d-1dcb-4222-9c13-47392259973c.png)

- Wifi : raspi-webgui
- Mot de passe : ChangeMe

Pour notre raspberry du RIR : 

- Wifi : RIRraspberry
- Mot de passe : Raspberrypi

Lorsque la connexion est faite:
- Ouvrir un navigateur internet 
- Se connecter à l'adresse Ip de la raspberry : 192.168.200.222  OU  10.3.141.1
- username = admin
- password = secret

![3](https://user-images.githubusercontent.com/114569016/210552647-2052c6e9-79e9-4a72-a0a0-40074dda2e61.png)

PS: Pensez à modifier le mot de passe !

![2](https://user-images.githubusercontent.com/114569016/210551571-e4974098-840f-49e7-86f1-7769938c61aa.png)


## Autres librairies (capteurs) :

voir dans IOT-pollution/wifi/lib/


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


