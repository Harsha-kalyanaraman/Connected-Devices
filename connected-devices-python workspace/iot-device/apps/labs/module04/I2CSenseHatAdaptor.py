'''
Created on Feb 3, 2019
@author: hkalyan
'''
import smbus
import threading
from time import sleep
from labs.common import ConfigUtil
from labs.common import ConfigConst

'''
Address constants and others constants which can be used whenever required.
'''
i2cBus = smbus.SMBus(1) # Use I2C bus No.1 on Raspberry Pi3 +
enableControl = 0x00
enableMeasure = 0x08
accelAddr = 0x1C # address for IMU (accelerometer)
magAddr = 0x6A # address for IMU (magnetometer)
pressAddr = 0x5C # address for pressure sensor
humidAddr = 0x5F # address for humidity sensor
begAddr = 0x28
totBytes = 6
DEFAULT_RATE_IN_SEC = 5

'''
I2CSenseHatAdaptor class makes use of the Smbus library and gets the I2C access. 
It implements a thread from the main thread. It also consists of a flag method
which acts as a switch for the App to work on.
'''
class I2CSenseHatAdaptor(threading.Thread):
    rateInSec = DEFAULT_RATE_IN_SEC
    
    '''
    Constructor for this class. An instance of configconst is created. Load 
    Config method is called. Initializes the I2C bus.
    '''
    def __init__(self):
        super(I2CSenseHatAdaptor, self).__init__()
        self.config = ConfigUtil.ConfigUtil(ConfigConst.ConfigConst.DEFAULT_CONFIG_FILE_NAME)
        self.config.loadConfig()
        print('Configuration data...\n' + str(self.config))
        self.initI2CBus()
    
    '''
    This initializes I2C bus. write_quick is used for device check at each of
    the respective sensors addresses. Perform quick transaction. 
    Throws IOError if unsuccessful.
    '''
    def initI2CBus(self):
        print("Initializing I2C bus and enabling I2C addresses...")
        i2cBus.write_quick(accelAddr)
        i2cBus.write_quick(magAddr)
        i2cBus.write_quick(pressAddr)
        i2cBus.write_quick(humidAddr)
    
    '''
    Run method
    runs an infinite loop for a passed rate in seconds. 
    if flag is true four methods are called.
    '''
    def run(self):
        while True:
            if self.enableEmulator:
                print("\nSensor values: \n")
                self.displayAccelerometerData()
                self.displayMagnetometerData()
                self.displayPressureData()
                self.displayHumidityData()
            sleep(self.rateInSec)
    
    '''
    This stores the accl_data by reading a block of data from a given
    (accelerometer address, beginning address, total bytes to be read)
    '''
    def displayAccelerometerData(self):
        self.accl_data = i2cBus.read_i2c_block_data(accelAddr, begAddr, totBytes)
        print("Accelerometer value- "+ str(self.accl_data));#quick writes

    '''
    This stores the mag_data by reading a block of data from a given
    (magnetometer address, beginning address, total bytes to be read)
    '''
    def displayMagnetometerData(self):
        self.mag_data = i2cBus.read_i2c_block_data(magAddr, begAddr, totBytes)
        print("Magnetometer value- "+ str(self.mag_data));
    
    '''
    This stores the pres_data by reading a block of data from a given
    (pressure address, beginning address, total bytes to be read)
    '''
    def displayPressureData(self):
        self.pres_data = i2cBus.read_i2c_block_data(pressAddr, begAddr, totBytes)
        print("Pressure value- "+ str(self.pres_data));
    
    '''
    This stores the humid_data by reading a block of data from a given
    (humidity address, beginning address, total bytes to be read)
    '''
    def displayHumidityData(self):
        self.humid_data = i2cBus.read_i2c_block_data(humidAddr, begAddr, totBytes)
        print("Humidity value- "+ str(self.humid_data));
