'''
Created on Mar 2, 2019

@author: khars
'''
'''
This class has methods defined for both MQTT Publisher and subscriber
'''
import paho.mqtt.client as mqtt    #import client library
import time

class MqttClientConnector():
    host = "test.mosquitto.org"
    json_data = "Hello"
    
    '''
    This method is called when a subscriber connects to a publisher. This is a
    call back funtion which is executed when an internal on connect method is called
    
    @param client: Instance of client
    @param userdata : Private userdata of client
    @param flags: Response flag sent by the MQTT broker
    @param rc : Response code 0 for succesful connection
    '''
    def on_connect(self,client,userdata,flags,rc):
        print("Connected with Client: "+str(rc))
        client.subscribe(self.topic,2)
    
    '''
    This function will execute once the client receives message
    from MQTT Broker. This is a call back funtion which is executed when an 
    internal on message method is called which will again invoke the below defined
    method
    
    @param client: Instance of client
    @param userdata : Private userdata of client
    @param msg : Subcribed message
    ''' 
    def on_message(self,client,userdata,msg):
        global json_data
        json_data = str(msg.payload.decode("utf-8"))
        client.loop_stop()
    
    '''
    Constructor
    
    @param topic:topic of the message published or subscribed 
    ''' 
    def __init__(self,topic=None):
        self.topic = topic;
        
    '''
    This function is used for publishing the message
    An instance of mqtt paho client is created and connect and publish methods 
    are called
    
    @param topic: Topic of the message
    @param message: Message to be sent
    @param host: address of MQTT broker   
    '''
    def publish(self,topic,message,host):
        client = mqtt.Client();
        client.connect(host,1883)
        client.publish(topic,message)
        
    '''
    Function is used to subscribe to a topic
    An instance of mqtt paho client is created and connect and publish methods 
    are called and a infinite loop is started
    
    @param host: Address of MQTT broker 
    '''
    def subscribe(self,host):
        client = mqtt.Client()
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        client.connect(host,1883,60)
        client.loop_start()
        time.sleep(10)
    
    '''
    Function is used to store the data received from MQTT Broker
    
    @return: Data received from MQTT Broker
    '''
    def message(self):
        global json_data
        return json_data        
        