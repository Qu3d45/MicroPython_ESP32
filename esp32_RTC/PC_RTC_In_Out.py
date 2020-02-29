# read from file and wirte
# calculate the time passed between readings
# Manuel Lameira

import datetime as dt
from dateutil import parser


datetimeFormat = '%Y-%m-%d %H:%M:%S.%f'

# Read from file
with open("timestamp_rtc.txt", mode='r') as rtc_file:
    rtc_readings = rtc_file.read().lstrip('Last reading at ')  # .rstrip('\n')


rtc_last_reading = str(parser.parse(rtc_readings))
print('XXXXXXXX last: ', rtc_last_reading)
# -----

# Codigo aqui

# ------
rtc_reading_now = str(dt.datetime.now())
print('XXXXXXXXX now: ', rtc_reading_now)

start_dt = dt.datetime.strptime(rtc_last_reading, datetimeFormat)
end_dt = dt.datetime.strptime(rtc_reading_now, datetimeFormat)
diff = (end_dt - start_dt)

print("Difference:", diff)
print("Days:", diff.days)
print("Microseconds:", diff.microseconds)
print("Seconds:", diff.seconds)

caudal = diff.seconds * 10

print('caudal: ', caudal)

# Wirte to file
with open("timestamp_rtc.txt", mode='w') as file:
    file.write('Last reading at {} \n'.format(rtc_reading_now))
