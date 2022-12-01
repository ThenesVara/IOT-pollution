# IOT-pollution


## Wifi / Cloud :

Lire README.md pour connaitre la procedure pour envoyer des donnees de la pycom à adafruit

- connexion wifi.py : la pycom se connecte au wifi

- temperature wifi adafruit pycom.py : pycom envoi les informations de température (1 topic) à Adafruit. Les données sont visibles sur le compte adafruit sélectionné.

- connexion 2 feeds adafruit.py : pycom envoi les informations de température et luminosité (2 topics) à Adafruit


## Serveur raspberry Pi - Mqtt

- Connexion MQTT entre raspberry et un ordinateur (sur un même réseau) -> envoi d'information, enregistrement des valeurs dans un Excel et création de courbes à partir des données du Excel

## Bluetooth


# A faire :

## Bluetooth : 

- connexion bluetooth simple de la pycom en bluetooth

- Interface bluetooth (avec un télephone par exemple) qui récupère et affiche les données de la pycom 

-> les données doivent etre visible sur une interface (comme pour adafruit)

## Serveur :

- Création d'un serveur avec une raspberry Pi (avec module wifi ou raspi 4) - en Mqtt pour que la pycom puisse envoyer des informations à ce serveur.



# Les capteurs qu'on va recevoir :

Capteurs DFROBOTS : NH3, S02 et un autre
