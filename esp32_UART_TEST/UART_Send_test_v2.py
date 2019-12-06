# Manuel Lameira
# DTH 22 readings using MicroPython

# DTH22 --> ESP32
# GND   --> GND
# VCC   --> 5v or 3.3v
# DAT   --> D14

from machine import Pin, UART
from time import sleep

uart = UART(1, 9600)
uart.init(9600, bits=8, parity=None, stop=1,tx=17, rx=16,txbuf=512)

bin_arr = bytearray(b'') # Payload for test

for i in range(1,256): 
    bin_arr.append(i)

while True:
    
    uart.write(bin_arr)
#    time.sleep_us( ctl_up_us ) # !!! Problematic place
#    ctrlPin(0)    
    sleep(3)
    
#
#    ch = b""
#    print(ch)
#    while ch != b"quit":
#        if uart.any():
#            ch = uart.read()
#            uart.write(ch)
    
    print(bin_arr)