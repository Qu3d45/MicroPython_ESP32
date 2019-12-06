# Manuel Lameira
# Licence under MIT
# code for ESP32 with MicroPython

# Interrupt Example with Micropython

# PIR --> ESP32
# -------------
# GND  --> GND
# DATA --> Digitalpin 14
# VCC  --> 3V3 or 5V


from machine import Pin
from time import time

# variables to keep track of what is going on
startTimer = False
motion = False
lastMotionTime = 0
delayInterval = 20


def handel_Interrupt(pin):
    global motion, lastMotionTime, startTimer
    motion = True
    startTimer = True
    lastMotionTime = time()


led = Pin(12, Pin.OUT)
pir = Pin(14, Pin.IN)

pir.irq(trigger=Pin.IRQ_RISING, handler=handel_Interrupt)

while True:
    if motion and startTimer:
        print('Motion detected!')
        led.value(1)
        startTimer = False
    elif motion and (time() - lastMotionTime) > delayInterval:
        print('Motion stopped!')
        led.value(0)
        motion = False
