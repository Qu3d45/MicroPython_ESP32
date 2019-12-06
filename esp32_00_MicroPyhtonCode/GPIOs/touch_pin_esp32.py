
# Touch on GIPO 4

from time import sleep
from machine import TouchPad, Pin
ESP32_Touch_Pin_Circuit

touch_pin = TouchPad(Pin(4))

while True:
    touch_value = touch_pin.read()
    print(touch_value)
    sleep(0.5)
