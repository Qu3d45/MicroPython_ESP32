# Manuel Lameira
# MicroPython I2C OLED Display with internal RTC

from machine import Pin, I2C

import ssd1306

# ESP32 Pin assignment 
i2c = I2C(1, scl=Pin(15), sda=Pin(4), freq=400000) # 4=SDK/SDA  15=SCK/SCL  As per labeling on TTGO Lora32

# Define the OLED width and height
oled_width = 128
oled_height = 32
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

while True:
    # fill(), to fill the screen in black (1) or white (0)
    oled.fill(0)
    
    oled.text( 'Ola,', 0, 0)
    oled.text( 'Manuel', 0, 10)
    oled.text( '', 0, 20)
    oled.text( 'Lameira', 0, 30)

    oled.show()


