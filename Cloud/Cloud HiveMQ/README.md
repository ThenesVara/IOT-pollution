# Choix du cloud

## Différents options en fonctions de la carte choisie
ESP 32 ou Pycom

### App Inventor : 
Passage par la connexion Bluetooth, base de données avec un retour graphique, langage : Scratch, pas disponible sur Apple

### Arduino IoT Cloud :
Très pratique et facile d'utilisation, inexploitable avec une pycom

### Cloud Pycom : 
Pas possible avec une ESP32

### Cloud HiveMQ :
Possible pour ESP32 et Pycom mais problème rencontré (voir plus bas)

### Cloud Adafruit :
Option choisie pour le projet


# Piste faisable mais abandonnée : HiveMQ

## Pour reprendre le projet
- se créer un compte sur HiveMQ : https://auth.hivemq.cloud/login?state=hKFo2SAxT09lUUVrQ0xGb09EMEFmVzBnX1M1c1c1OS02cmg4VqFupWxvZ2luo3RpZNkgR0c1QU0xMXhiQjNtNmVybTJNNGtsYnJnRk1OVzBqcmujY2lk2SBJYWpvNGUzMmp4d1VzOEFkRnhneFFuMlZQM1l3SVpUSw&client=Iajo4e32jxwUs8AdFxgxQn2VP3YwIZTK&protocol=oauth2&audience=hivemq-cloud-api&redirect_uri=https%3A%2F%2Fconsole.hivemq.cloud&scope=openid%20profile%20email&response_type=code&response_mode=query&nonce=MnpxY2U0TW5TbzJISm9wUUFuMXZ%2Bd1hQcGNMa29mSEREcExxT0lYUExwbQ%3D%3D&code_challenge=wiWpta9GXoFWfRTyo5rpy3d_TaJnHQ9XM0veiPDwXwo&code_challenge_method=S256&auth0Client=eyJuYW1lIjoiYXV0aDAtc3BhLWpzIiwidmVyc2lvbiI6IjEuMTMuNiJ9

- Pour la création des clusters et sa connexion... suivre les instructions d'ici : https://www.hivemq.com/docs/hivemq-cloud/introduction.html


Jusqu'à maintenant, les cluster ne se connecte qu'en local, notre objectif est de connecter la pycom au cloud via Wifi. 
Pour cela, nous avons utilisé les codes de ce dossier (Cloud HiveMQ).
Le dossier _lib.umqtt_ est celui qui a été utilisé pour faire la connexion avec le cloud (le dossier _lib.mqtt_ nous a aidé pour faire des tests).
Dans notre _main_, la lignes 18 correspond au transfert de données sur le cloud : 

![image](https://user-images.githubusercontent.com/119596360/220925142-d973937c-2c35-4073-9d81-aa3f8cce36c5.png)

Il faut trouver ce qu'attend HiveMQ comme données pour qu'il affiche les résusltats. 
De notre côté, nous avons réussi à envoyé des données sur le cloud mais l'affichage de celles-ci ne faisait pas. 
À vous de jouer ! (attention, HiveMQ n'est pas compatible sur certains navigateur)
