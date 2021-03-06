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


while True:
  try:
    
    oled.fill(0)
    # The DHT22 need 2s to get the readings  
    sleep(2)
    sensor.measure()
    temp = sensor.temperature()
    temp_conv = str('%3.1f C' %temp)
    hum = sensor.humidity()
    hum_conv = str('%3.1f %%' %hum)
   
    
    oled.text('Temperature: ', 0, 0)
    oled.text( temp_conv, 0, 10)
    #oled.text( temp_f_conv, 0, 20)
    oled.text('Humidity: ', 0, 30)
    oled.text( hum_conv, 0, 40)
    
    oled.show()
        
    
  except OSError as e:
    #print('Failed to read sensor.')
    oled.fill(0)    
    oled.text('Failed to read sensor!', 0, 20)
    oled.show()

