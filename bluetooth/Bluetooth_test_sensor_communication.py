from SI7006A20 import SI7006A20
from pycoproc_1 import *
import machine
import time
from network import Bluetooth
from machine import Timer
import ubinascii
import struct

# initialisation variables pour le capteur de temperature
py = Pycoproc(Pycoproc.PYSENSE)
dht = SI7006A20(py)

#################################################################################################
### Partie Bluetooth ###
longueur = 200
update = False
donnee = [ 0 for i in range(longueur)]
msg = [0 for i in range(3)]
def conn_cb(chr):
    events = chr.events()
    if events & Bluetooth.CLIENT_CONNECTED:
        print('client connected')
    elif events & Bluetooth.CLIENT_DISCONNECTED:
        print('client disconnected')
        update = False

def chr1_handler(chr, data): # fonction de transmission des donnée lorsqu'un event de lecture detecter

    global msg
    global update
    global donnee

    events = chr.events()
    print("events: ",events)
    if events & (Bluetooth.CHAR_READ_EVENT | Bluetooth.CHAR_SUBSCRIBE_EVENT):
        chr.value(str(msg)) #transforme la liste msg en string et l'envoie
        print("transmitted :", msg)
        if (events & Bluetooth.CHAR_SUBSCRIBE_EVENT):
            update = True

def uuid2bytes(uuid): # fonction qui permet de mettre l'addresse uuid dans le bon format pour pycom
    uuid = uuid.encode().replace(b'-',b'')
    tmp = ubinascii.unhexlify(uuid)
    return bytes(reversed(tmp))

bluetooth = Bluetooth()
bluetooth.set_advertisement(name='ProjIOT', manufacturer_data="Pycom", service_uuid=uuid2bytes('4fafc201-1fb5-459e-8fcc-c5c9c331914b')) #défini le nom, le manufacturer et l'addresse uuid de la pycom en bluetooth

bluetooth.callback(trigger=Bluetooth.CLIENT_CONNECTED | Bluetooth.CLIENT_DISCONNECTED, handler=conn_cb) #appel la fonction conn_cb dans le cas d'une conneciton ou deconnection du bleutooth
bluetooth.advertise(True)

srv1 = bluetooth.service(uuid=uuid2bytes('4fafc201-1fb5-459e-8fcc-c5c9c331914b'), isprimary=True,nbr_chars=1)

chr1 = srv1.characteristic(uuid=uuid2bytes('beb5483e-36e1-4688-b7f5-ea07361b26a8'), value=128) #client reads from here

chr1.callback(trigger=(Bluetooth.CHAR_READ_EVENT | Bluetooth.CHAR_SUBSCRIBE_EVENT), handler=chr1_handler) #applique la fonction chr1_handler dans le cas d'un retour avec lecture d êvenement

print('Start BLE service')
def update_handler(update_alarm): # fonction d'update des varaibles
    global update
    global donnee
    #boucle afin de remplir la liste de données des valeurs du capteurs
    for i in range(len(donnee)):
        donnee[i] = temperature
        if i == len(donnee): #reset la boucle une fois la dernière valeur remplis
            i = 0
    for i in range(0,len(donnee),1): # parcours toute les valeur de la liste de donnée
        for j in range (len(msg)): # valeur de donnée ajouté a la liste de message paquet de 3 valeurs
            msg[j] = donnee[i]
            if j == len(msg): # reset la boucle de remplissage de msg
                j = 0
        if i == (len(donnee)): #reset la boucle de parcours de donnee
            i = 0

    if update:

        chr1.value(str(msg)) # envoie la valeur de la batterie
        print(msg)
        print(donnee)

update_alarm = Timer.Alarm(update_handler, 3, periodic=True) #aplication de la fonction d'update variables à chaque update du timer
#################################################################
### Partie température###
while True: #lecture continue du capteur
    temperature = str("{0:.1f}".format((dht.temperature())))
