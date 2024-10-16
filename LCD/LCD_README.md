## Description
Il nous est demandé d'écrire un code permettant d'afficher la température actuelle ainsi que de la comparer à une valeur fixée via un potentiomètre. Certaines actions doivent ainsi être effectuées si la température fixée est plus basse que la température lue par le capteur.
Les consignes exactes de cet exercice se trouvent dans ce PDF : [Exercice3.pdf](https://github.com/user-attachments/files/17187571/Exercice3.pdf)

Les différents modules sont connectés comme suit :
- DHT11 sur Pin16
- LED sur Pin18
- Buzzer sur Pin20
- LCD sur I2C1
- Potentiomètre sur ADC0

## Versions
[LCD_1.0.py](https://github.com/hepl-Heusdain/smartcities/blob/main/LCD/LCD_1.0.py)

Affiche la valeur de l'ADC sur le LCD

[LCD_2.0.py](https://github.com/hepl-Heusdain/smartcities/blob/main/LCD/LCD_2.0.py)

Lecture et affichage des valeurs Set (fixée par le potentiomètre) & Ambient (via le DHT11)

[LCD_3.0.py](https://github.com/hepl-Heusdain/smartcities/blob/main/LCD/LCD_3.0.py)

Ajout des fonctions relatives au delta entre Set et Ambient

[LCD_3.1.py](https://github.com/hepl-Heusdain/smartcities/blob/main/LCD/LCD_3.1.py)

"ALARM" clignotte maintenant lur le LCD lorsque Ambient >> Set

## Rpi Pinout
![302113634-20d19fc4-b9c3-4903-9ec8-b62cda90aee3](https://github.com/user-attachments/assets/a88ab59c-e48d-4154-8099-57b1d01e0204)

