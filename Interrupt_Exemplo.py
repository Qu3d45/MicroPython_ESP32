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
from time import sleep

# This variable will indicate whether motion was detected or not
motion = False


def handel_Interrupt(pin):
    global motion
    motion = True
    global interrupt_pin
    interrupt_pin = pin


led = Pin(12, Pin.OUT)
pir = Pin(14, Pin.IN)

pir.irq(trigger=Pin.IRQ_RISING, handler=handel_Interrupt)

while True:
    if motion:
        print('Motion detected! Interrupt caused by: {}'.format(interrupt_pin))
        led.value(1)
        sleep(20)
        led.value(0)
        print('Motion stopped!')
        motion = False
