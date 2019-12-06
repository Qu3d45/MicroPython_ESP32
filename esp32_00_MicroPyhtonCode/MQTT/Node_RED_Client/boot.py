
# LED:                ESP32:
# GND add 330 Ohm --> GND
# VCC -->             GPIO2

# DS18x20:                          ESP32:
# GND -->                           GND
# Signal (middel pin) add 4.7K Ohm -->  GPIO14 + 3V3
# VCC -->                           3V3


import gc
import time
import onewire
import ds18x20
from umqttsimple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp
esp.osdebug(None)
gc.collect()

ssid = 'REPLACE_WITH_YOUR_SSID'
password = 'REPLACE_WITH_YOUR_PASSWORD'
mqtt_server = 'REPLACE_WITH_YOUR_MQTT_BROKER_IP'
# EXAMPLE IP ADDRESS
#mqtt_server = '192.168.1.144'
client_id = ubinascii.hexlify(machine.unique_id())
topic_sub = b'output'
topic_pub = b'temp'

last_sensor_reading = 0
readings_interval = 5

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
    pass

print('Connection successful')
print(station.ifconfig())

ds_pin = machine.Pin(14)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

led = machine.Pin(2, machine.Pin.OUT, value=0)
