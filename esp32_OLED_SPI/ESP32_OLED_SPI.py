
# OLED:     ESP32:
# GND  -->  GND
# VDD  -->  3V3
# CLK  -->  GIPO18 (SCK)    Clock
# MOSI -->  GIPO19 (MISO)   Master in Slave out
# RES  -->  GIPO16 (normal) Reset
# DC   -->  GIPO17 (normal) Data Select
# CS   -->  GIPO5  (SS)     Chip Select


from machine import Pin, SPI
from time import sleep

import ssd1306


# ESP32 Pin assignment
#i2c = I2C(-1, scl=Pin(22), sda=Pin(21))

# ESP8266 Pin assignment
#i2c = I2C(-1, scl=Pin(5), sda=Pin(4))

# ESP32 SPI initalization 
hspi = SPI(2, baudrate=8000000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(23), miso=Pin(19))

#oled_width = 128
#oled_height = 64
oled = ssd1306.SSD1306_SPI(128, 64, hspi, dc=Pin(17), res=Pin(16), cs=Pin(5))

# class SSD1306_SPI(SSD1306):
#     def __init__(self, width, height, spi, dc, res, cs, external_vcc=False):

oled.text('Hello, World 1!', 0, 0)
oled.text('Hello, World 2!', 0, 10)
oled.text('Hello, World 3!', 0, 20)
oled.text('Hello, World 4!', 0, 30)
oled.text('Hello, World 5!', 0, 40)

oled.show()
