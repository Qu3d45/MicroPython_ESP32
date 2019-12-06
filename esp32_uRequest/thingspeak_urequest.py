import json
import urequests
import time
import wlan
from machine import ADC


#adc = ADC(0)

url = "https://api.thingspeak.com/update?api_key=IL9VIMCHEXM9H3W4&field1={}&field2={}&field3={}&field4={}&field5={}&field6={}&field7={}".format(ds18_temp, pH_final, discharge, tdsValue, temp_dht22, hum_dht22, ecValue)

#moisure = adc.read()

#data = url % moisure

update = urequests.get(url)

ds18_temp = url % str(temp_agua)
pH_final = url % str(pH)
discharge = url % str(caudal_inst)
tdsValue = url % str(tds)
ecValue = url % str(ec)
temp_dht22 = url % str(temp_amb)
hum_dht22 = url % str(humidade)


