# IOT-pollution

## Wifi / Cloud :

Lire README.md pour connaitre la procedure pour envoyer des donnees de la pycom à adafruit

- lib : librairies utilisées à importer sur l'esp32 (voir README.md)

- mqtt pysense.py : pycom envoi les informations de plusieurs topics (temperature, lumiere, altitude, humidite, control) à Adafruit en mqtt par WiFi

## Hotspot raspberry pi

### Raspap (MQTT)

- Création d'un hotspot raspberry Pi (Raspap)

- pycom data to adafruit with raspi hotspot.py : l'esp32 se connecte au hotspot de la raspberry pour envoyer des données à adafruit. La raspberry est en hotspot et connecté en ethernet (ou autre) à internet.
    

### Database php (sans MQTT)

- esp32_php_raspi.ino : esp32 qui envoi des données à la raspberry pi (sur la base de données php de la raspberry en local). L'esp32 et la raspi sont connectés sur le même réseau.

- csv_data_courbes_excel : Après avoir récupéré le fichier .csv (d'Adafruit ou la base de donées php) puis converti en .xlsx. Voir README.md

Il est posible de récupérer les données de l'excel et tracer des courbes.

## Bluetooth

- 

## LoRa

- 

# A faire :
## Bluetooth : 

-

## LoRa

-

## Serveur hotspot raspi :

- la raspberry pi est le broker à laquelle l'esp envoi des données


# Les capteurs qu'on va recevoir :

Capteurs DFROBOTS : NH3, S02 et un autre
