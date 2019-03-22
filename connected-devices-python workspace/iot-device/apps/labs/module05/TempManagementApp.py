'''
Created on Feb 16, 2019

@author: hkalyan
'''

from time import sleep 
from labs.module05 import TempSensorAdaptor

'''
In this api instanceof TempSensorEmulator is initialized
Derived Thread is made as Daemon thread
and calls start method to run
'''
sensor_data = TempSensorAdaptor.TempSensorAdaptor("New sensor readings")
sensor_data.daemon = True
sensor_data.start()

'''
Open an Infinite loop for this app to keep running
'''
while True:
    sleep(1)
    pass
    