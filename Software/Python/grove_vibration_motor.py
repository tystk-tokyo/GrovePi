# GrovePi + Grove Vibration Motor
# http://www.seeedstudio.com/wiki/Grove_-_Vibration_Motor

import time
import grovepi

# Connect the Vibration Motor to digital port D8
vibration_motor = 8

grovepi.pinMode(vibration_motor,"OUTPUT")

while True:
    try:
        # Start vibrating for 1 second
        grovepi.digitalWrite(vibration_motor,1)
        print 'start'
        time.sleep(1)

        # Stop vibrating for 1 second, then repeat
        grovepi.digitalWrite(vibration_motor,0)
        print 'stop'
        time.sleep(1)

    except IOError:
        print "Error"
