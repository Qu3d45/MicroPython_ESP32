# Manuel Lameira
# MicroPython I2C OLED Display on TTGO LoRa32 board

from machine import Pin, I2C

import ssd1306

# The embedded display, is mounted on SCL(15) and SDA(4), but there is another pin must be considered,
# the pin 16 is the OLED_RST. The OLED_RST must be high during normal operations.

rst = Pin(16, Pin.OUT)
rst.value(1)

# ESP32 Pin assignment 
i2c = I2C(scl=Pin(15), sda=Pin(4))

# Define the OLED width, height and iniciate the OLED object
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

while True:
    # fill(), to fill the screen in black (1) or white (0)
    oled.fill(0)
    
    oled.text( 'Ola,', 0, 0)
    oled.text( 'Manuel', 0, 10)
    oled.text( 'Francisco', 0, 20)
    oled.text( 'Machado', 0, 30)
    oled.text( 'Lameira', 0, 40)
    oled.text( 'Lameira', 0, 50)

    oled.show()

# from machine import I2C, Pin
# import ssd1306

# rst = Pin(16, Pin.OUT)
# rst.value(1)
# scl = Pin(15, Pin.OUT, Pin.PULL_UP)
# sda = Pin(4, Pin.OUT, Pin.PULL_UP)
# i2c = I2C(scl=scl, sda=sda, freq=450000)
# oled = ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3c)

