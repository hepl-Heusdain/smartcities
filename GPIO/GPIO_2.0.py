# GPIO version 2.0 

# utilisation de l'interruption pour changer la vitesse de clignottement de la LED
# Point à amméliorer : utiliser un timer pour faire clignotter la LED

from machine import Pin
import time
LED = Pin(16, Pin.OUT)
BTN = Pin(18, Pin.IN, Pin.PULL_UP)

ledSpeed = 0
debounce_time = 0

def interruption_callback(BTN):
    global debounce_time, ledSpeed
    if (time.ticks_ms()-debounce_time) > 500:
        ledSpeed = ledSpeed + 1
        if ledSpeed == 3:
            ledSpeed = 0
            LED.value(0)
        debounce_time=time.ticks_ms()

BTN.irq(trigger=Pin.IRQ_FALLING, handler=interruption_callback)

while True:
    while ledSpeed > 0:
        LED.toggle()
        time.sleep(2/ledSpeed)