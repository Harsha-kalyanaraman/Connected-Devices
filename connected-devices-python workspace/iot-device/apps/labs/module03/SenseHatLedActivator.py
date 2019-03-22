'''
Created on Feb 1, 2019
@author: hkalyan
'''

from time import sleep
from sense_hat import SenseHat
import threading

'''
This class acts as an API to pass message to senseHat Led and it implements a thread
'''

class SenseHatLedActivator(threading.Thread):
    enableLed = False
    rateInSec = 1
    rotateDeg = 270
    sh = None
    displayMsg = None
    
    '''
    This is the constructor of this class
    @param rotateDeg: Its represents the angle to rotate LED matrix
    @param rateInSec: Rate at which the message is displayed 
    The rate in seconds and rotate deg values are passed to a container
    '''
    
    def __init__(self, rotateDeg = 270, rateInSec = 1):
        super(SenseHatLedActivator, self).__init__()
        if rateInSec > 0:
            self.rateInSec = rateInSec
        if rotateDeg >= 0:
            self.rotateDeg = rotateDeg
            
            '''
            Instance of sensehat class is created
            '''
            
        self.sh = SenseHat() 
        self.sh.set_rotation(self.rotateDeg)
    
    '''
    This is run method which has a infinite loop in which
    if flag is true no message is displayed else message is
    displayed
    '''
        
    def run(self):
        while True:
            if self.enableLed:
                if self.displayMsg != None:
                    self.sh.show_message(str(self.displayMsg))
                else:
                    self.sh.show_letter(str('R'))
                sleep(self.rateInSec)
                self.sh.clear()
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
        self.sh.clear()
        self.enableLed = enable
    
    '''
    This will store the data reveived based on the parameter received.
    @param msg: Its a data that is passed to display message variable
    '''   
        
    def setDisplayMessage(self, msg):
        self.displayMsg = msg