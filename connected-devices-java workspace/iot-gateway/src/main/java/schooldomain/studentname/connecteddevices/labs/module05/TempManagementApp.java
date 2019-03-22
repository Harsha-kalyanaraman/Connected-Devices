/**
 *Created on Feb 17, 2019
 *
 *@author hkalyan
 */
package schooldomain.studentname.connecteddevices.labs.module05;
import java.io.FileNotFoundException; 
import com.google.gson.Gson;

import schooldomain.studentname.connecteddevices.common.DataUtil;
import schooldomain.studentname.connecteddevices.common.SensorData;

import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Iterator;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

/**
 * This class creates an instance of DataUtil class where json file is passed and
 * printed to console
 */
public class TempManagementApp {

	/**
	 * This method is static to be called by module05 App
	 * creates an instance of DataUtil class where json file is passed and
	 * printed to console
	 */
	public static void demo()
	{
		DataUtil sensor = new DataUtil();
		SensorData sen = sensor.JsonToSensorData(null, "G:\\Test2\\workspace\\iot-device\\apps\\labs\\module05\\sensordata.txt");
		System.out.println(sen);
	}
}

