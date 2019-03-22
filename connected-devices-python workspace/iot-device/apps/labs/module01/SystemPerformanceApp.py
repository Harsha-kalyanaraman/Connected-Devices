'''
Created on Jan 16, 2019

@author: Harsha vardhanram kalyanaraman
'''
from time import sleep#Importing sleep
from labs.module01 import SystemPerformanceAdaptor#importing systemPerformanceAdaptor class


s_adp_obj = SystemPerformanceAdaptor.SystemPerformanceAdaptor()#Creating an instance of the systemPerformanceAdaptor class
s_adp_obj.adaptorFlag()#calling the flag method to switch flag to ON
print("Status of the Thread before enabling as daemon thread:", s_adp_obj.daemon)#Since the ourThread is inherited from main thread it is not Daemon
s_adp_obj.daemon = True#Setting out thread to Daemon
print("Status of the Thread after enabling as daemon thread: ",s_adp_obj.daemon)#OurThread is set to Daemon
s_adp_obj.start()#Calling the run method using start method
print("Starting system performance app daemon thread...")
while True:#This infinite loop is written for the app to wait
    sleep(1)
    pass