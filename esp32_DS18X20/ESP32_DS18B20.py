# Manuel Lameira
# Board: ESP32 - WROOM or WROVER

# DS18B20 using MicroPython


# DS18B20 --> ESP32
# GND     --> GND
# VCC     --> 5v or 3.3v
# DAT     --> D4


from machine import Pin
from time import sleep_ms
from onewire import OneWire
from ds18x20 import DS18X20


ds18_sensor = DS18X20(OneWire(Pin(4)))

addrs = ds18_sensor.scan()
addr = addrs.pop()

while True:
    ds18_read = ds18_sensor.convert_temp()
    sleep_ms(750)
    ds18_temp = ds18_sensor.read_temp(addr)
    print(str('%3.2f C' % ds18_temp))
