from machine import I2C, Pin, deepsleep
from time import sleep, ticks_ms, ticks_diff


i2c = I2C(sda=Pin(21), scl=Pin(22))

rtc_start = 0
print(rtc_start)

sleep(10)

rtc_reading_now = ticks_ms()
print(rtc_reading_now)

time_diff = ticks_diff(rtc_reading_now, rtc_start)
print(time_diff)

caudal = ((time_diff/1000)+10) * 35
print(caudal, 'm3')

deepsleep(10)
