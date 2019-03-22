'''
Created on Feb 1, 2019

@author: hkalyan
'''
import os
from datetime import datetime

COMMAND_OFF = 0
COMMAND_ON = 1
COMMAND_SET = 2
COMMAND_RESET = 3
STATUS_IDLE = 0
STATUS_ACTIVE = 1
ERROR_OK = 0
ERROR_COMMAND_FAILED = 1
ERROR_NON_RESPONSIBLE = -1

'''
This class is used for setting the various parameter of the Actuator
and return the compiled output data in a string format
'''
class ActuatorData():

    timeStamp = None
    name = 'Not set'
    hasError = False
    command = 0
    errCode = 0
    statusCode = 0
    stateData = None
    val = 0.0
    
    '''
    This is the constructor of the Actuator Data Class
    It has a function named UpdateTimeStamp()
    '''
    def __init__(self):
        self.updateTimeStamp()
        
    '''
    This will overwrite whatever value is currently stored in command.
    
    @return: Returns the command
    ''' 
    def getCommand(self):
            return self.command
    
    '''
    This will overwrite whatever value is currently stored in name.
    
    @return: Returns the name
    '''
    def getName(self):
        return self.name
    
    '''
    This will overwrite whatever value is currently stored in stateData.
    
    @return: Returns the stateData
    '''
    def getStateData(self):
        return self.stateData
    
    '''
    This will overwrite whatever value is currently stored in statusCode.
    
    @return: Returns the statusCode
    '''
    def getStatusCode(self):
        return self.statusCode
    
    '''
    This will overwrite whatever value is currently stored in ErrorCode.
    
    @return: Returns the ErrorCode
    '''
    def getErrorCode(self):
        return self.errCode
    
    '''
    This will overwrite whatever value is currently stored in value.
    
    @return: Returns the value
    '''
    def getValue(self):
        return self.val
    
    '''
    This will overwrite whatever value is currently stored in hasError.
    
    @return: Returns the hasError 
    '''
    def hasError(self):
        return self.hasError
    
    '''
    This will store the command.
    '''   
    def setCommand(self, command):
        self.command = command
    
    '''
    This will store the name.
    '''   
    def setName(self, name):
        self.name = name
    
    '''
    This will store the StateData.
    ''' 
    def setStateData(self, stateData):
        self.stateData = stateData
    
    '''
    This will store the statusCode.
    '''    
    def setStatusCode(self, statusCode):
        self.statusCode = statusCode
    
    '''
    This will store the ErrorCode.
    The hasError flag is set to true if errCode flag is true else hasErr is false
    '''    
    def setErrorCode(self, errCode):
        self.errCode = errCode
    
        if (self.errCode != 0):
            self.hasError = True
        else:
            self.hasError = False
    
    '''
    This will store the value.
    '''       
    def setValue(self, val):
        self.val = val
    
    '''
    This function updates the current data using the parameter passed
    
    @param data: The actuator data is passed and actuator variable are stored 
    ''' 
    def updateData(self, data):
        self.command = data.getCommand()
        self.statusCode = data.getStatusCode()
        self.errCode = data.getErrorCode()
        self.stateData = data.getStateData()
        self.val = data.getValue()
    
    '''
    This function stores the current date time to a container
    ''' 
    def updateTimeStamp(self):
        self.timeStamp = str(datetime.now())
    
    '''
    This funtion does object to string of this class
    Contains a simple container which has a string of all the data to be
    printed.
    
    @return: customStr: Returns the the string container
    '''
    def __str__(self):
        customStr = \
        str(self.name + ':' + \
        os.linesep + '\tTime: ' + self.timeStamp + \
        os.linesep + '\tCommand: ' + str(self.command) + \
        os.linesep + '\tStatus Code: ' + str(self.statusCode) + \
        os.linesep + '\tError Code: ' + str(self.errCode) + \
        os.linesep + '\tState Data: ' + str(self.stateData) + \
        os.linesep + '\tValue: ' + str(self.val))
        return customStr