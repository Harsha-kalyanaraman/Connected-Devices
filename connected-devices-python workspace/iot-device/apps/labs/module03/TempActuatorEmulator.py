'''
Created on Feb 2, 2019
@author: hkalyan
'''

from labs.common import ActuatorData
from labs.module03 import SenseHatLedActivator

'''
This class invokes a processMessage function
'''

class TempActuatorEmulator(object):
    
    '''
    This is the Constructor of this class and an instance of Actuator data class is created
    '''
    
    def __init__(self):
       
        '''
        Constructor
        '''
        
        self.actuator_data = ActuatorData.ActuatorData()
        
    '''
    This function starts the run method in SenseHatLedActivator class
    To trigger the actuator to display the message.
    @param act_data: This is the data given to actuator based on which it triggers
    a message 
    '''  
        
    def processMessage(self,act_data):
        
        if act_data!= self.actuator_data:
            self.val = act_data.getValue()
        
        if act_data.getCommand()==2:
            mes = "Reduce the Temperature by %.2f" %(self.val)
        else:
            mes = "Increase the Temperature by %.2f" %(self.val)
           
            '''
            Instance of SenseHatLedActivator is created and message is passed
            and flag value is set to enable
            '''
            
        sense_hat = SenseHatLedActivator.SenseHatLedActivator()
        sense_hat.setDisplayMessage(mes);
        sense_hat.setEnableLedFlag('enable');
        
        try:
            sense_hat.start();
        except:
            print("Couldn't activate Actuator");
        finally:
            sense_hat.enableLed = False
            
            '''
            The actuator data is passed to updatedata function
            '''
            
            self.actuator_data.updateData(act_data);
        