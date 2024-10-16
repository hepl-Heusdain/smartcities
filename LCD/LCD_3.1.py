# I2C_3.1.py
# "ALARM" clignotte sur l'écran

from machine import I2C, Pin, ADC, Timer, PWM
from time import sleep_ms
from lcd1602 import LCD1602
from dht11 import *

POT = ADC(0)
dht = DHT(16)
Buzzer = PWM(Pin(20))
LED = Pin(18, Pin.OUT)
i2c = I2C(1,scl=Pin(7), sda=Pin(6), freq=400000)
lcd = LCD1602(i2c, 2, 16)
timer = Timer()

tDelta = 0

def timerInterruptCallback(timer):
    global tDelta
    Set = int(15 + 20*(POT.read_u16()/65000))
    Ambient = dht.readTemperature()
    tDelta = Ambient - Set
    if tDelta <= 3:
        lcd.setCursor(0, 0)
        lcd.print("Set : " + str(Set))
        lcd.setCursor(0, 1)
        lcd.print("Ambient : " + str(Ambient))
    
timer.init(mode=Timer.PERIODIC, period=200, callback=timerInterruptCallback)

lcd.display()
Buzzer.duty_u16(0)
Buzzer.freq(1000)

while True:
    if tDelta > 3:
        Buzzer.duty_u16(1000)
        lcd.clear()
        lcd.print("ALARM")
        LED.toggle()
        sleep_ms(250)
        lcd.clear()
        LED.toggle()
        sleep_ms(250)
    elif tDelta > 0:
        LED.toggle()
        Buzzer.duty_u16(0)
        sleep_ms(500)
    else:
        LED.low()
        Buzzer.duty_u16(0)