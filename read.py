from beebotte import *
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
led_pin=12
GPIO.setup(led_pin,GPIO.OUT)
bclient = BBT('API_KEY', 'SECRET_KEY')
while True:
	records = bclient.read('raspberry','led')
	x = str(records).split()
	final = x[3].rstrip(',')
	if final =="True":
		GPIO.output(led_pin,GPIO.HIGH)
		print ("The LED is ON")
	else:
		GPIO.output(led_pin,GPIO.LOW)
		print("The LED is OFF")
