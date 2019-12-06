# Manuel Lameira
# Board: ESP32 - WROOM or WROVER

# This is a micropython convertion for the code provided by diymore.cc for the arduino platform.
# Please see the website for more information:
# https://www.diymore.cc/products/diymore-liquid-ph-value-detection-detect-sensor-module-monitoring-control-for-arduino-m?_pos=1&_sid=4a08bbc6e&_ss=r

# For the temperatur compensation i used the DFRobot_PH.py library from DFRobot.com
# Original: https://github.com/DFRobot/DFRobot_PH/blob/master/RaspberryPi/Python/DFRobot_PH.py

# For connection to an ESP32 board a voltage divider with R1 = 10kOhm and R2 = 20kOhm
# in between pin PO (PH4502) and analog input (ESP32) is required.

# ESP32 --> 12 bit ADC --> 4095 samples at 3.3V
# ADC Pin; 0, 2, 4, 12, 13, 14, 15, 25, 26, 27, 32, 33, 34, 35, 36, 39


from machine import Pin, ADC
from time import sleep


def Average(lst):
    # function to get average of a list
    return sum(lst) / len(lst)


def ReadPH(voltage, temp):
    # Calibration of probe
    # PH4502 with 5V --> pH 4 acidVoltage = 1.432V and pH 7 (pot calibration) neutralVoltage = 2.5V 
    # with voltage divider --> pH 4 = 0.944V and pH 7 = 1.652V
    acidVoltage = 0.9440
    neutralVoltage = 1.6520
    
    if temp >= 25:
        temp_correction = 0.003 * (temp - 25)
    else:
        temp_correction = -0.003 * (temp - 25)
    
    slope = (7.0 - 4.0) / (- (acidVoltage - neutralVoltage) / 3.0)
    intercept = 7.0 - slope * (neutralVoltage - neutralVoltage) / 3.0
    phValue  = (slope * (voltage - neutralVoltage) / 3.0 + intercept) + temp_correction
    
    round(phValue,2)
    return phValue

# Pin definition and ADC initialization
pH = ADC(Pin(34))
pH.atten(ADC.ATTN_11DB)  # Reading range: 3.3V

# DS18B20 temperatur
ds18_temp = 25


# Creat empty list for value storage
buf = []
sample = range(10)

for i in sample:
    buf.append(pH.read())
    sleep(2)
    print(buf)

avgValue = Average(buf)

print(avgValue)

phVoltage = (avgValue / (4095/3.3))

print(phVoltage)

pH_final = ReadPH(phVoltage, ds18_temp)

print(pH_final)