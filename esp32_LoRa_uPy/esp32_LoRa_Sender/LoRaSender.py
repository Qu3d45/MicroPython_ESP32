# Manuel Lameira
# LCD 16x2 i2c with Micropython
# Original Code from Guillermo Sampallo: https://www.youtube.com/watch?v=i82YLOAw_iU

# LCD --> ESP 32
# -------------
# GND --> GND
# VCC --> Vin (5V)
# SDA --> GPIO 21
# SCL --> GPIO 22

# Files Needed:
# -------------
# lcd_api.py
# i2c_lcd.py
# esp8266_i2c_lcd.py


from time import sleep
from uPySensors.ssd1306_i2c import Display


from time import sleep_ms, ticks_ms
from machine import I2C, Pin
from esp8266_i2c_lcd import I2cLcd


i2c = I2C(scl=Pin(22), sda=Pin(21), freq=400000)
lcd = I2cLcd(i2c, 0x27, 2, 16)

# Comment icd.blacklight_on() if jumper is connected
# lcd.blacklight_on()

lcd.clear()
lcd.putstr("Hello,")
lcd.move_to(0, 1)
lcd.putstr("Manuel Lameira!")


def send(lora):
    counter = 0
    print("LoRa Sender")
    display = Display()

    while True:
        payload = 'Hello ({0})'.format(counter)
        #print("Sending packet: \n{}\n".format(payload))
        display.show_text_wrap(
            "{0} RSSI: {1}".format(payload, lora.packetRssi()))
        lora.println(payload)

        counter += 1
        sleep(5)
