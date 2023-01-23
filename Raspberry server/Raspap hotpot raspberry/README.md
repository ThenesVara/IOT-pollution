# Pycom - raspberry pi

## Tutoriel - RASPAP Hotspot raspberry Pi

Tutoriel mise en place du hotspot de la raspberry : 
- https://raspap.com/#quick

- Vidéo tutoriel : https://www.youtube.com/watch?v=QWP81nG9zH0&ab_channel=Devyan

## Instructions sur la raspberry:
```
sudo apt-get update
sudo apt-get full-upgrade
sudo reboot
```
Install Raspap :
```
curl -sL https://install.raspap.com | bash
```

## Connexion avec un ordinateur sur le hotspot de la raspberry:

Pour la première connexion (setup) : 

![1](https://user-images.githubusercontent.com/114569016/210551508-2874c79d-1dcb-4222-9c13-47392259973c.png)

- Wifi : raspi-webgui
- Mot de passe : ChangeMe

Pour notre raspberry du RIR : 

- Wifi : RIRraspberry
- Mot de passe : Raspberrypi

Lorsque la connexion est faite:
- Ouvrir un navigateur internet 
- Se connecter à l'adresse Ip de la raspberry : 192.168.200.222  OU  10.3.141.1
- username = admin
- password = secret

![3](https://user-images.githubusercontent.com/114569016/210552647-2052c6e9-79e9-4a72-a0a0-40074dda2e61.png)

PS: Pensez à modifier le mot de passe !

![2](https://user-images.githubusercontent.com/114569016/210551571-e4974098-840f-49e7-86f1-7769938c61aa.png)


## Autres librairies (capteurs) :

voir dans IOT-pollution/wifi/lib/
