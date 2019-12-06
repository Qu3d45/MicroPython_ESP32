import machine
pin = 14

dht = machine.DHT(machine.Pin(pin), machine.DHT.DHT2X)

result, temperature, humidity = dht.read()

x = result
y = float(temperature)
z = int(humidity)

print(x)
print(y)
print(z)

if not result:
    print('Failed!')
else:
    print('t={} C'.format(temperature))
    print('h={} % RH'.format(int(humidity)))