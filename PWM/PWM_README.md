Les consignes exactes de cet exercice se trouvent dans ce PDF : [Exercice2.pdf](https://github.com/user-attachments/files/17187555/Exercice2.pdf)

Les différents modules sont connectés comme suit :
- Buzzer sur Pin27
- Potentiomètre sur ADC0

[PWM_1.0.py](https://github.com/hepl-Heusdain/smartcities/blob/main/PWM/PWM_1.0.py)

Joue une mélodie grâce au buzzer
- Les notes sont définies sur la 4eme octave dans des fonctions portant le nom de la note voulue
- Le volume du buzzer est géré par l'ADC0 qui est lu toutes les 1ms

[PWM_2.0.py](https://github.com/hepl-Heusdain/smartcities/blob/main/PWM/PWM_2.0.py)

- *très* légère optimisation du code précédent

[PWM_3.0.py](https://github.com/hepl-Heusdain/smartcities/blob/main/PWM/PWM_3.0.py)

- Réécritude des fonctions donnant les fréquences des notes
    - permet maintenant de choisir l'octave voulue pour chaque note
- ébauche non terminée du code permettant de changer de mélodie

![302113634-20d19fc4-b9c3-4903-9ec8-b62cda90aee3](https://github.com/user-attachments/assets/cceee934-d5e4-4459-bb2c-24b02900156c)
