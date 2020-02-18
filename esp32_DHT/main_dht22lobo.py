# Manuel Lameira
# Licence under MIT
# code for ESP32 with MicroPython Loboris

# For ADC1 only GPIOs 32-39 can be used as ADC inputs.
# For ADC2 gpios 4, 0, 2, 15, 13, 12, 14, 27, 25, 26 can be used as ADC inputs.

# DTH22 --> ESP32
# ---------------
# GND   --> GND
# VCC   --> 5v or 3.3v
# DAT   --> digitalPin 14

# DS18X20 --> ESP32
# -----------------
# VCC --> 5V or 3.3V with resistor
# GND --> GND
# DAT --> digitalPin 15

# ph  --> ESP32
# -----------------
# VCC --> 5V or 3.3V with resistor
# GND --> GND
# DAT --> digitalPin 34

# TDS --> ESP32
# --------------------
# VCC --> 5.5V or 3.3V
# A   --> Analog Pin 35
# GND --> GND

# SR04  --> ESP32
# --------------------
# VCC   --> 5V or 3.3V ATENCION: on 3.3V the range decresses
# Trig  --> DigitalPin 4
# Echo  --> DigitalPin 2
# GND   --> GND
# Speed of Sound = 343 m/s in dry air at 20ºC

from machine import Pin, I2C, time_pulse_us, Onewire, DHT, ADC, deepsleep
from time import sleep, sleep_ms, sleep_us

#from onewire import OneWire
#from ds18x20 import DS18X20

#import dht
# Channel ID 902540
# KEY IL9VIMCHEXM9H3W4
# GET https://api.thingspeak.com/update?api_key=IL9VIMCHEXM9H3W4&field1=0

# Channel ID 985682
# KEY 2IDFEOWYZCNDP7YW
# GET https://api.thingspeak.com/update?api_key=2IDFEOWYZCNDP7YW&field1=0



#####----- DHT22 -----#####
dht_sensor = DHT(19, DHT.DHT2X)

result, temperature, humidity = dht_sensor.read()
print(dht_sensor.read())
x = result
temp_dht22 = float(temperature)
hum_dht22 = int(humidity)

print(temp_dht22, " ºC")

print(hum_dht22, " %")
