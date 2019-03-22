
'''
Created on Jan 25, 2019

@author: hkalyan
'''
import os
from datetime import datetime

'''
This class is used for setting the various parameter of the temperature sensor
and return the compiled output data in a string format
'''
class SensorData(object):
  
    timeStamp = None
    name = 'Not set'
    curValue = 0
    avgValue = 0
    minValue = 0
    maxValue = 25
    totValue = 0
    sampleCount = 0
    log_values = list();
    
    '''
    Constructor for SensorData.
    
    @param name: The name of the data which is compiled.
    @param maxValue:The maximum limit to which the sensor can respond
    @param minValue:The minimum limit to which the sensor can respond  
    '''
    def __init__(self, name,minValue,maxValue):
        self.timeStamp = str(datetime.now())
        self.name = name;
        self.maxValue = maxValue;
        self.minValue = minValue;
        self.sampleCount = 0;
    
    '''
    Overrides the data to curVaue, minValue, maxValue, totValue and avgValue
    based on the obtained newValue. Also has a sample counter and a time stamp.
    
    @param newValue: The new data obtained, to update the existing values
    '''
    def addValue(self, newValue):
        self.sampleCount += 1
        self.timeStamp = str(datetime.now())
        self.curValue = newValue
        self.totValue += newValue
        if (self.curValue < self.minValue):
            self.minValue = self.curValue
        if (self.curValue > self.maxValue):
            self.maxValue = self.curValue
        if (self.totValue != 0 and self.sampleCount > 0):
            self.avgValue = self.totValue / self.sampleCount
    
    '''
    This will overwrite whatever value is currently stored in avgValue
    
    @return: Returns the avgValue
    '''           
    def getAvgValue(self):
        return self.avgValue
    
    '''
    This will overwrite whatever value is currently stored in maxValue.
    
    @return: Returns the maxValue
    '''     
    def getMaxValue(self):
        return self.maxValue

    '''
    This will overwrite whatever value is currently stored in minValue.
    
    @return: Returns the minValue
    '''     
    def getMinValue(self):
        return self.minValue
   
    '''
    This will overwrite whatever value is currently stored in curValue.
    
    @return: Returns the curValue
    '''     
    def getValue(self):
        return self.curValue
   
    '''
    This will stores the name of the sensorData.
    '''     
    def setName(self, name):
        self.name = name
   
    '''
    This is a string representation of the instance of this class
    Contains a simple container which has a string of all the  data to be
    printed to output screen.
    
    @return: customStr: Returns the the string container
    '''      
    def __str__(self):
        customStr = \
        str(self.name + ':' +  \
        os.linesep + '\tname = ' + "Temperature" +","+ \
        os.linesep + '\tTime = ' + self.timeStamp +","+ \
        os.linesep + '\tcurrentVal = ' + str(self.curValue) + chr(176)+"C,"+ \
        os.linesep + '\taverageVal = ' + str(self.avgValue) + chr(176)+"C,"+ \
        os.linesep + '\tMin Temperature = ' + str(self.minValue) + chr(176)+"C,"+ \
        os.linesep + '\tMax Temperature = ' + str(self.maxValue))+chr(176)+"C"+ \
        os.linesep + '\tMaintain your temperature at 20'+chr(176)+"C"+' to maintain within safe limits'
        return customStr