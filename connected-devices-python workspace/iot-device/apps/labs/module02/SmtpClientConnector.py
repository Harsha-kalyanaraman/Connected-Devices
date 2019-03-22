'''
Created on Jan 25, 2019

@author: hkalyan
'''

from labs.common import ConfigUtil
from labs.common import ConfigConst
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

'''
This is the bridge which passes data from app to cloud based e-mail account
'''
class SmtpClientConnector(object):
   
    '''
    Constructor for SmtpClientConnector.
    Calls a method for the configuration file to load.
    Creates an instance of ConfigUtil class
    '''
    def __init__(self):
        self.config = ConfigUtil.ConfigUtil('../../../config/ConnectedDevicesConfig.props')
        self.config.loadConfig()
        print('Configuration data...\n' + str(self.config))

    '''
    This method simply publishes a message to cloud based E-mail
    
    @param topic: Is the subject of the mail to be passed.
    @param data: Is the Body of the message which is to be passed here it is sensor data  
    '''
    def publishMessage(self, topic, data):
        
        '''
        This method assigns all the attributes of the alert mail obtained from the
        imported files.
        '''
        host = self.config.getProperty(ConfigConst.ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.ConfigConst.HOST_KEY)
        port = self.config.getProperty(ConfigConst.ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.ConfigConst.PORT_KEY)
        fromAddr = self.config.getProperty(ConfigConst.ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.ConfigConst.FROM_ADDRESS_KEY)
        toAddr = self.config.getProperty(ConfigConst.ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.ConfigConst.TO_ADDRESS_KEY)
        authToken = self.config.getProperty(ConfigConst.ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.ConfigConst.USER_AUTH_TOKEN_KEY)
        msg = MIMEMultipart()
        msg['From'] = fromAddr
        msg['To'] = toAddr
        msg['Subject'] = topic
        msgBody = str(data)
        msg.attach(MIMEText(msgBody))
        msgText = msg.as_string()
       
        '''
        Then tries to contact the cloud based E-mail by starting a connection using
        SSL ,initiates SMTP conversation(EHLO) and after authentication sends the
        mail to the to address.
        '''
        try:  
            smtpServer = smtplib.SMTP_SSL(host, port);
            smtpServer.ehlo();
            smtpServer.login(fromAddr, authToken);
            smtpServer.sendmail(fromAddr, toAddr, msgText);
            smtpServer.close();
        
            ''' 
            if it fails executes execute sends error message.
            '''   
        except:
            print("Error in Sending Mail");
            

        
        
        