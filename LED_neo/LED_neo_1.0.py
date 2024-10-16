# LED_neo_1.0.py

import neopixel
from machine import Pin, ADC, Timer
from utime import sleep, sleep_ms

black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 150, 0)
green = (0, 255, 0)
cyan = (0, 255, 255)
blue = (0, 0, 255)
purple = (180, 0, 255)
white = (255, 255, 255)

soundLevel = 0
sensitivity = 0

soundSensor = ADC(0)
POT = ADC(1)
p = Pin.board.GP18
n = neopixel.NeoPixel(p, 1)

while True:
    sensitivity = int(POT.read_u16()/256)
    average = 0
    for i in range (300):
        soundLevel = soundSensor.read_u16()/256
        average += soundLevel
    soundLevel = average/300
    if soundLevel-sensitivity < 5 :   n.fill(green)
    else :  n.fill(red)
    n.write()