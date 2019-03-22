'''
Created on Mar 7, 2019

@author: khars
'''

from labs.common.SensorData import SensorData
from coapthon.resources.resource import Resource
import coapthon.defines as defines

class TempResourceHandler(Resource):
    '''
    classdocs
    '''
    
    '''
    CoAP resource for storing temperature data
    '''
    def __init__(self, config, name="TemperatureResource", coap_server=None):
        super(TempResourceHandler, self).__init__(name, coap_server)
        self.config = config
        self.sensorData = None
    
    def render_GET_advanced(self, request, response):
        '''
        This method responds to a GET request on the resource
        
        Parameters:
            request - CoAP request
            response - CoAP response to be sent
            
        Returns:
            response - CoAP response
        '''
        
        if(self.sensorData == None):
            response.code = defines.Codes.NOT_FOUND.number
            response.payload = (defines.Content_types["text/plain"], "Object needs to be initialized")
        else:
            response.code = defines.Codes.CONTENT.number
            response.payload = (defines.Content_types["application/json"], self.sensorData.toJson(False)) #Response payload is SensorData in JSON format    
            
        return self, response
                
                
    def render_POST_advanced(self, request, response):
        '''
        This method responds to a POST request on the resource
        
        Parameters:
            request - CoAP request
            response - CoAP response to be sent
            
        Returns:
            response - CoAP response
        '''
            
        if(self.sensorData != None):
            response.code = defines.Codes.BAD_REQUEST.number
            response.payload = (defines.Content_types["text/plain"], "Object already exists")
        else:
            jsonData = request.payload
            self.sensorData = SensorData(self.config)
            self.sensorData.fromJson(False, jsonData) #Initialize a new SensorData object form the request payload
                
            response.code = defines.Codes.CREATED.number
            response.payload = (defines.Content_types["text/plain"], "Object created successfully")    
            
        return self, response
        
    def render_PUT_advanced(self, request, response):
        '''
        This method responds to a PUT request on the resource
        
        Parameters:
            request - CoAP request
            response - CoAP response to be sent
            
        Returns:
            response - CoAP response
        '''
        
        if(self.sensorData == None):
            response.code = defines.Codes.BAD_REQUEST.number
            response.payload = (defines.Content_types["text/plain"], "Object needs to be initialized")
        else:
            jsonData = request.payload
            self.sensorData.fromJson(False, jsonData) #Update resource data with JSON data received in request paylaod
                
            response.code = defines.Codes.CHANGED.number
            response.payload = (defines.Content_types["text/plain"], "Object changed successfully")    
            
        return self, response
        
    def render_DELETE_advanced(self, request, response):
        '''
        This method responds to a PUT request on the resource
        
        Parameters:
            request - CoAP request
            response - CoAP response to be sent
            
        Returns:
            response - CoAP response
        '''
        
        if(self.sensorData == None):
            response.code = defines.Codes.BAD_REQUEST.number
            response.payload = (defines.Content_types["text/plain"], "Object already deleted")
        else:
            self.sensorData = None # Set SensorData object to null
                
            response.code = defines.Codes.DELETED.number
            response.payload = (defines.Content_types["text/plain"], "Object deleted successfully")    
            
        return self, response 


    
    
    