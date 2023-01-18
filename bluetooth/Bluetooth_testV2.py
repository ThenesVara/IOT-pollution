from network import Bluetooth
from machine import Timer
import ubinascii

battery = 100
update = False
donnee = [] # créer une list vide
def conn_cb(chr):
    events = chr.events()
    if events & Bluetooth.CLIENT_CONNECTED:
        print('client connected')
    elif events & Bluetooth.CLIENT_DISCONNECTED:
        print('client disconnected')
        update = False

def chr1_handler(chr, data):
    global battery
    global update
    global donnee
    events = chr.events()
    print("events: ",events)
    if events & (Bluetooth.CHAR_READ_EVENT | Bluetooth.CHAR_SUBSCRIBE_EVENT):
        chr.value(str(donne)) #transforme la liste donnee en string and l'envoie
        print("transmitted :", donnee)
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
def update_handler(update_alarm):
    global battery
    global update
    global donnee
    donnee.append(battery)#ajoute dans la liste donnee la valeur ponctuel de battery
    battery-=10

    if battery == 0:
        donnee.clear() # vide la list
        battery = 100
    if update:
        chr1.value(donnee) # envoie la valeur de la batterie
        print(donnee)

update_alarm = Timer.Alarm(update_handler, 1, periodic=True)
