Il nous est demandé d'écrire un code réalisant une horloge en utilisant un Servomoteur. L'heure doit être récupérée à partir d'internet.
Les consignes exactes de cet exercice se trouvent dans ce PDF : [Exercice5.pdf](https://github.com/user-attachments/files/17396724/Exercice5.pdf)

Les différents modules sont connectés comme suit :
- DHT11 sur Pin16
- LED sur Pin18
- Buzzer sur Pin20
- LCD sur I2C1
- Potentiomètre sur ADC0


[network_1.0.py](https://github.com/hepl-Heusdain/smartcities/blob/main/network/network_1.0.py)

Récupère l'heure via la connection WiFi et fait varier la position du servomoteur en fonction sur une base de 12H

[network_2.0.py](https://github.com/hepl-Heusdain/smartcities/blob/main/network/network_2.0.py)

Permet de changer de base de temps (h12 ou h24) par deux pression rapide du bouton poussoir (instable)

![302113634-20d19fc4-b9c3-4903-9ec8-b62cda90aee3](https://github.com/user-attachments/assets/a88ab59c-e48d-4154-8099-57b1d01e0204)

