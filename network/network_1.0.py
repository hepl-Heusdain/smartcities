# network_1.0.py

from machine import Pin
from Servo import SERVO
from time import sleep, localtime, ticks_ms
import network, ntptime

sta_if = network.WLAN(network.STA_IF)
servo = SERVO(Pin(26))

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

    servoAngle = ((localTime[3]+2)*3600 + localTime[4]*60 + localTime[5])/240
    if servoAngle > 180:
        servoAngle -= 180
#    print(servoAngle)

    servo.turn(servoAngle)

    