'''
Created on Feb 1, 2019
@author: hkalyan
'''

from time import sleep
import threading
# This next import is why we need the RPi.GPIO proxy class
import RPi.GPIO as GPIO

'''
This class acts as a proxy to SenseHatledActivator class and it implements a thread 
'''

class SimpleLedActivator(threading.Thread):
    enableLed = False
    rateInSec = 1
    
    '''
    This is the constructor of this class
    @param rateInSec: Rate at which the message is displayed 
    '''
    
    def __init__(self, rateInSec = 1):
        super(SimpleLedActivator, self).__init__()
        if rateInSec > 0:
            self.rateInSec = rateInSec
            
            '''
                Pins are referred by Broadcom SOC channel
                Declaring pin 17 as output
            '''
            
        GPIO.setmode(GPIO.BCM) 
        GPIO.setup(17, GPIO.OUT)
        
        '''
        This is run method which has a infinite loop in which
        if flag is true no message is displayed as HIGH else message is
        displayed as LOW
        '''
        
    def run(self):
        while True:
            if self.enableLed:
                GPIO.output(17, GPIO.HIGH)
                sleep(self.rateInSec)
                GPIO.output(17, GPIO.LOW)
            sleep(self.rateInSec)
            
    '''
    This will overwrite whatever value is currently stored in rateInSec.
    @return: Returns the rateInSec
    '''
            
    def getRateInSeconds(self):
        return self.rateInSec
    
    '''
    This will enable the flag based on the parameter received.
    @param enable: Its a boolean value that is passed 
    '''   
   
    def setEnableLedFlag(self, enable):
        GPIO(17, GPIO.LOW)
        self.enableLed = enable