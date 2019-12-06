'''
  Using your phone:
    - Disable PIN code on the SIM card
    - Check your balance
    - Check that APN, User, Pass are correct and you have internet
  Ensure the SIM card is correctly inserted into the board
  Ensure that GSM antenna is firmly attached

  NOTE: While GSM is connected to the Internet, WiFi can be used only in AP mode

  More docs on GSM module here:
  https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo/wiki/gsm

  Author: Volodymyr Shymanskyy
'''
# Channel ID 902540
# KEY IL9VIMCHEXM9H3W4
# GET https://api.thingspeak.com/update?api_key=IL9VIMCHEXM9H3W4&field1=0

import socket
import machine
import time
import sys
import gsm


# APN credentials (replace with yours)

GSM_APN = 'Qu3d45_ESP32'  # Your APN
GSM_USER = ''  # Your User
GSM_PASS = ''  # Your Pass

# Power on the GSM module

GSM_PWR = machine.Pin(4, machine.Pin.OUT)
GSM_RST = machine.Pin(5, machine.Pin.OUT)
GSM_MODEM_PWR = machine.Pin(23, machine.Pin.OUT)

GSM_PWR.value(0)
GSM_RST.value(1)
GSM_MODEM_PWR.value(1)

# Init PPPoS

# gsm.debug(True)  # Uncomment this to see more logs, investigate issues, etc.

gsm.start(tx=27, rx=26, apn=GSM_APN, user=GSM_USER, password=GSM_PASS)

sys.stdout.write('Waiting for AT command response...')
for retry in range(20):
    if gsm.atcmd('AT'):
        break
    else:
        sys.stdout.write('.')
        time.sleep_ms(5000)
else:
    raise Exception("Modem not responding!")
print()

print("Connecting to GSM...")
gsm.connect()

while gsm.status()[0] != 1:
    pass

print('IP:', gsm.ifconfig()[0])

# GSM connection is complete.
# You can now use modules like urequests, uPing, etc.