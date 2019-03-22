'''
Created on Mar 7, 2019

@author: khars
'''

from labs.module07.CoapServerConnector import CoapServerConnector
from labs.common.ConfigUtil import ConfigUtil
from labs.common import ConfigConst

config = ConfigUtil('../../../config/ConnectedDevicesConfig.props')
config.loadConfig()
host = config.getProperty(ConfigConst.ConfigConst.COAP_DEVICE_SECTION, ConfigConst.ConfigConst.HOST_KEY)
port = int(config.getProperty(ConfigConst.ConfigConst.COAP_DEVICE_SECTION, ConfigConst.ConfigConst.PORT_KEY))
server = CoapServerConnector(host,port,config)
server.start()