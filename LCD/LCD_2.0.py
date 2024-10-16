# I2C_2.0.py
# Lecture et affichage des valeurs Set & Ambient

from machine import I2C, Pin, ADC
from time import sleep_ms
from lcd1602 import LCD1602
from dht11 import *

POT = ADC(0)
dht = DHT(16)
i2c = I2C(1,scl=Pin(7), sda=Pin(6), freq=400000)
lcd = LCD1602(i2c, 2, 16)

lcd.display()
lcd.setCursor(0, 0)
lcd.print("Set : ")
lcd.setCursor(0, 1)
lcd.print("Ambient : ")

while True:
    lcd.setCursor(6, 0)
    Set = int(15 + 20*(POT.read_u16()/65000))
    lcd.print(str(Set))
    lcd.setCursor(10, 1)
    Ambient = dht.readTemperature()
    lcd.print(str(Ambient))
    sleep_ms(1000)