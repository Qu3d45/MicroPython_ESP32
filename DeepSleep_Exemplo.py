# Manuel Lameira
# Licence under MIT
# code for ESP32 with MicroPython

# DeepSleep Example with Micropython
# the ESP32 is in deep sleep mode for 10 seconds, then it
# wakes up, blinks an LED, and goes back to sleep

from machine import deepsleep, Pin
from time import sleep

led = Pin(2, Pin.OUT)

# blink LED
led.value(1)
sleep(1)
led.value(0)
# wait 5 seconds so that we catch the ESP awake
sleep(5)


print('The LED was on, now going back to sleep...')

# sleep for 10 seconds (10000 miliseconds)
deepsleep(10000)
