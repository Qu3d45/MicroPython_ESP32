# Manuel Lameira
# Board: ESP32 - WROOM or WROVER

# This is a micropython convertion for the code provided by https://dronebotworkshop.com for the arduino platform.
# Please see the website for more information:
# https://dronebotworkshop.com/hc-sr04-ultrasonic-distance-sensor-arduino/#1

# SR04  --> ESP32
# --------------------
# VCC   --> 5V or 3.3V ATENCION: on 3.3V the range decresses
# Trig  --> DigitalPin 17
# Echo  --> DigitalPin 16
# GND   --> GND

# Speed of Sound = 343 m/s in dry air at 20ºC

from machine import Pin, time_pulse_us
from time import sleep, sleep_us

trig = Pin(17, Pin.OUT)
echo = Pin(16, Pin.IN)

timeout_us = 25000  # no need to wait more then sensor's range limit (4,00 m)

sensor_hight = 1, 50

while True:
    temp = 25
    hum = 50

    # trig.value(0)  # Stabilize the sensor
    # sleep_us(2)
    trig.value(1)
    sleep_us(10)
    trig.value(0)

    duration = time_pulse_us(echo, 1, timeout_us)

    if duration < 0:
        print("Out of range")
    else:
        # To calculate the distance we get the pulse_time and divide it by 2
        # (the pulse walk the distance twice)
        # the sound speed on air (343.2 m/s), that It's equivalent to
        # 0.034320 cm/us that is 1cm each 29.1us

        # Calculate the Speed of Sound in M/S
        sound_comp = 331.4 + (0.606 * temp) + (0.0124 * hum)

        distance = (duration / 2) * 0.000343
        print(distance, " m")

        water_hight = sensor_hight - distance
        print(water_hight, " m")

        discharge = (0.209763317*(water_hight**(5/3))) / \
            ((water_hight + 0.918486862)**(2/3))
        print(discharge, " m3/s")

    sleep(2)
