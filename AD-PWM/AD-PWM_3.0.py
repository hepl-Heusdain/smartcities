# PWM version 3.0 
# Réécriture des fonctions déterminant la fréquence de chaque note
    # possibilité de choisir l'octave voulue
# ébauche du code permettant de changer de musique
    # Ne permet pas encore de directement transitionner lors de l'appui du bouton

from machine import Pin, ADC, PWM, Timer
from time import sleep, ticks_ms
BTN = Pin(18, Pin.IN, Pin.PULL_UP)
Buzzer = PWM(Pin(27))
POT = ADC(0)
timer = Timer()

mute = 0
debounce_time = 0
melodie = 0

def interruption_callback(BTN):
    global debounce_time, melodie
    if (ticks_ms()-debounce_time) > 500:
        if melodie == 0:
            melodie = 1
        else:
            melodie = 0
        debounce_time=ticks_ms()
BTN.irq(trigger=Pin.IRQ_FALLING, handler=interruption_callback)

def timerInterruptCallback(erika):
    global mute
    if mute:
        Buzzer.duty_u16(0)
    else:
        val = POT.read_u16()
        Buzzer.duty_u16(int(val/25))
timer.init(mode=Timer.PERIODIC, period=1, callback=timerInterruptCallback)

def c(octave):          # do
    global mute
    note = int((2**octave)*32.7)
    mute = 0
    Buzzer.freq(note) 
def d(octave):          # re
    global mute
    note = int((2**octave)*36.71)
    mute = 0
    Buzzer.freq(note) 
def e(octave):          # mi
    global mute
    note = int((2**octave)*41.2)
    mute = 0
    Buzzer.freq(note) 
def f(octave):          # fa
    global mute
    note = int((2**octave)*43.65)
    mute = 0
    Buzzer.freq(note) 
def g(octave):          # sol
    global mute
    note = int((2**octave)*49)
    mute = 0
    Buzzer.freq(note) 
def a(octave):          # la
    global mute
    note = int((2**octave)*55)
    mute = 0
    Buzzer.freq(note) 
def b(octave):          # si
    global mute
    note = int((2**octave)*61.74)
    mute = 0
    Buzzer.freq(note) 

def melodie_1():
    global mute
    sleep(0.5)
    c(4)
    sleep(1)
    d(4)
    sleep(0.2)
    e(4)
    sleep(0.4)
    mute = 1
    sleep(0.2)
    e(4)
    sleep(0.4)
    mute = 1
    sleep(0.2)
    e(4)
    sleep(0.6)
    a(4)
    sleep(0.4)
    mute = 1
    sleep(0.2)
    a(4)
    sleep(0.6)
    c(5) 
    sleep(0.4)
    mute = 1
    sleep(0.2)
    c(5)
    sleep(1)
    b(4)
    sleep(0.2)
    a(4)
    sleep(0.2)
    mute = 1

def melodie_2():
    global mute
    sleep(0.5)


while True:
    if melodie == 0:
        melodie_1()
    else :
        melodie_2()