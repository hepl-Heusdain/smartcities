# AD-PWM version 2.0 

from machine import Pin, ADC, PWM, Timer
from time import sleep
Buzzer = PWM(Pin(27))
POT = ADC(0)

mute = 0

def timerInterruptCallback(erika):
    global mute
    if mute:
        Buzzer.duty_u16(0)
    else:
        val = POT.read_u16()
        Buzzer.duty_u16(int(val/25))
timer = Timer()
timer.init(mode=Timer.PERIODIC, period=1, callback=timerInterruptCallback)

def do():
    global mute
    mute = 0
    Buzzer.freq(1046) 
def re():
    global mute
    mute = 0
    Buzzer.freq(1175) 
def mi():
    global mute
    mute = 0
    Buzzer.freq(1318) 
def fa():
    global mute
    mute = 0
    Buzzer.freq(1397) 
def sol():
    global mute
    mute = 0
    Buzzer.freq(1568) 
def la():
    global mute
    mute = 0
    Buzzer.freq(1760) 
def si():
    global mute
    mute = 0
    Buzzer.freq(1967) 
def N():
    global mute
    mute = 1

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
    mute = 0
    Buzzer.freq(2093) 
    sleep(0.4)
    N()
    sleep(0.2)
    mute = 0
    Buzzer.freq(2093) 
    sleep(1)
    si()
    sleep(0.2)
    la()
    sleep(0.2)
    N()
    sleep(0.6)