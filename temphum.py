
import sys
import Adafruit_DHT
import time

i = 0

try:
    while True:

        humidity, temperature = Adafruit_DHT.read_retry(11, 4)

        print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)
        i = i + 1
        time.sleep ( 1800 )

except KeyboardInterrupt:

    print ' Sensor stopped!! looped %i times ' % i
    sys.stdout=open("test.txt","w")
    print '{0:0.1f}'.format(temperature, humidity)
    print '{1:0.1f}'.format(temperature, humidity)
    sys.stdout.close()