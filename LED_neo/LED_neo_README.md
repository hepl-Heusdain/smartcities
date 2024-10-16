## Description
Il nous est demandé d'écrire un code permettant de contrôler une LED RGB en fonction d'un volume sonore capté
Les consignes exactes de cet exercice se trouvent dans ce PDF : [Exercice4.pdf](https://github.com/user-attachments/files/17396857/Exercice4.pdf)

Les différents modules sont connectés comme suit :
- Capteur Volume sur ADC0
- LED RGB sur Pin18
- Potentiomètre sur ADC1

## Versions
[LED_neo_1.0.py](https://github.com/hepl-Heusdain/smartcities/blob/main/LED_neo/LED_neo_1.0.py)

La LED RGB passe du vert au rouge lorsqu'un pic de volume est détecté. La sensibilité du capteur peut être ajustée via le potentiomètre

## Rpi Pinout
![302113634-20d19fc4-b9c3-4903-9ec8-b62cda90aee3](https://github.com/user-attachments/assets/a88ab59c-e48d-4154-8099-57b1d01e0204)

