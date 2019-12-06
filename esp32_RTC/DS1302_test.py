'''
    DS1302 demo
    Author: shaoziyang
    Date:   2018.3
    http://www.micropython.org.cn
'''
import DS1302
from machine import Pin

ds = DS1302.DS1302(clk=Pin(4), dio=Pin(5), cs=Pin(2))

# ds.DateTime()
# datatime format: [Year, month, day, weekday, hour, minute, second]
ds.start()
ds.DateTime([2019, 11, 27, 4, 23, 02, 0, 0])

# ds.Hour()
# ds.Second(10)

print('hallo?')
print(ds.DateTime())