# Raspap (MQTT) - Hotspot raspberry

- Création d'un hotspot raspberry Pi (Raspap)

![image](https://user-images.githubusercontent.com/114569016/217320262-3d388469-ff79-4eec-a889-7ad60600b212.png)

Publisher :

- pycom data to adafruit with raspi hotspot.py : l'esp32 se connecte au hotspot de la raspberry pour envoyer des données à adafruit. La raspberry est en hotspot et connecté en ethernet (ou autre) à internet. Envoi des données.

- esp_micropython_data_to_broker_raspi_mqtt.py : l'esp32 se connecte au hotspot de la raspberry pour envoyer des données à adafruit. La raspberry est en hotspot et N'EST PAS CONNECTE à internet. Envoi des données. La raspberry peut récupérer les données du topic de l'esp32 avec : client_raspi_sub_to_esp32.py

Subscriber :

- client_raspi_sub_to_esp32.py : La raspberry s'abonne aux topics et récupère les données (en local) de l'esp32.

Il est posible de récupérer les données de l'excel et tracer des courbes.

# Raspberry (broker MQTT)

L'esp32 et la raspberry sont connecté sur le même réseau.

![image](https://user-images.githubusercontent.com/114569016/217320012-80b86254-34e4-4fc7-b1b1-321bfb910440.png)

- esp_micropython_data_to_broker_raspi_mqtt.py : esp32 qui envoi des données à la raspberry pi (micropython)

- esp_publish_raspi_broker_mqtt.ino : esp32 qui envoi des données à la raspberry pi (Arduino)

- client_esp_sub.py : Souscrit à tous les topics (de la raspberry et de l'esp32). Les données reçus sont affichés sur le terminal.


# Database php (sans MQTT)

![image](https://user-images.githubusercontent.com/114569016/217319862-06a2c00c-1e0b-4f70-8150-574215900e46.png)


- esp32_php_raspi.ino : esp32 qui envoi des données à la raspberry pi (sur la base de données php de la raspberry en local). L'esp32 et la raspi sont connectés sur le même réseau.

- csv_data_courbes_excel : Après avoir récupéré le fichier .csv (d'Adafruit ou la base de donées php) puis converti en .xlsx. Voir README.md

Il est posible de récupérer les données de l'excel et tracer des courbes.


