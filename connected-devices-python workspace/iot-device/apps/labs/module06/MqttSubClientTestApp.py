'''
Created on Mar 2, 2019

@author: khars
'''

'''
This App consists of instance of MqttClientConnector and Subscribes to a topic and
retrieves published message so its a MQTT Subscriber Client
'''
from labs.common import ConfigConst
from labs.common.ConfigUtil import ConfigUtil
from labs.module06.MqttClientConnector import MqttClientConnector
from labs.common.DataUtil import DataUtil
import logging

'''
Setting values for Topic and address for MQTT broker
'''
topic = "Temperature Sensor"
config = ConfigUtil('../../../config/ConnectedDevicesConfig.props');
host = config.getProperty(ConfigConst.ConfigConst.MQTT_CLOUD_SECTION, ConfigConst.ConfigConst.HOST_KEY)
subscribe = MqttClientConnector(topic)
subscribe.subscribe(host)                  # Connecting to MQTT Broker
msg = subscribe.message()                  # Subscribing to specefied Topic
logging.debug('JSon Data Received:')
print("Json Data Received:\n "+str(msg)+"\n")
data = DataUtil();
sensor = data.jsonToSensorData(msg)        # Converting Json data to Sensor Data
logging.debug('Json data converted into SensorData')
print("Received message in SensorData format"+str(sensor))
json = data.SensorDataToJson(sensor)
logging.debug('SensorData converted into Json Data: ')
print('SensorData converted to Json Data again: \n'+str(json))
