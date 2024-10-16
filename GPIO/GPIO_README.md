## Description
Il nous est demandé d'écrire un code permettant de faire clignotter une LED à des fréquences différentes lorque l'on appuie sur un bouton poussoir.
Les consignes exactes de cet exercice se trouvent dans ce PDF : 
[Exercice1.pdf](https://github.com/user-attachments/files/17187539/Exercice1.pdf)

Les différents modules sont connectés comme suit :
- LED sur Pin16
- Bouton sur Pin18

## Versions
[GPIO_1.0.py](https://github.com/hepl-Heusdain/smartcities/blob/main/GPIO/GPIO_1.0.py)

Transitionne entre les différentes fréquences par l'appui du bouton poussoir (code sans interruption)

[GPIO_2.0.py](https://github.com/hepl-Heusdain/smartcities/blob/main/GPIO/GPIO_2.0.py)

Utilise une interruption pour changer la fréquence de clignottement de la LED lors de l'appui du bouton

## Rpi Pinout
![302113634-20d19fc4-b9c3-4903-9ec8-b62cda90aee3](https://github.com/user-attachments/assets/196273cf-91a6-4708-b48f-fdd046db09e6)
