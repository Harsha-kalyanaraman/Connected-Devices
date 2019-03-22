'''
Created on Jan 25, 2019

Emulator class implements a child thread and has a run method
in which if a flag is true prints str representation of class SensorData.
If the threshold condition is satisfied calls the smtpClientConnector to pass 
the message to E-mail account

@author: hkalyan
'''
from threading import Thread
from random import uniform
from labs.common import SensorData
from time import sleep
from labs.module02 import SmtpClientConnector
from labs.common import ConfigUtil
from labs.common import ConfigConst

class TempSensorEmulator(Thread):
  
    '''
    Constructor for TempeSensorEmulator.
    Initializes the Thread.
    Sets the Flag enableEmulator true.
    Instance of Sensor data class is initialized.
    Gets the delay time from the imported files
    @param name The name of the sensor data to be passed to SensorData constructor.
    '''
    
    def __init__(self,name):
        Thread.__init__(self)
        self.enableEmulator = True
        self.sensor = SensorData.SensorData(name,0,30)
        self.temp_delay = ConfigUtil.ConfigUtil('../../../config/ConnectedDevicesConfig.props');
        
    '''
    Run method which executes when start() method is called
    '''   
             
    def run(self):
        while True:# Run a Infinite loop
            if self.enableEmulator:#when flag is true 
                
                '''
                 Run a Uniform method to generate random float values within max and min
                 temperature range
                '''
                
                self.sensor.curValue = uniform(float(self.sensor.getMinValue()), float(self.sensor.getMaxValue()));
                
                '''
                Passes that value to the sensor and prints the sensor data.
                '''
                
                self.sensor.addValue(self.sensor.curValue);
                print(self.sensor);
                
                '''
                If reached threshold sends an alert using smtpClientConnector by
                Creating an instance of SmtpClientConnector class
                '''
                
                if self.sensor.curValue >= (25):
                    data = (self.sensor);
                    print(data);
                    print("ALERT TEMPERATURE EXCEEDED 25",chr(176),"C");
                    sen_not = SmtpClientConnector.SmtpClientConnector(); 
                    sen_not.publishMessage("Temperature Alert *****IMPORTANT*****", data);
                delay = int(self.temp_delay.getProperty(ConfigConst.ConfigConst.CONSTRAINED_DEVICE, ConfigConst.ConfigConst.POLL_CYCLES_KEY));     
                sleep(delay);