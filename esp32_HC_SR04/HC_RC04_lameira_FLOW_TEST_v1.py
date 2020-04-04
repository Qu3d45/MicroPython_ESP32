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


################## TODO: Implementar um wakeup por botão quando esta em deepsleep, evita a tentativa erro de acordar o MCU  ##################


from machine import Pin, time_pulse_us, I2C, deepsleep
from time import sleep, sleep_us, ticks_ms, ticks_diff

import ssd1306


def str_to_int(lst):
    for i in range(0, len(lst)):
        lst[i] = int(lst[i])
    return lst


# Read from file
total_discharge_readings = []

with open("total_discharge.txt", mode='r') as total_discharge_file:
    for line in total_discharge_readings:
        total_discharge_readings.append(line.lstrip(
            'Last reading of total_discharge: ').rstrip('\n'))


rtc_start = 0
# sleep for 5 min (300000 miliseconds)
deepsleep_time = 10000  # 10 seconds

button = Pin(4, Pin.IN)

# ESP32 Pin assignment
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

temp_dht22 = 20
hum_dht22 = 30

# trig.value(0)  # Stabilize the sensor
# sleep_us(2)
trig.value(1)
sleep_us(10)
trig.value(0)

duration = time_pulse_us(echo, 1, timeout_us)

if duration < 0:
    oled.fill(0)
    oled.text('Out of range', 0, 20)
    oled.show()

else:
    # To calculate the distance we get the pulse_time and divide it by 2
    # (the pulse walk the distance twice)
    # the sound speed on air (343.2 m/s), that It's equivalent to
    # 0.034320 cm/us that is 1cm each 29.1us

    # Calculate the Speed of Sound in m/s

    oled.fill(0)

    sound_comp = (331.4 + (0.606 * temp_dht22) +
                  (0.0124 * hum_dht22))/10000

    # oled.text('Sound cm/us:', 0, 0)
    # oled.text(str(sound_comp), 0, 10)
    # verifica!

    distance = (duration / 2) * sound_comp

    # oled.text('distance cm:', 0, 20)
    # oled.text(str(distance), 0, 30)
    # verifica!

    water_hight = sensor_hight - distance
    # oled.text('water_hight cm:', 0, 0)
    # oled.text(str(water_hight), 0, 10)
    # verifica!

    water_hight_m = water_hight/100

    # Manning-Strickler
    discharge = (0.21579*(water_hight_m**(5/3))) / \
        (water_hight_m + 0.47918)**(2/3)
    # print(discharge, " m3/s")

    oled.text('m3/s: {}'.format(str(discharge)), 0, 20)

    #####----- RTC -----#####
    rtc_reading_now = ticks_ms()
    # print(rtc_reading_now)

    time_diff = ticks_diff(rtc_reading_now, rtc_start)
    # print(time_diff)

    total_discharge = (time_diff/1000) * discharge
    # print(total_discharge, 'm3')

    # Wirte to file
    # 'w' = write --> new file
    # 'a' = append
    # when "with" is used, no need to close the file
    with open("total_discharge.txt", mode='a') as file:
        file.write(
            'Last reading of total_discharge: {} \n'.format(total_discharge))

    oled.text('t_d m3: {}'.format(str(total_discharge)), 0, 30)

    conv_total_discharge_readings = str_to_int(total_discharge_readings)

    sum_total_discharge = sum(conv_total_discharge_readings) + total_discharge

    oled.text('acum_t_d m3: {}'.format(str(sum_total_discharge)), 0, 50)

    oled.show()

if button == True:
    oled.fill(0)
    oled.text('Waiting for resart', 0, 30)
    sleep(15)
else:
    deepsleep(deepsleep_time)
