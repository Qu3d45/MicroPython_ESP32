from machine import Onewire
from time import sleep

ow = Onewire(15)  # Initialize onewire & DS18B20 temperature sensor
ds = Onewire.ds18x20(ow, 0)

def get_temp_lobo(ds):
    try:
        while True:
            temp = ds.convert_read()
            print("Temperature: {0:.1f}°C".format(temp))
            sleep(4)
    except KeyboardInterrupt:
        print('\nCtrl-C pressed.  Cleaning up and exiting...')
    finally:
        ds.deinit()
        ow.deinit()

get_temp_lobo(ds)