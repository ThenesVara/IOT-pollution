## MQTT entre un ordinateur et une raspberry Pi (ou 2 ordinateurs) :

Install Librairies :
```
pip3 install openpyxl
pip3 install paho-mqtt
```
Mosquitto
```
sudo apt-get install -y mosquitto mosquitto-clients
sudo systemctl enable mosquitto
```

- Les 2 ordinateurs doivent être connectés au même réseau

Ordinateur 1 : publisher

Ordinateur 2 : subscriber

- Un ordinateur 1 peut alors publier des données 

- L'ordinateur 2 va s'abonner aux données publiés par l'ordinateur 1 et récupérer ces données

- Ensuite, l'ordinateur 2 peut alors écrire les données récupérés sur un excel pour ordonner et organiser les données
