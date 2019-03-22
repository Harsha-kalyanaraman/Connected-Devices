'''
Created on Mar 7, 2019

@author: khars
'''
from labs.module07.CoapClientConnector import CoapClientConnector
from labs.common.SensorData import SensorData
from labs.common.DataUtil import DataUtil
from coapthon.messages import request
from labs.common.ConfigUtil import ConfigUtil
from labs.common import ConfigConst

config = ConfigUtil('../../../config/ConnectedDevicesConfig.props')
config.loadConfig()
data = DataUtil()
host = config.getProperty(ConfigConst.ConfigConst.COAP_DEVICE_SECTION, ConfigConst.ConfigConst.HOST_KEY)
port = int(config.getProperty(ConfigConst.ConfigConst.COAP_DEVICE_SECTION, ConfigConst.ConfigConst.PORT_KEY))
path = 'temperature'
sensor = SensorData("Temperature",0.0,20.0)
sensor.addValue(3.0)
print(str(sensor))
coapClient = CoapClientConnector(host, port, path)
coapClient.ping()
json_data = data.SensorDataToJson(sensor)
print("json"+json_data)
#coapClient.get() #Get will respond with NOT_FOUND since data object on server is not initialized
coapClient.post((json_data)) #Post JSON to server
coapClient.get()
sensor.addValue(4.00)
coapClient.put(data.SensorDataToJson(sensor)) #Update resource on the server
coapClient.get()
coapClient.delete() #Delete resource
coapClient.get()
coapClient.stop()