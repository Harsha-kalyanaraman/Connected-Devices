'''
Created on Mar 7, 2019

@author: khars
'''
from coapthon.client.helperclient import HelperClient
from coapthon.messages import request
'''
This is a helper class that connects to the CoAP server
'''
class CoapClientConnector():
    
    '''
    Constructor of this class
        @param host:  (str) - IP address of the server
        @param port:  (int) - Port number to connect to
        @param path:  (str) - Resource URI
    '''
    def __init__(self, host, port, path):
        self.host = host
        self.port = port
        self.path = path
        self.client = HelperClient(server=(host, port))
        
    '''
    Wrapper method to ping the server
    '''
    def ping(self):
        self.client.send_empty("")
    
    '''
    Wrapper method for the GET action
    ''' 
    def get(self):
        response = self.client.get(self.path)
        print(response.pretty_print())
      
    '''
    Wrapper method for the POST action
    @param jsonData: (str) - Request payload in JSON format
    '''
    def post(self,jsonData):
        response  = self.client.post(self.path, jsonData)
        print(response.pretty_print())
    
    '''
    Wrapper method for the PUT action
    @param jsonData: (str) - Request payload in JSON format
    '''
    def put(self, jsonData):
        response = self.client.put(self.path, jsonData)
        print(response.pretty_print())
    
    '''
    Wrapper method for the DELETE action
    '''
    def delete(self):
        response = self.client.delete(self.path)
        print(response.pretty_print())
    
    '''
    This method stops the client thread
    ''' 
    def stop(self):
        self.client.stop()     