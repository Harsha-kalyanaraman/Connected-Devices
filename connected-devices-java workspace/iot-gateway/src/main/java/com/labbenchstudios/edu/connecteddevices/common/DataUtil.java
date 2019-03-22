package com.labbenchstudios.edu.connecteddevices.common;

import com.google.gson.Gson; //using goolgle gson library for json format conversion
import schooldomain.studentname.connecteddevices.labs.module05.FileTransaction;


/*
 * This Class is used for conversion of json data to object 
 * and vice versa
 */
public class DataUtil {
	
	/*
	 * This method is used to convert Sensor data to json
	 * 
	 * @param sensordata = SensorData Object
	 */
	public String SensorDataToJson(SensorData sensordata)
	{
		String jsonSd;
		Gson gson = new Gson();
		jsonSd = gson.toJson(sensordata);
		return jsonSd;
	}
	
	/*
	 * This method is used to convert json to Sensor data
	 * 
	 * @param      jsondata = json object to convert into SensorData Object
	 * @param      filename = file where json data is present
	 * @return   sensorData = SensorData Object
	 */
	public SensorData JsonToSensorData(String jsondata,String filename)
	{
		SensorData sensorData=null;
		if(filename==null)
		{
			
			Gson gson = new Gson();
			sensorData = gson.fromJson(jsondata, SensorData.class);
			return sensorData;
		}
		else
		{
			Gson gson = new Gson();
			String data = FileTransaction.FileReader(filename);
			System.out.println("Sensor Data in Json Format:");
			System.out.println(data+"\n");
			System.out.println("SensorData After converting: ");
			sensorData = gson.fromJson(data, SensorData.class);
			return sensorData;
			
		}
			
	}

}