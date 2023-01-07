# IOT-pollution


## Wifi / Cloud :

Lire README.md pour connaitre la procedure pour envoyer des donnees de la pycom à adafruit

- connexion wifi.py : la pycom se connecte au wifi

- temperature wifi adafruit pycom.py : pycom envoi les informations de température (1 topic) à Adafruit. Les données sont visibles sur le compte adafruit sélectionné.

- connexion 2 feeds adafruit.py : pycom envoi les informations de température et luminosité (2 topics) à Adafruit


## Raspberry Pi - Mqtt

- Connexion MQTT entre raspberry et un ordinateur (sur un même réseau) -> envoi d'information, enregistrement des valeurs dans un Excel et création de courbes à partir des données du Excel

## Hotspot raspberry pi

- Création d'un hotspot raspberry Pi
- Connexion possible à la raspberry Pi avec un ordinateur ou téléphone grâce au hotspot de la raspi et son adresse IP
- Connexion de la pycom sur le hotspot de la raspberry Pi

## Bluetooth

- Connexion bluetooth simple de la pycom en bluetooth


# A faire :

## Bluetooth : 

- Interface bluetooth (avec un télephone par exemple) qui récupère et affiche les données de la pycom 

-> les données doivent etre visible sur une interface (comme pour adafruit)

## Serveur hotspot raspi :

- Envoi d'information d'une pycom à la raspberry Pi



# Les capteurs qu'on va recevoir :

Capteurs DFROBOTS : NH3, S02 et un autre
