# I2C_1.0.py 
# Affichage de la valeur d'un ADC sur 16bits

from machine import I2C, Pin, ADC
from time import sleep
from lcd1602 import LCD1602

POT = ADC(0)
i2c = I2C(1,scl=Pin(7), sda=Pin(6), freq=400000)
d = LCD1602(i2c, 2, 16)
d.display()
sleep(1)

while True:
    d.clear()
    d.setCursor(0, 0)
    d.print(str(POT.read_u16()))
    sleep(1)