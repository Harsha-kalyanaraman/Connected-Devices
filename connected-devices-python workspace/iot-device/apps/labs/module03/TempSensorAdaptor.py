'''
Created on Jan 25, 2019
@author: hkalyan
'''

from threading import Thread
from labs.common import SensorData
from time import sleep
from labs.module02 import SmtpClientConnector
from labs.common import ConfigUtil
from labs.common import ConfigConst
from sense_hat import SenseHat
from datetime import datetime
from labs.common import ActuatorData
from labs.module03 import TempActuatorEmulator

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
    Run method which executes when start() method is called 
    '''      
          
    def run(self):
        while True:# Run a Infinite loop
            if self.enableEmulator:#when flag is true 
                
                '''
                Instance of SenseHat class is created
                '''
                
                sense = SenseHat()
                
                '''
                The current value is obtained from temperature sensor of sensehat
                '''
                
                self.sensor.curValue = sense.get_temperature_from_pressure()
                
                '''
                Passes that value to the sensor and prints the sensor data.
                '''
                
                self.sensor.addValue(self.sensor.curValue);
                print(self.sensor)
                
                '''
                Obtaining the value of nominal temperature from config file 
                and getting its difference from avg value
                '''
                
                nominal_temp = self.temp.getProperty(ConfigConst.ConfigConst.CONSTRAINED_DEVICE, ConfigConst.ConfigConst.NOMINAL_TEMP)
                self.sensor.diffVal = self.sensor.curValue - self.sensor.avgValue;
                
                '''
                If the sensor data exceeds or reduces below the threshold values
                data is updated and appended with a list of log values. And a 
                warning is printed and sent to a cloud based E-mail 
                '''
                
                if self.sensor.curValue >= (self.sensor.getAvgValue() + 3):
                    data = (self.sensor)
                    self.sensor.timestamp = datetime.now();
                    SensorData.SensorData.log_values.append(self.sensor)
                    print(SensorData.SensorData.log_values)
                    print("Warning!! Temperature exceeded the average temperature by %.2f degrees" %(self.sensor.diffVal));
                    sen_not = SmtpClientConnector.SmtpClientConnector(); 
                    sen_not.publishMessage("Temperature Alert *****IMPORTANT*****", data);
                    print('Nominal temperature: ',nominal_temp)
                    
                    '''
                    Based on this information Actuator is triggered to send
                    an increase the temperature or reduce the temperature
                    message. 
                    '''
                    
                if self.sensor.curValue!=nominal_temp:
                    self.actuator_data = ActuatorData.ActuatorData()
                    self.diff = (self.sensor.curValue - float(nominal_temp))
                    
                    if self.diff>0:
                        self.actuator_data.setValue(self.sensor.curValue - float(nominal_temp))
                        self.actuator_data.setCommand(ActuatorData.COMMAND_SET);
                    else:
                        self.actuator_data.setValue(float(nominal_temp) - self.sensor.curValue)
                        self.actuator_data.setCommand(ActuatorData.COMMAND_RESET)
                    self.temp_emul.processMessage(self.actuator_data)
                
                '''
                Delay variable is obtained from the import files
                '''
                    
                delay = int(self.temp_delay.getProperty(ConfigConst.ConfigConst.CONSTRAINED_DEVICE, ConfigConst.ConfigConst.POLL_CYCLES_KEY))
                sleep(delay)