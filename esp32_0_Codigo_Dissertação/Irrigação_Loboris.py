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

from machine import Pin, I2C, time_pulse_us, Onewire, DHT, ADC
from time import sleep, sleep_ms, sleep_us
#from onewire import OneWire
#from ds18x20 import DS18X20

#import dht

def ReadDS18(ds18_sensor):
    
    temp = ds18_sensor.convert_read()
#    print("Temperature: {0:.1f}°C".format(temp))
#    sleep(4)
    return temp
   

def ReadFLOW(trig, echo):

    pass

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


def ReadTDS(voltage, temp):
    # Temperature compensation to 25 °C reference value
    comp_Coefficente = 1 + 0.02 * (temp - 25)
    
    # compensated electrical conductivity
    comp_Voltage = voltage / comp_Coefficente
    
    # convert voltage value to tds value
    tds_value = ((133.42 * comp_Voltage**3) - (255.86 * comp_Voltage**2) + (857.39 * comp_Voltage)) * 0.5
    
    return tds_value


#####----- DS18X20 LOBORIS-----#####
ds18_pin = Onewire(15)
ds18_sensor = Onewire.ds18x20(ds18_pin, 0)

ds18_temp = ReadDS18(ds18_sensor)

#addrs = ds18_sensor.scan()
#addr = addrs.pop()

#ds_read = ds18_sensor.convert_temp()
#sleep_ms(750)
#ds18_temp = ds18_sensor.read_temp(addr)

print("Temperature: {0:.1f}°C".format(ds18_temp))

#####----- ph -----#####
pH = ADC(34)
pH.atten(ADC.ATTN_11DB)  # Reading range: 3.3V

# Creat empty list for value storage
buf_ph = []
sample_ph = range(10)

for i in sample_ph:
    buf_ph.append(pH.read())
    sleep(1)

avgValue_ph = Average(buf_ph)
phVoltage = (avgValue_ph / (4095/3.3))

pH_final = round(ReadPH(phVoltage, ds18_temp),1)

print(pH_final, "ph")

#####----- TDS -----#####

# Pin definition and ADC initialization
tds = ADC(35)
tds.atten(ADC.ATTN_11DB)  # Reading range: 3.3V

# Creat empty list for value storage
buf_tds = []
sample_tds = range(5)

for i in sample_tds:
    buf_tds.append(tds.read())
    sleep(1)
    
avgValue_tds = Average(buf_tds)
tdsVoltage = (avgValue_tds * (3.3/4095)) # read the voltage in mV

tdsValue = round(ReadTDS(tdsVoltage, ds18_temp), 3)
ecValue = round((tdsValue / 640), 3) # conversion factor ppm to dS/m


print(ecValue, " dS/m")
print(tdsValue, " ppm")

#####----- DHT22 -----#####
dht_sensor = DHT(14, DHT.DHT2X)

result, temperature, humidity = dht_sensor.read()

x = result
temp_dht22 = float(temperature)
hum_dht22 = int(humidity)

print(temp_dht22, " ºC")

print(hum_dht22, " %")


#####----- Water flow HC-SR04 -----#####

trig = Pin(4, Pin.OUT)
echo = Pin(2, Pin.IN)

timeout_us = 25000  # no need to wait more then sensor's range limit (4,00 m)

sensor_hight = 150 # cm

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
    sound_comp = 331.4 + (0.606 * temp_dht22) + (0.0124 * hum_dht22)
#    print(sound_comp, " sound_comp")
        
    distance = (duration / 2) * (sound_comp/1000000) # m/us 
#    print(distance, " distance")
       
    water_hight = sensor_hight - distance #m
#    print(water_hight, " water_hight2")
        
       
    discharge = (0.209763317*(water_hight**(5/3)))/((water_hight + 0.918486862)**(2/3))
    print(discharge, " m3/s")







