'''
Created on Feb 16, 2019

@author: hkalyan
'''

from threading import Thread
from labs.common import SensorData
from time import sleep
from labs.module02 import SmtpClientConnector
from labs.common import ConfigUtil
from labs.common import ConfigConst
#from sense_hat import SenseHat
from datetime import datetime
from labs.module03 import TempActuatorEmulator
from labs.common.DataUtil import DataUtil
from random import uniform
import json

'''
Adaptor class implements a child thread and has a run method
in which if a flag is true prints str representation of class SensorData.
If the threshold condition is satisfied calls the smtpClientConnector to pass 
the message to E-mail account
'''
class TempSensorAdaptor(Thread):
  
    '''
    Constructor for TempeSensorEmulator.
    Initializes the Thread.
    Sets the Flag enableEmulator true.
    Instance of Sensor data class is initialized.
    Gets the delay time from the imported files
    Instance of TempActuatorEmulator class is created
    
    @param name The name of the sensor data to be passed to SensorData constructor.
    '''
    def __init__(self,name):
        Thread.__init__(self)
        self.enableEmulator = True
        self.sensor = SensorData.SensorData(name,0,30)
        self.temp_delay = ConfigUtil.ConfigUtil('../../../config/ConnectedDevicesConfig.props')
        self.temp = ConfigUtil.ConfigUtil('../../../config/ConnectedDevicesConfig.props')
        self.temp_emul = TempActuatorEmulator.TempActuatorEmulator()
    
    '''
    This method writes the passed JSON data to a text file which can be called
    in the future to convert to an object
    
    @param value:The JSON data that is passed to this function
    @param filename:The name of the file that is passed with its type(eg.txt)
    '''   
    def fileWrite(self,value,filename):
        with open(filename,'w'):
            json.dumps(value) 
    
    '''
    Run method which executes when start() method is called 
    '''        
    def run(self):
        print("Created DataUtil instance.\n"+"Starting data formatter app test...\n"+"Created DataUtil instance.\n"+"Starting temp adaptor app daemon thread...\n");
        while True:# Run a Infinite loop
            if self.enableEmulator:#when flag is true 
                
                '''
                Instance of SenseHat class is created not used in this project
                But can be utilized when a SenseHAT is connected
                '''
                #sense = SenseHat()
                
                '''
                The current value is obtained from temperature sensor of sensehat
                '''
                #self.sensor.curValue = sense.get_temperature_from_pressure()
                
                '''
                Random simulated value generated to test this project
                '''
                self.sensor.curVal = uniform(float(self.sensor.getMinValue()), float(self.sensor.getMaxValue()));
                
                '''
                Passes that value to the sensor and prints the sensor data.
                '''
                self.sensor.addValue(self.sensor.curVal);
                
                '''
                Obtaining the value of nominal temperature from config file 
                and getting its difference from avg value
                '''
                self.sensor.diffVal = self.sensor.curValue - self.sensor.avgValue;
                
                print("--------------------")
                print(self.sensor)# Printing Sensor data
                
                '''
                If the sensor data exceeds or reduces below the threshold values
                data is converted to JSON format. The it is updated and appended
                with a list of log values. And a warning is printed and sent to
                a cloud based E-mail 
                '''
                if self.sensor.curValue >= (self.sensor.getAvgValue() + 3):
                    data = DataUtil()
                    json_data = data.SensorDataToJson(self.sensor)
                    self.fileWrite(json_data,"data.json")#JSON data written to a txt file
                    self.sensor.timestamp = datetime.now();
                    SensorData.SensorData.log_values.append(self.sensor)
                    #print(SensorData.SensorData.log_values) 
                    print("\nWarning!! Temperature exceeded the average temperature by %.2f degrees. Converting data...\n" %(self.sensor.diffVal));
                    print("JSON data: "+json_data+"\n")
                    sen_not = SmtpClientConnector.SmtpClientConnector(); 
                    sen_not.publishMessage("Temperature Alert *****IMPORTANT*****", json_data);
                
                '''
                Delay variable is obtained from the import files to refresh the 
                app for every POLL_CYCLES_KEY
                '''    
                delay = int(self.temp_delay.getProperty(ConfigConst.ConfigConst.CONSTRAINED_DEVICE, ConfigConst.ConfigConst.POLL_CYCLES_KEY))
                sleep(delay)