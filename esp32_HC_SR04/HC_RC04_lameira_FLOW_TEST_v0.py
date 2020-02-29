# Manuel Lameira
# Board: ESP32 - WROOM or WROVER

# This is a micropython convertion for the code provided by https://dronebotworkshop.com for the arduino platform.
# Please see the website for more information:
# https://dronebotworkshop.com/hc-sr04-ultrasonic-distance-sensor-arduino/#1

# SR04  --> ESP32
# --------------------
# VCC   --> 5V or 3.3V ATENCION: on 3.3V the range decresses
# Trig  --> DigitalPin 13
# Echo  --> DigitalPin 12
# GND   --> GND

# Speed of Sound = 343 m/s in dry air at 20ºC

from machine import Pin, time_pulse_us, I2C
from time import sleep, sleep_us, ticks_ms, ticks_diff

import ssd1306

rtc_start = 0


# 21=SDK/SDA  22=SCK/SCL  As per labeling on ESP32 WROOM
i2c = I2C(1, scl=Pin(22), sda=Pin(21), freq=400000)

# Define the OLED width and height
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)


trig = Pin(13, Pin.OUT)
echo = Pin(12, Pin.IN)

timeout_us = 25000  # no need to wait more then sensor's range limit (4,00 m)

sensor_hight = 150  # in centimeters

while True:

    temp_dht22 = 20
    hum_dht22 = 30

    trig.value(1)
    sleep_us(10)
    trig.value(0)

    duration = time_pulse_us(echo, 1, timeout_us)

    if duration < 0:
        oled.fill(0)
        oled.text('Out of range', 0, 20)
        oled.show()

    else:
        oled.fill(0)

        sound_comp = (331.4 + (0.606 * temp_dht22) +
                      (0.0124 * hum_dht22))/10000

        #oled.text('Sound cm/us:', 0, 0)
        #oled.text(str(sound_comp), 0, 10)
        # verifica!

        distance = (duration / 2) * sound_comp

        #oled.text('distance cm:', 0, 20)
        #oled.text(str(distance), 0, 30)
        # verifica!

        water_hight = sensor_hight - distance
        oled.text('water_hight cm:', 0, 0)
        oled.text(str(water_hight), 0, 10)
        # verifica!

        discharge = (0.209763317*(water_hight**(5/3))) / \
            ((water_hight + 0.918486862)**(2/3))
        # print(discharge, " m3/s")

        oled.text('m3/s: {}'.format(str(discharge)), 0, 30)

        #####----- RTC -----#####
        rtc_reading_now = ticks_ms()
        # print(rtc_reading_now)

        time_diff = ticks_diff(rtc_reading_now, rtc_start)
        # print(time_diff)

        total_discharge = (time_diff/1000) * discharge
        # print(total_discharge, 'm3')

        oled.text('t_d m3: {}'.format(str(total_discharge)), 0, 50)

        oled.show()
