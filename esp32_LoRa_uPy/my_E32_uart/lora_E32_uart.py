# Manuel Lameira
# Board: ESP32 - WROOM or WROVER

# This is a micropython convertion for the code provided by DFRobot.com for the arduino platform.
# Please see the website for more information:
# https://wiki.dfrobot.com/Gravity__Analog_TDS_Sensor___Meter_For_Arduino_SKU__SEN0244

# For the temperatur compensation i used the DFRobot_PH.py library from DFRobot.com
# Original: https://github.com/DFRobot/DFRobot_PH/blob/master/RaspberryPi/Python/DFRobot_PH.py

# For connection to an ESP32 board we do not need a voltage divider, 
# the transmitter Board has an MAX OUTPUT VOLTAGE of 2.3V

# ESP32 --> 12 bit ADC --> 4095 samples at 3.3V
# ADC Pin; 0, 2, 4, 12, 13, 14, 15, 25, 26, 27, 32, 33, 34, 35, 36, 39

# E32 LoRa --> ESP32
# --------------------
# VCC --> 5.5V or 3.3V
# GND --> GND
# AUX --> State Indication
# TXD --> UART - RX
# RXD --> UART - TX
# M1  --> Config Mode
# M2  --> Config Mode
#
