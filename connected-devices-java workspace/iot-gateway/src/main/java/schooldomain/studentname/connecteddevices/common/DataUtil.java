/**
 *Created on Feb 17, 2019
 *
 *@author hkalyan
 */
package schooldomain.studentname.connecteddevices.common;
import com.google.gson.Gson; 
import schooldomain.studentname.connecteddevices.labs.module05.FileTransaction;

/**
*This class is used for converting the object data to JSON format and vice versa
*/
public class DataUtil {
	
	/**
	*This method is used for converting sensorData object to JSON format
	*
	*@param sensordata The SensorData object which is passed to be converted to 
	*JSON format
	*@return Returns the converted json output
	*/
	public String SensorDataToJson(SensorData sensordata)
	{
		String jsonSd;
		Gson gson = new Gson();
		jsonSd = gson.toJson(sensordata);
		return jsonSd;
	}
	
	/**
	*This method is used for converting JSON format to sensorData object 
	*
	*@param jsondata The jsondata which is passed to be converted to 
	*object
	*@param filename The name of the file from which JSON data is obtained
	*@return Returns the sensorData object
	*/
	public SensorData JsonToSensorData(String jsondata,String filename)
	{
		SensorData sensorData=null;
		if(filename==null)//passing the json directly from the class
		{
			Gson gson = new Gson();
			sensorData = gson.fromJson(jsondata, SensorData.class);
			return sensorData;
		}
		else//passing json data from a file
		{
			Gson gson = new Gson();
			String data = FileTransaction.FileReader(filename);
			sensorData = gson.fromJson(data, SensorData.class);
			return sensorData;
			
		}
	}
}