## Description
Il nous est demandé d'écrire un code permettant de jouer une mélodie à l'aide d'un Buzzer.
Les consignes exactes de cet exercice se trouvent dans ce PDF : [Exercice2.pdf](https://github.com/user-attachments/files/17187555/Exercice2.pdf)

Les différents modules sont connectés comme suit :
- Buzzer sur Pin27
- Potentiomètre sur ADC0

## Versions
[AD-PWM_1.0.py](https://github.com/hepl-Heusdain/smartcities/blob/main/AD-PWM/AD-PWM_1.0.py)

Joue une mélodie grâce au buzzer
- Les notes sont définies sur la 4eme octave dans des fonctions portant le nom de la note voulue
- Le volume du buzzer est géré par l'ADC0 qui est lu toutes les 1ms

[AD-PWM_2.0.py](https://github.com/hepl-Heusdain/smartcities/blob/main/AD-PWM/AD-PWM_2.0.py)

- *très* légère optimisation du code précédent

[AD-PWM_3.0.py](https://github.com/hepl-Heusdain/smartcities/blob/main/AD-PWM/AD-PWM_3.0.py)

- Réécritude des fonctions donnant les fréquences des notes
    - permet maintenant de choisir l'octave voulue pour chaque note
- ébauche non terminée du code permettant de changer de mélodie

## Rpi Pinout
![302113634-20d19fc4-b9c3-4903-9ec8-b62cda90aee3](https://github.com/user-attachments/assets/ce8e1dc2-699c-4c7a-8bf7-f8bdfdcd9692)

