# LED:                ESP32:
# GND add 330 Ohm --> GND
# VCC -->             GPIO5

from machine import Pin, PWM
from time import sleep

frequency = 5000
led = PWM(Pin(5), frequency)

while True:
    for duty_cycle in range(0, 1024):
        led.duty(duty_cycle)
        sleep(0.005)
