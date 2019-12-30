'''
    DS1307 demo
    Author: shaoziyang
    Date:   2018.3
    http://www.micropython.org.cn
'''
import DS1307
from machine import I2C, Pin
from time import sleep

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



i2c = I2C(sda=Pin(5), scl=Pin(4))
ds = DS1307.DS1307(i2c)

ds.DateTime()
#  datatime format: [Year, month, day, weekday, hour, minute, second]
#ds.DateTime([2019, 12, 19, 5, 23, 01, 0, 0])


while True:
    date_tuple = ds.DateTime()
    time = date_tuple[4:7]
    print("")
    print("Time: ", str(time))
    weekday = date_tuple[3]
    day = switch_day(weekday)
    print("Day: ", str(day))
    date = date_tuple[0:3]
    print("Date: ", str(date))
    sleep(5)
