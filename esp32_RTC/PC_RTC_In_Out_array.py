# read from file and wirte
# calculate the time passed between readings
# Manuel Lameira

import datetime as dt
from dateutil import parser


datetimeFormat = '%Y-%m-%d %H:%M:%S.%f'

# Read from file
rtc_readings = []

with open("timestamp_rtc_array.txt", mode='r') as rtc_file:
    #contents = rtc_file.read()
    for line in rtc_file:
        rtc_readings.append(line.lstrip('Last reading at '))  # .rstrip('\n')
    for element in rtc_readings:
        print(element, end='')

# Reading the last value of the array
print(rtc_readings[-1])

date_list_str = parser.parse(rtc_readings[-1])
date_list = str(date_list_str)

# date_list = '2020-1-9 3:0:20.0'
# print(date_list)
# date_list_now = (2020, 2, 17, 2, 14, 55, 0, 0)

date_list_now = str(dt.datetime.now())
# print(date_list_now)

start_dt = dt.datetime.strptime(date_list, datetimeFormat)
end_dt = dt.datetime.strptime(date_list_now, datetimeFormat)
diff = (end_dt - start_dt)

print("Difference:", diff)
print("Days:", diff.days)
print("Microseconds:", diff.microseconds)
print("Seconds:", diff.seconds)

# Wirte to file
# 'w' = write --> new file
# 'a' = append
# when with is used, no need to close the file
with open("timestamp_rtc_array.txt", mode='a') as file:
    file.write('Last reading at %s \n' %
               (date_list_now))
