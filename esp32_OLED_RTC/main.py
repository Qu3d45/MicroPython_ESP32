# Manuel Lameira
# MicroPython I2C OLED Display with internal RTC

from machine import Pin, I2C, RTC
from time import sleep, sleep_ms

import ssd1306
import DS1307


def switch_day(argument):
    switcher = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday",
    }
    return switcher.get(argument, "Invalid month")


# ESP32 Pin assignment
# 5=SDK/SDA  4=SCK/SCL  As per labeling on ESP32 DevKi
i2c = I2C(-1, scl=Pin(4), sda=Pin(5))
i2c2 = I2C(sda=Pin(0), scl=Pin(2))

ds = DS1307.DS1307(i2c2)

# Define the OLED width and height
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# rtc = RTC()
# print(rtc)
# # struct_time order: year, month, day, weekday, hour, minute, second
# rtc.init((2019, 12, 12, 7, 16, 59, 0, 0))  # set a specific date and time
# print(rtc.datetime())

#ds.DateTime()
#  datatime format: [Year, month, day, weekday, hour, minute, second]
ds.DateTime([2019, 12, 19, 5, 22, 20, 0, 0])

ds.Hour()

while True:
    # fill(), to fill the screen in black (1) or white (0)
    oled.fill(0)

    #time = str(rtc.datetime())
    date_tuple = ds.DateTime()
    time = ds.Hour()
    weekday = date_tuple[3]
    day = switch_day(weekday)
    date = date_tuple[0:3]

    oled.text('Hora:', 0, 0)
    oled.text(str(time), 0, 10)
    oled.text('', 0, 20)
    oled.text('Data:', 0, 30)
    oled.text(str(date), 0, 40)
    oled.text(day, 0, 50)

    oled.show()
