# Pycom - Hotspot raspberry Pi

pycom wifi to raspi hotspot.py : la pycom se connecte au hotspot de la raspberry Pi

## Vérification sur la raspberry Pi:

- Ouvrir un navigateur internet 
- Se connecter à l'adresse Ip de la raspberry : 192.168.200.222
- username = admin
- password = secret

Dans l'onglet DHCP - Liste des clients, vous pouvez observer l'adresse IP de la pycom (qui est connectée).

Sur le terminal, vous pouvez ping l'adresse IP de la pycom :
```
ping 10.3.141.107
``` 

