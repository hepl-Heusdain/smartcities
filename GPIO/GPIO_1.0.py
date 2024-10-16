# GPIO version 1.0 
# Looping in a while without the use of interrupts

# code pas pratique, l'appui du bouton lors de l'exécution de sleep() est ignoré

import machine
import utime
LED = machine.Pin(16, machine.Pin.OUT)
BTN = machine.Pin(18, machine.Pin.IN)

while True:
    while BTN.value() == 0: 
        LED.value(0)
    while BTN.value() == 0:
        LED.toggle()
        utime.sleep(2)
    while BTN.value() == 0:
        LED.toggle()
        utime.sleep(1)