# Manuel Lameira

# This is a micropython convertion for the code provided by diymore.cc for the arduino platform.
# Please see the website for more information:
# https://www.diymore.cc/products/diymore-liquid-ph-value-detection-detect-sensor-module-monitoring-control-for-arduino-m?_pos=1&_sid=4a08bbc6e&_ss=r

# For the temperatur compensation i have used uFire_pH.py library
# Original: https://github.com/u-fire/Isolated_ISE/blob/master/python/RaspberryPi/uFire_pH.py

# For connection to an ESP32 board a voltage divider with R1 10kOhm and R2 20kOhm
# on the PO pin and analog input is required.

# ESP32 --> 12 bit ADC --> 4095 samples at 3.3V
# ADC Pin; 0, 2, 4, 12, 13, 14, 15, 25, 26, 27, 32, 33, 34, 35, 36, 39


from machine import Pin, ADC
from time import sleep
from math import floor

# function to get average of a list


def Average(lst):
    return sum(lst) / len(lst)


def TempCorrection(phValue, temp):
    # temp_correction_factor = 0.03

    distance_from_7 = abs(7 - round(phValue))
    distance_from_25 = floor(abs(25 - round(temp)) / 10)
    temp_multiplier = (distance_from_25 * distance_from_7) * \
        temp_correction_factor
    if (phValue >= 8.0) and (temp >= 35):
        temp_multiplier *= -1
    if (phValue <= 6.0) and (temp <= 15):
        temp_multiplier *= -1
    phValue += temp_multiplier
    return phValue


# Pin definition and ADC initialization
pH = ADC(Pin(34))

pH.atten(ADC.ATTN_11DB)  # Reading range: 3.3V

temp = 25

# Creat empty list for value storage
buf = []
sample = range(10)

for i in sample:
    buf.append(pH.read())
    sleep(2)
    print(buf)

avgValue = Average(buf)

print(avgValue)

phValue = 3.5 * (avgValue * (5/4095))

print(phValue)

pH_final = TempCorrection(phValue, temp)

print(pH_final)
