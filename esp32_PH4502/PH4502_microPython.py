# Manuel Lameira

# This is a micropython adaptation of the code provided by diymore.cc for the arduino platform.
# Please see the website for more information:
# https://www.diymore.cc/products/diymore-liquid-ph-value-detection-detect-sensor-module-monitoring-control-for-arduino-m?_pos=1&_sid=4a08bbc6e&_ss=r

# For connection to an ESP32 board a voltage divider with R1 10kOhm and R2 20kOhm
# on the PO pin and analog input is required.

# ESP32 --> 12 bit ADC --> 4095 samples at 3.3V
# ADC Pin; 0, 2, 4, 12, 13, 14, 15, 25, 26, 27, 32, 33, 34, 35, 36, 39


from machine import Pin, ADC
from time import sleep

# function to get average of a list


def Average(lst):
    return sum(lst) / len(lst)


# Pin definition and ADC initialization
pH = ADC(Pin(34))
pH.atten(ADC.ATTN_11DB)  # Reading range: 3.3V

# Creat empty list for value storage
buf = []
sample = range(10)

for i in sample:
    buf.append(pH.read())
    sleep(1)
    print(buf)

avgValue = Average(buf)

print(avgValue)

phValue = 3.5 * (avgValue * (5/4095))

print(phValue)
