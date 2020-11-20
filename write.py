import time
from beebotte import *

bclient = BBT('API_KEY', 'SECRET_KEY')
set_value = Resource(bclient, 'raspberry', 'value')
while True:
    for i in range(1,999):
	time.sleep(1)
	print("Sending the value - "+str(i)+" to Beebotte")
        set_value.write(i)

