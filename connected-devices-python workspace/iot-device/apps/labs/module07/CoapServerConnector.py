'''
Created on Mar 7, 2019

@author: khars
'''

import getopt
import sys
from coapthon.server.coap import CoAP
from coapthon.server.coap import CoAP
from labs.module07.TempResourceHandler import TempResourceHandler
from coapthon.resources.resource import Resource
from labs.common.ConfigUtil import ConfigUtil
from labs.common import ConfigConst

client = None
'''

'''
class CoapServerConnector(CoAP):
    '''
    classdocs
    '''

    def __init__(self,host,port,config):
        '''
        Constructor
        '''
        CoAP.__init__(self, (host, port))
        self.add_resource("temperature/", TempResourceHandler(config = config)) #Add Temperature resource while initializing server
        
    
    def start(self):
        try:
            print("Starting Server...")
            self.listen(10)
        except KeyboardInterrupt:
            print("Server Shutdown")
            self.close()
            print("Exiting...")
        finally:
            self.close()
            
        