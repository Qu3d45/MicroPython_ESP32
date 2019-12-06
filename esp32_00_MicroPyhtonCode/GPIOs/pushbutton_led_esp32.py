
# Button:             ESP32:
# GND Add 10kOhm -->  GND + GPIO4
# VCC -->             3V3

# LED:                ESP32:
# GND add 330 Ohm --> GND
# VCC -->             GPIO5

from machine import Pin
from time import sleep

led = Pin(5, Pin.OUT)
button = Pin(4, Pin.IN)

while True:
    led.value(button.value())
    sleep(0.1)
