# Manuel Lameira
# DTH 22 readings using MicroPython

# DTH22 --> ESP32
# GND   --> GND
# VCC   --> 5v or 3.3v
# DAT   --> D14

from machine import Pin, UART
from time import sleep

uart = UART(1, 9600)
uart.init(9600, bits=8, parity=None, stop=1)

while True:
    
    ch = b""
    print(ch)
    while ch != b"quit":
        if uart.any():
            ch = uart.read()
            uart.write(ch)
    
    print(ch)