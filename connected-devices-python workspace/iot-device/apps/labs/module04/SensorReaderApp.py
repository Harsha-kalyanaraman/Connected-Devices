'''
Created on Feb 5, 2019
@author: hkalyan
'''
from time import sleep 
from labs.module04 import I2CSenseHatAdaptor

'''
In this api instanceof I2CSenseHatAdaptor is initialized
Derived Thread is made as Daemon thread. Made flag value true.
and calls start method to run
'''
sensor_data = I2CSenseHatAdaptor.I2CSenseHatAdaptor()
sensor_data.daemon = True
sensor_data.enableEmulator = True
sensor_data.start()

'''
Open an Infinite loop for this app to keep running
'''
while True:
    sleep(1)
    pass
    