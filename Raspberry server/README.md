# Raspap (MQTT) - Hotspot raspberry

- Création d'un hotspot raspberry Pi (Raspap)

- pycom data to adafruit with raspi hotspot.py : l'esp32 se connecte au hotspot de la raspberry pour envoyer des données à adafruit. La raspberry est en hotspot et connecté en ethernet (ou autre) à internet. Envoi des données.

- esp_micropython_data_to_broker_raspi_mqtt.py : l'esp32 se connecte au hotspot de la raspberry pour envoyer des données à adafruit. La raspberry est en hotspot et N'EST PAS CONNECTE à internet. Envoi des données. La raspberry peut récupérer les données du topic de l'esp32 avec : client_raspi_sub_to_esp32.py

Il est posible de récupérer les données de l'excel et tracer des courbes.

# Raspberry (broker MQTT)

L'esp32 et la raspberry sont connecté sur le même réseau.

- esp_micropython_data_to_broker_raspi_mqtt.py : esp32 qui envoi des données à la raspberry pi (micropython)

- esp_publish_raspi_broker_mqtt.ino : esp32 qui envoi des données à la raspberry pi (Arduino)

- client_esp_sub.py : Souscrit à tous les topics (de la raspberry et de l'esp32). Les données reçus sont affichés sur le terminal.


# Database php (sans MQTT)

- esp32_php_raspi.ino : esp32 qui envoi des données à la raspberry pi (sur la base de données php de la raspberry en local). L'esp32 et la raspi sont connectés sur le même réseau.

- csv_data_courbes_excel : Après avoir récupéré le fichier .csv (d'Adafruit ou la base de donées php) puis converti en .xlsx. Voir README.md

Il est posible de récupérer les données de l'excel et tracer des courbes.


