Les consignes exactes de cet exercice se trouvent dans ce PDF : [Exercice3.pdf](https://github.com/user-attachments/files/17187571/Exercice3.pdf)

Les différents modules sont connectés comme suit :
- DHT11 sur Pin16
- LED sur Pin18
- Buzzer sur Pin20
- LCD sur I2C1
- Potentiomètre sur ADC0


[I2C_1.0.py](https://github.com/hepl-Heusdain/smartcities/blob/main/I2C/I2C_1.0.py)

Affiche la valeur de l'ADC sur le LCD

[I2C_2.0.py](https://github.com/hepl-Heusdain/smartcities/blob/main/I2C/I2C_2.0.py)

Lecture et affichage des valeurs Set (fixée par le potentiomètre) & Ambient (via le DHT11)

[I2C_3.0.py](https://github.com/hepl-Heusdain/smartcities/blob/main/I2C/I2C_3.0.py)

Ajout des fonctions relatives au delta entre Set et Ambient

[I2C_3.1.py](https://github.com/hepl-Heusdain/smartcities/blob/main/I2C/I2C_3.1.py)

"ALARM" clignotte maintenant lur le LCD lorsque Ambient >> Set

![302113634-20d19fc4-b9c3-4903-9ec8-b62cda90aee3](https://github.com/user-attachments/assets/769ba007-b2aa-41cb-a855-35c6bf710a28)
