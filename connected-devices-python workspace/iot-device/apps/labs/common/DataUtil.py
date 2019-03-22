'''
Created on Feb 16, 2019

@author: hkalyan
'''
import json
from labs.common.ActuatorData import ActuatorData
from labs.common.SensorData import SensorData

'''
This Class converts the object data to JSON format and vice versa
'''
class DataUtil(object):
   
    def __init__(self):
        '''
        Constructor
        '''
        
    '''
    This function is used for the conversion of ActuatorData object to JSON format
    
    @param ActuatorData: Instance of the ActuatorData class
    @return: Converted JSON format output 
    '''
    def ActuatorDataToJson(self, ActuatorData):
        self.jsonAd = json.dumps(ActuatorData.__dict__)
        outputAd = open('actuatordata.txt','w')
        outputAd.write(self.jsonAd)
        return self.jsonAd
    
    '''
    This function is used for the conversion of JSON format to ActuatorData object
    
    @param jsonData: Instance of the ActuatorData class
    @return: Converted ActuatorData object output 
    '''
    def jsonToActuatorData(self, jsonData):
        adDict = json.loads(jsonData)
        #print(" decode [pre] --> " + str(adDict))
        ad = ActuatorData()
        ad.name = adDict['name']
        ad.timeStamp = adDict['timeStamp']
        ad.hasError = adDict['hasError']
        ad.command = adDict['command']
        ad.errCode = adDict['errCode']
        ad.statusCode = adDict['statusCode']
        ad.stateData = adDict['stateData']
        ad.curValue = adDict['curValue']
        #print(" decode [post] --> " + str(ad))
        return ad
    
    '''
    This function is used for the conversion of SensorData object to JSON format
    
    @param SensorData: Instance of the SensorData class
    @return: Converted JSON format output 
    '''
    def SensorDataToJson(self,sensor_data):
        data = {};
        data['name'] = sensor_data.name;
        data['avgVal'] = sensor_data.avgValue;
        data['maxVal'] = sensor_data.getMaxValue();
        data['minVal'] = sensor_data.getMinValue();
        data['curVal'] = sensor_data.getValue();
        data['timeStamp'] = str(sensor_data.timeStamp);
        data['sampleCount'] = str(sensor_data.sampleCount);
        self.jsonSd = json.dumps(data)
        outputSd = open('sensordata.txt','w')
        outputSd.write(self.jsonSd)
        return self.jsonSd
    
    '''
    This function is used for the conversion of JSON format to SensorData object
    
    @param jsonData: Instance of the SensorData class
    @return: Converted SensorData object output 
    '''
    def jsonToSensorData(self, jsonData):
        sdDict = json.loads(jsonData)
        #print(" decode [pre] --> " + str(sdDict))
        sd = SensorData('Temperature',0,30)
        sd.name = sdDict['name']
        sd.timeStamp = sdDict['timeStamp']
        sd.avgValue = sdDict['avgVal']
        sd.minValue = sdDict['minVal']
        sd.maxValue = sdDict['maxVal']
        sd.curValue = sdDict['curVal']
        #print(" decode [post] --> " + str(sd))
        return sd