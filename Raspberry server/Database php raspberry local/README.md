# esp32 send data to raspberry Pi (lamp server)

## Mise en place de la base de données MySQL sur la raspberry Pi

1 - PHP Application et la base de donnée MySQL – Raspberry Pi

https://randomnerdtutorials.com/esp32-esp8266-raspberry-pi-lamp-server/

2 - Mise en place de la base de donnée MySQL

Voir 2 - https://randomnerdtutorials.com/esp32-esp8266-raspberry-pi-lamp-server/

3. PHP Script HTTP POST – Insérer des données dans la base de donnée MySQL

Voir 3 - https://randomnerdtutorials.com/esp32-esp8266-raspberry-pi-lamp-server/

4. PHP Script – Affichage du contenu de la base de données

Voir 4 - https://randomnerdtutorials.com/esp32-esp8266-raspberry-pi-lamp-server/ 

## ESP32

Voir 5 - https://randomnerdtutorials.com/esp32-esp8266-raspberry-pi-lamp-server/ 

La raspberry et l'esp32 doivent être connectés sur le même réseau 

- sur la raspberry pi : 

-> affiche l'adresse IP du réseau
```
hostname -I
``` 

- Sur arduino, ouvrir le code : esp32_php_raspi.ino

esp32_php_raspi.ino : se connecte sur le réseau renseigné et envoi des valeurs (à l'adresse IP) à la base de donnée de la raspberry pi

Vous pouvez modifier le code pour récupérer des données de capteurs