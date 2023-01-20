
# Librairies

Install Librairies :
```
pip3 install openpyxl
pip3 install matplotlib
```

# Enregistrer les données obtenues en xlsx

## Adafruit

Dans votre compte adafruit, dans vos feeds, vous pouvez enregistrer les données (en local).

![image](https://user-images.githubusercontent.com/114569016/213159129-e463fde0-450d-466e-a237-f9878bdd5949.png)

- Enregistrer les données en csv

![image](https://user-images.githubusercontent.com/114569016/213160177-dc19ae3c-308c-4914-9d90-1dfcfae9c11e.png)

- Ouvrir excel

- Importer le fichier de données csv 

![image](https://user-images.githubusercontent.com/114569016/213159948-23fd222c-c309-400a-8eee-ddd039d89e36.png)

- Vous pouvez modifier le nom et organiser vos données par période, par localisation, dans des classeurs etc...

![image](https://user-images.githubusercontent.com/114569016/213160893-281aad4d-f849-4886-98c6-07665778d6ec.png)

- Enregistrer les données en xlsx

### PHPmyadmin raspberry

- Se connecter sur votre serveur local (dans notre cas sur la raspberry Pi)

- Commande pour vérifier l'adresse IP : 
```
hostname -I
```

- Ouvrir une page internet sur : http://localhost/phpmyadmin/ OU http://ADRESSEIP/phpmyadmin/

![connect](https://user-images.githubusercontent.com/114569016/213706180-61395d9f-d97e-42cd-addb-1098cbd7ce4a.png)

- Notre raspberry database : 

username : pi

password : raspberry

- Aller sur les données que vous voulez récupérer : dans notre cas : esp_data/SensorData

- Exporter

![export](https://user-images.githubusercontent.com/114569016/213706227-256ec995-9484-42dc-ba68-ebc5e9f0f04b.png)

- Exporter en csv

![export csv](https://user-images.githubusercontent.com/114569016/213706386-ffb22dd7-2355-4e02-b90d-9ab405bc1c90.png)

- Sur libreoffice ou Excel, convertir le csv en xlsx

![convert xlsx](https://user-images.githubusercontent.com/114569016/213706549-baadc74f-0b49-40b1-af1b-b292a28f65fc.png)


# Courbes data

courbes_from_excel_data.py : Récupère les donnees de l'excel (.xlsx) et trace des courbes avec les topics

![courbe](https://user-images.githubusercontent.com/114569016/213712374-87381ecd-51c0-47be-9246-88c450b854fb.png)



