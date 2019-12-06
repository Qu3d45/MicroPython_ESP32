# Manuel Lameira
# DTH 22 readings using MicroPython

# DTH22 --> ESP32
# GND   --> GND
# VCC   --> 5v or 3.3v
# DAT   --> D14

from machine import Pin, I2C
from time import sleep
import dht
import ssd1306

sensor = dht.DHT22(Pin(14))
#sensor = dht.DHT11(Pin(14))

# ESP32 Pin assignment 
i2c = I2C(-1, scl=Pin(4), sda=Pin(5)) # 5=SDK/SDA  4=SCK/SCL  As per labeling on ESP32 DevKi

# Define the OLED width and height
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)


for i in range(0,10):
  try:
    # The DHT22 need 2s to get the readings  
    sleep(2)
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    # uncomment if you need temp in Fahrenheit
    # temp_f = temp * (9/5) + 32.0
    #print('Temperature: %3.1f C' %temp)
    # print('Temperature: %3.1f F' %temp_f)
    #print('Humidity: %3.1f %%' %hum)
    
    oled.text('Temperature: ', 0, 0)
    oled.text('Hello, World 2!', 0, 10)
    oled.text('Humidity:', 0, 20)
    oled.text('Hello, World 4!', 0, 30)
    oled.text('Hello, World 5!', 0, 40)
    
    oled.show()
        
    i +=i
  except OSError as e:
    #print('Failed to read sensor.')
    
    oled.text('Failed to read sensor!', 0, 20)
    oled.show()

