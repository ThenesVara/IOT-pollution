#tutoriel pour se connecter au wifi

from network import WLAN
import machine
import pycom

pycom.heartbeat(False)

wlan = WLAN(mode=WLAN.STA)

nets = wlan.scan()
for net in nets:
    if net.ssid == 'raspi-webgui': #Mettre votre wifi
        print('Network found!')
        wlan.connect(net.ssid, auth=(net.sec, 'ChangeMe'), timeout=5000) #Mettre votre mot de passe
        pycom.rgbled(0xff00) 
        while not wlan.isconnected():
            machine.idle() # save power while waiting
        pycom.rgbled(0x7f7f00)
        print('WLAN connection succeeded!')
        break