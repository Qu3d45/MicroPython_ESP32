# Manuel Lameira
# LoRa E32 UART mode

# Test of UART conection with ESP32 and Ebyte E32

# E32 --> ESP32
# ---------------
# GND --> GND
# VCC --> VCC
# AUX -->
# TX  --> RX (UART 2) 17
# RX  --> TX (UART 2) 16
# M1  -->
# M0  -->

from machine import UART, Pin
from time import sleep



uart = UART(2, 9600)
uart.init(9600, bits=8, parity=None, stop=1)

while True==True:
  val = uart.read()
  print(val)
  sleep(1)

# from machine import I2C, Pin
# import utime
# from machine import UART

# uart = UART(0, 9600)
# uart.init(9600)

# while True==True:
#   val = uart.read()
#   print(val)
#   utime.sleep(1)