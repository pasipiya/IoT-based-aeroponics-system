import RPi.GPIO as GPIO
import time
import Adafruit_DHT
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
from beebotte import *
import lcd_board

bbt = BBT('API_KEY', 'SECRET_KEY')
period = 1
pin = 4 
mist_pin = 40 
GPIO.setup(mist_pin,GPIO.OUT)
temp_resource   = Resource(bbt, 'raspberry', 'temperature')
humid_resource  = Resource(bbt, 'raspberry', 'humidity')

def run():
  while True:
    records = bbt.read('raspberry','mist')
    x = str(records).split()
    final = x[3].rstrip(',')
    if final =="True":
      GPIO.output(mist_pin,GPIO.LOW)
      print("The mist machine is ON")
    else:
       GPIO.output(mist_pin,GPIO.HIGH)
       print("The mist machine is OFF")
    humidity, temperature = Adafruit_DHT.read_retry( Adafruit_DHT.DHT11, pin )
    if humidity is not None and temperature is not None:
      temp=int(temperature)
      humd=int(humidity)
      print ("Current Temperature is = "+str(temp)+"'C")
      print ("Current Humidity level is = "+str(humd)+"%")
      print ("________________________________________\n")
      lcd_board.first("Temperature-"+str(temp)+"'C","Humidity - "+str(humd)+"%")
      try:
          temp_resource.write(temperature)
          humid_resource.write(humidity)
      except Exception:
          print "Error can't write data to Beebotte"
    else:
        print "Failed to get reading. Try again!"

    time.sleep( period )

run()
