# Projet SmartCities
## Description
Dans le cadre du cours "Smartcities & IoT", nous sommes amenés à réalier des projets uilisant un Raspberry Pi Pico W programmé en MicroPython. Ce cours a donc pour but de nous introduire au langage grâce à un kit grove de base.

Le détail de chaque version des codes de ce projet est fourni à la fois dans le README propre à chaque exercice ainsi que dans les en-têtes des codes en eux mêmes.

## Répertoires
- [GPIO](https://github.com/hepl-Heusdain/smartcities/blob/main/GPIO/GPIO_README.md)
- [AD-PWM](https://github.com/hepl-Heusdain/smartcities/blob/main/AD-PWM/AD-PWM_README.md)
- [LCD](https://github.com/hepl-Heusdain/smartcities/blob/main/LCD/LCD_README.md)
- [LED_neo](https://github.com/hepl-Heusdain/smartcities/blob/main/LED_neo/LED_neo_README.md)
- [network](https://github.com/hepl-Heusdain/smartcities/blob/main/network/network_README.md)

## Raspberry Pi Pico W
Le raspberry Pi Pico W offre les mêmes performances que le Rasperry Pi Pico classique en plus d'offrir une connectivité WiFi/Bluetooth supplémentaire.
Les caractéristiques les plus notables de ce microcontrôleur sont les suivantes :
- 2MB de mémoir Flash
- Dual core Cortex M0+ offrant une fréquence d'horloge jusqu'à 133MHz
- 264kB SRAM
- ADC 12-bit 500ksps
- 2x UART, 2x I2C, 2x SPI, 16x PWM
- Fonctionne sous 3.3V
- L'entièreté des GPIO peuvent êtres programmés en tant qu'interuption externe

### Pinout
![302113634-20d19fc4-b9c3-4903-9ec8-b62cda90aee3](https://github.com/user-attachments/assets/7db5d3e3-2b80-4f3e-994b-bcd2d8b20a01)

## MicroPython
MicroPython est un portage du langage Python sur micro-contrôleurs. Voici une vue d'ensemble de la structure de Micropython comprenant :
- Le portage complet des mots-clés, des objets Python et des fonctions built-in
- Le portage d'une vingtaine de modules standards dans un format allégé et finalement adapté au contexte du microcontrôleur, mais avec à chaque fois les fonctions essentielles. Notamment, les modules re (expressions régulières), time, sys, os, io, math sont portés en Micropython
- Des modules spécifiques Micropython qui rassemblent les classes et fonctions communes dans le cadre d'une utilisation sur base microcontrôleur
- Des modues dédiés par plateforme, fournissant les classes et fonctions spécifiques à une carte précise
- Des modules "librairies" enfin qui fournissent les fonctionnalités matérielles utiles pour l'utilisation de cartes, capteurs, modules dédiés dans un contexte micro-contrôleur.


