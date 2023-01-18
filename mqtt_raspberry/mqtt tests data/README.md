
### MQTT get data

mqtt_publisher_topics.py : publie des infos aux topics nommés test1, test2. Considéré comme le client qui publie à l'adresse IP du serveur.

mqtt_subscriber_text.py : souscrit aux infos des topics nommés tests1, tests2. Considéré comme le serveur en local. Ces données sont écrits sur un fichier : mqtt_update.txt

mqtt_subscriber_write_excel.py : souscrit aux infos des topics nommés tests1, tests2. Considéré comme le serveur en local. Ces données sont écrits sur un excel: data.xlsx -> (pas encore terminé)
