/**
 *Created on Feb 17, 2019
 *
 *@author hkalyan
 */
package schooldomain.studentname.connecteddevices.labs.module05;
import java.io.*;

/**
 *This class is where file transactions take place.
 *uses File io library FileReader method to read the JSON file
 *uses File io library FileWriter method to write Json data to a file
 */
public class FileTransaction {
	
	/**
	 *uses File io library FileReader method to read the JSON file
	 *Uses error handling by encapsulating in a try-catch block
	 *Reads each data from the passed file and stores in a String JSON
	 *
	 *@param file The name of the file that is passed to read Json data from
	 *@return Returns the json string
	 */
	public static String FileReader(String file)
	{
		String json = new String();
		try
		{
			FileReader fr = new FileReader(file);
			int ch;
			while((ch=fr.read())!=-1)
			{
				json = json + (char)ch;
			}
			fr.close();
		}
		catch(Exception e)
		{
			e.printStackTrace();
		}
		return json;
	}
	
	/**
	 *uses File io library FileWriter method to read the JSON file
	 *Uses error handling by encapsulating in a try-catch block
	 *Writes the passed JSON data to the passed file
	 *
	 *@param file The name of the file that is passed to write Json data
	 *@param fileWriteEnable A flag that is set to write data
	 *@param json The json data that is to be written to the file
	 */
	public static void fileWrite(String fileWriteEnable, String file, String json)
	{
		File jsonFile = new File(file);
		
		try {
			jsonFile.createNewFile();//Creates a new file
			FileWriter writer = new FileWriter(jsonFile);
			writer.write(json);//writes the data into the passed file
			writer.flush();//flushes the stream
			writer.close();//Closes the stream after flushing it
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		
		
	}

}
