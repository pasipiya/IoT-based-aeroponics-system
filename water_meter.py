import RPi.GPIO as GPIO
import time, sys

LIQUID_FLOW_SENSOR = 32

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LIQUID_FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_UP)

global rotation
rotation = 0

def countPulse(channel):
   rotation = rotation+1
   print ("Total rotation = "+str(rotation))
   litre = rotation / (60 * 7.5)
   two_decimal = round(litre,3)
   print("Total consumed = "+str(two_decimal)+" Litres")

GPIO.add_event_detect(LIQUID_FLOW_SENSOR, GPIO.FALLING, callback=countPulse)

while True:
    try:
        time.sleep(1)

    except KeyboardInterrupt:
        print 'Program terminated, Keyboard interrupt'
        GPIO.cleanup()
        sys.exit()
