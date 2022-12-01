# Procédure pour envoyer des données sur adafruit

## Compte 

- Créer son compte adafruit : https://accounts.adafruit.com/users/sign_in

- Se connecter sur : io.adafruit.com

- Aller sur API Key :

![1](https://user-images.githubusercontent.com/114569016/205045411-33ab2a49-ed61-4fa2-a527-3505fdc5aed3.png)

- Récupérer IO Key -> username et active Key

![2](https://user-images.githubusercontent.com/114569016/205045447-8f827e6a-b65a-4093-b0fc-36b8ee353c95.png)

Ces informations permettront à la pycom d'envoyer les infos sur votre compte adafruit


## Création Feed et Dashboard

### Feed
Pour chaque type de donnée, il faut créer un feed sur votre compte adafruit.

![3](https://user-images.githubusercontent.com/114569016/205045633-2a1e71dd-511a-4265-834a-3918a0e78603.png)

exemple : Création d'un feed temperature

![4](https://user-images.githubusercontent.com/114569016/205045649-b821655c-c187-4531-b85d-01803b383405.png)


### Dashboard
Dans le dashboard, vous pourrez récupérer et afficher toutes les données qui vous intéressent.

![5](https://user-images.githubusercontent.com/114569016/205045666-8ef42a42-77ef-43b9-a1e4-19300ccefc07.png)

![6](https://user-images.githubusercontent.com/114569016/205045678-c40796b3-bbb4-4f81-9194-8dc2e6f26719.png)


## Code MQTT
Dans le code, il vous faudra modifier les informations du wifi, de votre compte adafruit (IO Key) et le nom des topics.

- Wifi : Modifier votre nomwifi et motdepasse selon le wifi sur lequel votre pycom se connecte

![8](https://user-images.githubusercontent.com/114569016/205045828-afa3d022-82c8-44a6-a023-693c73c7e3c4.png)


- IO Key : Modifier user et password des paramètres MQTT

![9](https://user-images.githubusercontent.com/114569016/205045743-4fe1b058-a10f-41dd-a336-ff42f82665bc.png)

- Topic : dans les clients.subscribe et client.publish modifier le nom du topic

Nom du topic : 
![7](https://user-images.githubusercontent.com/114569016/205045957-5b6cf9b2-1179-4c31-b8a6-a33692dd4334.png)

![10](https://user-images.githubusercontent.com/114569016/205045866-24a4a01f-d82c-4423-8c8d-96fc44e5c3f3.png)

![11](https://user-images.githubusercontent.com/114569016/205045881-101009f5-e424-4d30-9a6d-142375c9c5bb.png)

## Librairie 

### Ajout d'une librairie
Récupérer le fichier librairie puis upload sur la pycom 

- exemple : librairie mqtt.py : https://github.com/pycom/pycom-libraries/blob/master/lib/mqtt/mqtt.py
Il faudra upload cette librairie sur la pycom.

