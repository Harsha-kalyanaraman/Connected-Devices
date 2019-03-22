'''
Created on Mar 2, 2019

@author: khars
'''

'''
This App consists of instance of MqttClientConnector and publishes message so its
a MQTT Publisher Client
'''
from labs.common import ConfigConst
from labs.common.ConfigUtil import ConfigUtil
from labs.module06.MqttClientConnector import MqttClientConnector
from labs.common.SensorData import SensorData
from labs.common.DataUtil import DataUtil
import logging
from random import uniform
from datetime import datetime

topic = "Temperature Sensor"
config = ConfigUtil('../../../config/ConnectedDevicesConfig.props');
host = config.getProperty(ConfigConst.ConfigConst.MQTT_CLOUD_SECTION, ConfigConst.ConfigConst.HOST_KEY)

'''
Creating Sensor Data
'''
sensor = SensorData(topic,10,30)
sensor.curValue = uniform(float(sensor.getMinValue()), float(sensor.getMaxValue())); 
sensor.addValue(sensor.curValue);
sensor.diffValue = sensor.curValue - sensor.avgValue;
sensor.timestamp = datetime.now();
logging.info('SensorData to be sent:')
print("Sensor Value before converting to Json: "+str(sensor));

'''
Converting SensorData to json format
'''
data = DataUtil()#creating DataUtil instance
json_data = data.SensorDataToJson(sensor);
logging.info('SensorData converted into Json:')
print("SensorData in Json Format before publishing"+str(json_data)+"\n")
pub_client = MqttClientConnector();#creating MqttClientConnector Instance

'''
Function is used to publish the Json to the MQTT broker through MQTT ClientConnector

@param topic:Topic of message
@param json_data: Json Payload
@param host: address of MQTT broker 
'''
pub_client.publish(topic,json_data,host)