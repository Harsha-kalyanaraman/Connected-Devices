'''
Created on Jan 25, 2019

@author: hkalyan
'''
from time import sleep 
from labs.module02 import TempSensorEmulator

'''
In this api instanceof TempSensorEmulator is initialized
Derived Thread is made as Daemon thread
and calls start method to run
'''
sensor_data = TempSensorEmulator.TempSensorEmulator("Temperature Information")
sensor_data.daemon = True
sensor_data.start()

'''
Open an Infinite loop for this app to keep running
'''
while True:
    sleep(1)
    pass