# Manuel Lameira
# DTH 22 readings using MicroPython with I2C OLED Display

# DTH22 --> ESP32
# ---------------
# GND   --> GND
# VCC   --> 5v or 3.3v
# DAT   --> D14

# DS18X20 --> ESP32
# -----------------
# VCC --> 5V or 3.3V with resistor
# GND --> GND
# DAT --> digitalPin 15

from machine import Pin, I2C
from time import sleep, sleep_ms
from onewire import OneWire
from ds18x20 import DS18X20

import dht
import ssd1306

sensor = dht.DHT22(Pin(14))

ds_pin = Pin(15)
ds_sensor = DS18X20(OneWire(ds_pin))

addrs = ds_sensor.scan()
addr = addrs.pop()

# ESP32 Pin assignment 
i2c = I2C(-1, scl=Pin(4), sda=Pin(5)) # 5=SDK/SDA  4=SCK/SCL  As per labeling on ESP32 DevKi

# Define the OLED width and height
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)


while True:
  try:
    # fill(), to fill the screen in black (1) or white (0)
    oled.fill(0)
    
    # The DHT22 need 2s to get the readings
    sleep(2)
    
    sensor.measure()
    
    temp = sensor.temperature()
    temp_conv = str('%3.2f C  DHT22' %temp)
    
    hum = sensor.humidity()
    hum_conv = str('%3.2f %%' %hum)
    
    ds_read = ds_sensor.convert_temp()
    sleep_ms(750)
    temp_ds = ds_sensor.read_temp(addr)
    ds_reed_print = str('%3.2f C  DS18X20' %temp_ds)
    
    oled.text('Temperature: ', 0, 0)
    oled.text( temp_conv, 0, 10)
    oled.text( ds_reed_print, 0, 20)
    oled.text('Humidity: ', 0, 40)
    oled.text( hum_conv, 0, 50)
    
    oled.show()
    
  except OSError as e:
    oled.fill(0)
    oled.text('Failed to ', 0, 20)
    oled.text('read sensor!',0, 30)
    oled.show()

