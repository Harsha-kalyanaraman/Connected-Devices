'''
Created on Jan 16, 2019

@author: Harsha vardhanram kalyanaraman
'''

import psutil ,datetime #importing psutil library
from time import sleep# importing to get sleep function
from threading import Thread #importing thread to start a new thread


class SystemPerformanceAdaptor(Thread):#This class implements a child thread
    '''
    classdocs
    '''
    def __init__(self):# Initializing parameterized Constructor 
        Thread.__init__(self)
        self.adaptor = False#Setting a flag adaptor off
        
    

    def run(self):#Overriding run method of the main class
        while self.adaptor:#making adaptor flag on
           
            print('\n--------------------')
            battery_remaining = psutil.sensors_battery().percent #assigning battery remaining data obtained from psutil library to battery_remaining variable
            SecondsRemainingInCharge = psutil.sensors_battery().secsleft#assigning remaining charge data obtained from psutil library to SecondsRemainingInCharge variable
            IsPowerPlugged = psutil.sensors_battery().power_plugged#assigning power plugged boolean data obtained from psutil library to IsPowerPlugged variable
            print('\n--------------------')
            print('System Performance App\n')
            print('Battery Details:\n')
            print("Remaining Charge : %s%% \nSeconds Remaining: %s \nIs Power Plugged : %s"%(battery_remaining, SecondsRemainingInCharge, IsPowerPlugged))#Printing Battery details to screen
            print('\nBoot Time:\n')
            BootTime = psutil.boot_time()#assigning boot time data in seconds obtained from psutil library to BootTime variable
            print("Boot time : %2d seconds"%BootTime) #Printing boot time to screen
            print(datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("Time stamp :%Y-%m-%d %H:%M:%S"))#attaching timestamp to the boot time in years/months/days hours/minutes/seconds
            sleep(5)#sleep haults the process 
      
    def adaptorFlag(self):#Creating an adaptorFlag method to call from the app
        self.adaptor = True#setting adaptor flag as true