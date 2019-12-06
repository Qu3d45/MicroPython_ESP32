from machine import Pin, I2C
import ssd1306

# i2c = I2C(-1, scl=Pin(22), sda=Pin(21), freq=100000)
i2c = I2C(0, I2C.MASTER, baudrate=100000)

lcd = ssd1306.SSD1306_I2C(128,64,i2c)

lcd.text("Micropython",0,0)
lcd.text("are",24,16)
lcd.text("Awesome",64,24)
lcd.show()