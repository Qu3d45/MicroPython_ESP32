import machine
import time


trig = machine.Pin(4, machine.Pin.OUT)
echo = machine.Pin(2, machine.Pin.IN)

timeout_us = 25000  # no need to wait more then sensor's range limit (4,00 m)

sensor_hight = 1.50

while True:
    temp_dht22 = 23.3
    hum_dht22 = 98
    
    trig.value(0)  # Stabilize the sensor
    time.sleep_us(2)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)

    duration = machine.time_pulse_us(echo, 1, timeout_us)

    if duration < 0:
        print("Out of range")
    else:
        # To calculate the distance we get the pulse_time and divide it by 2
        # (the pulse walk the distance twice)
        # the sound speed on air (343.2 m/s), that It's equivalent to
        # 0.034320 cm/us that is 1cm each 29.1us

        # Calculate the Speed of Sound in M/S
        sound_comp = 331.4 + (0.606 * temp_dht22) + (0.0124 * hum_dht22)
        print(sound_comp, " sound_comp")
        
        distance = (duration / 2) * (sound_comp/1000000) # m/us 
        print(distance, " distance")
        
        water_hight = sensor_hight - distance #m
        print(water_hight, " water_hight2")
        
       
        discharge = (0.209763317*(water_hight**(5/3)))/((water_hight + 0.918486862)**(2/3))
        print(discharge, " m3/s")
        
        time.sleep(3)
