# network_2.0.py

from machine import Pin
from Servo import SERVO
from time import sleep, localtime, ticks_ms
import network, ntptime

class timeMode(object) :
    H12_MODE = 1
    H24_MODE = 2

mode = timeMode.H12_MODE
debounce_time = 0

sta_if = network.WLAN(network.STA_IF)
servo = SERVO(Pin(26))
btn = Pin(18, Pin.IN, Pin.PULL_UP)


def interruption_callback(BTN):
    global debounce_time
    timeout = ticks_ms()
    print('enter interrupt')
    if (ticks_ms()-debounce_time) > 600:
        while (ticks_ms()-timeout) < 500:
            print('enter while')
            if btn.value() == 1:
                print('enter if')
                global mode
                if mode == timeMode.H24_MODE:
                    mode = timeMode.H12_MODE
                else :  
                    mode = timeMode.H24_MODE
        print('exit while')
        debounce_time = ticks_ms()


btn.irq(trigger=Pin.IRQ_FALLING, handler=interruption_callback)

if not sta_if.isconnected():
    print('connecting to network...')
    sta_if.active(True)
    sta_if.connect('NETGEAR95', 'kft4-i3al-c0si')
    while not sta_if.isconnected():
        pass

print('network config:', sta_if.ipconfig('addr4'))
ntptime.host = "1.be.pool.ntp.org"
print(ntptime.host)
print('Local time Before sync : ', localtime())
try:
    ntptime.settime()
    print('Sync OK')
except:
    print('Error while synchronizing time,\nPlease make sure internet connection is functional and reboot the Pico')
print('Local time After sync : ', localtime())

while True :
    localTime = localtime()
#    print(localTime)

    servoAngle = ((localTime[3]+2)*3600 + localTime[4]*60 + localTime[5])/(240*mode)
    if servoAngle > 180:
        servoAngle -= 180
#    print(servoAngle)

    servo.turn(servoAngle)

    