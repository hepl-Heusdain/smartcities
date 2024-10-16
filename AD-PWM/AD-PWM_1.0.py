# AD-PWM version 1.0 

from machine import Pin, ADC, PWM, Timer
from time import sleep
Buzzer = PWM(Pin(27))
POT = ADC(0)
Buzzer.freq(500)
Buzzer.duty_u16(0)

mute = False

def timerInterruptCallback(erika):
    global mute
    if mute == True:
        Buzzer.duty_u16(0)
    else:
        val = POT.read_u16()
        Buzzer.duty_u16(int(val/25))
timer = Timer()
timer.init(mode=Timer.PERIODIC, period=1, callback=timerInterruptCallback)

def do():
    mute = False
    Buzzer.freq(1046) 
def re():
    mute = False
    Buzzer.freq(1175) 
def mi():
    mute = False
    Buzzer.freq(1318) 
def fa():
    mute = False
    Buzzer.freq(1397) 
def sol():
    mute = False
    Buzzer.freq(1568) 
def la():
    mute = False
    Buzzer.freq(1760) 
def si():
    mute = False
    Buzzer.freq(1967) 
def N():
    mute = True

while True:
    do()
    sleep(1)
    re()
    sleep(0.2)
    mi()
    sleep(0.4)
    N()
    sleep(0.2)
    mi()
    sleep(0.4)
    N()
    sleep(0.2)
    mi()
    sleep(0.6)
    la()
    sleep(0.4)
    N()
    sleep(0.2)
    la()
    sleep(0.6)
    mute = False
    Buzzer.freq(2093) 
    Buzzer.duty_u16(POT.read_u16())
    sleep(0.4)
    N()
    sleep(0.2)
    mute = False
    Buzzer.freq(2093) 
    Buzzer.duty_u16(POT.read_u16())
    sleep(1)
    si()
    sleep(0.2)
    la()
    sleep(0.2)
    N()
    sleep(0.6)