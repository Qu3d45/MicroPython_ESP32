# Manuel Lameira
# Board: ESP32 - WROOM or WROVER

# This is a micropython convertion for the code provided by DFRobot.com for the arduino platform.
# Please see the website for more information:
# https://wiki.dfrobot.com/Gravity__Analog_TDS_Sensor___Meter_For_Arduino_SKU__SEN0244

# For the temperature compensation is used the DFRobot_PH.py library from DFRobot.com
# Original: https://github.com/DFRobot/DFRobot_PH/blob/master/RaspberryPi/Python/DFRobot_PH.py

# For connection to an ESP32 board we do not need a voltage divider,
# the transmitter Board has an MAX OUTPUT VOLTAGE of 2.3V

# ESP32 --> 12 bit ADC --> 4095 samples at 3.3V
# ADC Pin; 0, 2, 4, 12, 13, 14, 15, 25, 26, 27, 32, 33, 34, 35, 36, 39

# TDS --> ESP32
# --------------------
# VCC --> 5.5V or 3.3V
# A   --> Analog Pin
# GND --> GND


from machine import Pin, ADC
from time import sleep
from math import floor


def Average(lst):
    # function to get average of a list
    return sum(lst) / len(lst)


def ReadTDS(voltage, temp):
    # Temperature compensation to 25 °C reference value
    comp_Coefficente = 1 + 0.02 * (temp - 25)

    # compensated electrical conductivity
    comp_Voltage = voltage / comp_Coefficente

    # convert voltage value to tds value
    tds_value = ((133.42 * comp_Voltage**3) - (255.86 *
                                               comp_Voltage**2) + (857.39 * comp_Voltage)) * 0.5

    return tds_value


# Pin definition and ADC initialization
tds = ADC(Pin(34))
tds.atten(ADC.ATTN_11DB)  # Reading range: 3.3V

# DS18B20 temperatur
ds18_temp = 25


# Creat empty list for value storage
buf = []
sample = range(5)

for i in sample:
    buf.append(tds.read())
    sleep(1)
    print(buf)

avgValue = Average(buf)

print(avgValue)

tdsVoltage = (avgValue * (3.3/4095))  # read the voltage in mV

print(tdsVoltage)

tdsValue = round(ReadTDS(tdsVoltage, ds18_temp), 3)

print(tdsValue, " ppm")

ecValue = round((tdsValue / 640), 3)  # conversion factor ppm to dS/m

print(ecValue, " dS/m")
