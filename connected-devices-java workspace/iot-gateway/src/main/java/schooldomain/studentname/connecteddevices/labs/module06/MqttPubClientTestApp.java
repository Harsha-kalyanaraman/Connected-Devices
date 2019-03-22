package schooldomain.studentname.connecteddevices.labs.module06;

import java.util.logging.Logger; 

/*
 * This Class is used to Publish Message to MQTT Broker  
 * 
 * @author - khars
 */

import schooldomain.studentname.connecteddevices.common.DataUtil;
import schooldomain.studentname.connecteddevices.common.SensorData;

public class MqttPubClientTestApp {
	
	private static final Logger logger = Logger.getLogger(MqttPubClientTestApp.class.getName());
	private static MqttPubClientTestApp SubApp;
	private MqttClientConnector mqttClient;
	public SensorData sensorData;
	public DataUtil dataUtil;

	public MqttPubClientTestApp() {
		super();
	}
	
	/*This method is used to create Json data from SensorData
	 * 
	 * @param sensorData: variable of type SensorData
	 * @return: Json object
	 */
	public String createJSON(SensorData sensorData) {
		dataUtil = new DataUtil();
		SensorData data = setSensorData(sensorData);
		logger.info("SensorData before converting into Json\n");
		System.out.println(data+"\n");
		String SJobj = dataUtil.SensorDataToJson(data);
		return SJobj;
	}
	
	/*
	 * This method is used to intialize or update the SensorData
	 * 
	 * @param sensorData: variable of SensorData Class
	 * @return: Update SensorData variable
	 */
	public SensorData setSensorData(SensorData sensorData) {
		sensorData.setName("Temperature Sensor");
		sensorData.updateTimeStamp();
		sensorData.setCurVal((double)10.23);
		sensorData.setAvgVal((double)30.23);
		sensorData.setSampleCount(5);
		sensorData.setMinVal((double)10);
		sensorData.setMaxVal((double)35);
		
		return sensorData;
		
	}
	
	/*
	 * method used to initialize publish action
	 * 
	 * @param topicName: Topic of the message
	 */
	public void start(String topicName)
	{
		mqttClient = new MqttClientConnector();
		sensorData = new SensorData(30.0,0.0,"name","Temperature");
		mqttClient.connect();
		String sensor = createJSON(sensorData);
		logger.info("SensorData after converting into Json\n");
		System.out.println(sensor+"\n");
		mqttClient.publishMessage(topicName, 2 , sensor.getBytes());
	}
	
	public static void main(String[] args) {

		SubApp = new MqttPubClientTestApp();
		String topic = "Temperature Sensor";
		try {
			SubApp.start(topic);
		}catch (Exception ex) {
			ex.printStackTrace();
		}
	}

}
