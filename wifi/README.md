# Procédure pour envoyer des données sur adafruit

## Création Compte 

- Créer son compte adafruit : https://accounts.adafruit.com/users/sign_in

- Se connecter sur : io.adafruit.com

- Aller sur API Key :

![1](https://user-images.githubusercontent.com/114569016/205045411-33ab2a49-ed61-4fa2-a527-3505fdc5aed3.png)

- Récupérer IO Key -> username et active Key

<img src="https://user-images.githubusercontent.com/114569016/205045447-8f827e6a-b65a-4093-b0fc-36b8ee353c95.png" width=50% height=50%>

Ces informations permettront à la pycom d'envoyer les infos sur votre compte adafruit


## Création Feed et Dashboard

### Feed
Pour chaque type de donnée, il faut créer un feed sur votre compte adafruit.

<img src="https://user-images.githubusercontent.com/114569016/205045633-2a1e71dd-511a-4265-834a-3918a0e78603.png" width=50% height=50%>


Exemple : Création d'un feed temperature

<img src="https://user-images.githubusercontent.com/114569016/205045649-b821655c-c187-4531-b85d-01803b383405.png" width=50% height=50%>

### Dashboard
Dans le dashboard, vous pourrez récupérer et afficher toutes les données qui vous intéressent.

<img src="https://user-images.githubusercontent.com/114569016/205045666-8ef42a42-77ef-43b9-a1e4-19300ccefc07.png" width=50% height=50%>

<img src="https://user-images.githubusercontent.com/114569016/205045678-c40796b3-bbb4-4f81-9194-8dc2e6f26719.png" width=50% height=50%>

<img src="https://user-images.githubusercontent.com/114569016/205047414-a4c42ec8-2402-4ae1-a0ac-b83bf0963196.png" width=50% height=50%>



### Enregistrer les données obtenues 

Dans votre compte adafruit, dans vos feeds, vous pouvez enregistrer les données (en local).

![image](https://user-images.githubusercontent.com/114569016/213159129-e463fde0-450d-466e-a237-f9878bdd5949.png)

- Enregistrer les données en csv

![image](https://user-images.githubusercontent.com/114569016/213160177-dc19ae3c-308c-4914-9d90-1dfcfae9c11e.png)

- Ouvrir excel

- Importer le fichier de données csv 

![image](https://user-images.githubusercontent.com/114569016/213159948-23fd222c-c309-400a-8eee-ddd039d89e36.png)

- Vous pouvez modifier le nom et organiser vos données par période, par localisation, dans des classeurs etc...

![image](https://user-images.githubusercontent.com/114569016/213160893-281aad4d-f849-4886-98c6-07665778d6ec.png)


### Donnes xlsx en courbes

https://github.com/ThenesVara/IOT-pollution/tree/main/Raspberry%20server/Database%20php%20raspberry%20local/csv_data_courbes_excel#donnes-xlsx-en-courbes






## Code MQTT

Dans le code, il vous faudra modifier les informations du wifi, de votre compte adafruit (IO Key) et le nom des topics.

- Wifi : Modifier votre nomwifi et motdepasse selon le wifi sur lequel votre pycom se connecte

![8](https://user-images.githubusercontent.com/114569016/205045828-afa3d022-82c8-44a6-a023-693c73c7e3c4.png)


- IO Key : Modifier user et password des paramètres MQTT

![9](https://user-images.githubusercontent.com/114569016/205045743-4fe1b058-a10f-41dd-a336-ff42f82665bc.png)

- Topic : dans les clients.subscribe et client.publish modifier le nom du topic

Nom du topic : Thenes/feeds/temperature

![10](https://user-images.githubusercontent.com/114569016/205045866-24a4a01f-d82c-4423-8c8d-96fc44e5c3f3.png)

![11](https://user-images.githubusercontent.com/114569016/205045881-101009f5-e424-4d30-9a6d-142375c9c5bb.png)

PS : la donnee temperature envoyée est une chaine de caractere.

## Librairie 

### Ajout d'une librairie
Récupérer le fichier librairie puis upload sur la pycom 

- exemple : librairie mqtt.py : https://github.com/pycom/pycom-libraries/blob/master/lib/mqtt/mqtt.py

Enregistrer le fichier mqtt.py dans votre projet.

Upload cette librairie sur la pycom.

Ensuite, vous pouvez importer la librairie mqtt dans votre code.

![image](https://user-images.githubusercontent.com/114569016/212953700-fc79f1d5-4beb-4d97-ba22-1008e7dfbf21.png)


