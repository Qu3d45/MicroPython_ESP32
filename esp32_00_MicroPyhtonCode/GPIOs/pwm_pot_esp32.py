
# POT:        ESP32:
# GND -->     GND
# Signal -->  GPIO34
# VCC -->     3V3

# LED:                ESP32:
# GND add 330 Ohm --> GND
# VCC -->             GPIO5

from machine import Pin, PWM, ADC
from time import sleep

frequency = 5000
led = PWM(Pin(5), frequency)
pot = ADC(Pin(34))
pot.width(ADC.WIDTH_10BIT)
pot.atten(ADC.ATTN_11DB)

while True:
    pot_value = pot.read()
    print(pot_value)

    if pot_value < 15:
        led.duty(0)
    else:
        led.duty(pot_value)

    sleep(0.1)
