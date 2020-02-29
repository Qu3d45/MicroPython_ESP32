import DS1307
from machine import I2C, Pin
from time import sleep, ticks_ms, ticks_diff


i2c = I2C(sda=Pin(21), scl=Pin(22))

with open("timestamp_rtc_ms.txt", mode='r') as rtc_file:
    rtc_readings = rtc_file.read().lstrip('Last reading in millisecond: ')

rtc_readings_last = int(rtc_readings)
print(rtc_readings_last)


rtc_reading_now = ticks_ms()
print(rtc_reading_now)

time_diff = ticks_diff(rtc_reading_now, rtc_readings_last)
print(time_diff)

# Wirte to file
with open("timestamp_rtc_ms.txt", mode='w') as file:
    file.write('Last reading in millisecond: {} \n'.format(rtc_reading_now))
