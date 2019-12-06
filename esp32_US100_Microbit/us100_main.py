# Manuel Lameira

#tpin=pin15, rpin=pin14


from us100 import US100
from time import sleep


sonar=US100()
while True:
    print('%.1f' % (sonar.distance_mm()/10))
    sleep(10)

    print('%i' % sonar.temperature)
    sleep(10)