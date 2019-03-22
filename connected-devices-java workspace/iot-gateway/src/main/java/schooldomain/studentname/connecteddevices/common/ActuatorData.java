/**
 *Created on Feb 16, 2019
 *
 *@author hkalyan
 */
package schooldomain.studentname.connecteddevices.common;

/**
*This class is used for setting the various parameter of the actuator
*and return the compiled output data in a string format
*/
public class ActuatorData {
	private String time;
	private String name;
	private boolean hasError = false;
	private int command = 0;
	private int errCode = 0;
	private int statusCode = 0;
	private  String stateData;
	private double val = 0.0;
	private int sampleCount = 0;
	
	/**
	 *Constructor for ActuatorData.
	 *
     *@param name The name of the data which is compiled.
     *@param time The time at which the data is generated
     *@param val The val that is passed to trigger an event
     *@param sampleCount The counter which keeps adding 
	 */
	public ActuatorData(String time, String name, double val, int sampleCount) {
		super();
		this.time = time;
		this.name = name;
		this.val = val;
		this.sampleCount = sampleCount;
	}

	/**
	 *Getters and setters of this class variables
	 */
	public String getTime() {
		return time;
	}


	public void setTime(String time) {
		this.time = time;
	}


	public String getName() {
		return name;
	}


	public void setName(String name) {
		this.name = name;
	}


	public boolean isHasError() {
		return hasError;
	}


	public void setHasError(boolean hasError) {
		this.hasError = hasError;
	}


	public int getCommand() {
		return command;
	}


	public void setCommand(int command) {
		this.command = command;
	}


	public int getErrCode() {
		return errCode;
	}


	public void setErrCode(int errCode) {
		this.errCode = errCode;
	}


	public int getStatusCode() {
		return statusCode;
	}


	public void setStatusCode(int statusCode) {
		this.statusCode = statusCode;
	}


	public String getStateData() {
		return stateData;
	}


	public void setStateData(String stateData) {
		this.stateData = stateData;
	}


	public double getVal() {
		return val;
	}


	public void setVal(double val) {
		this.val = val;
	}


	public int getSampleCount() {
		return sampleCount;
	}


	public void setSampleCount(int sampleCount) {
		this.sampleCount = sampleCount;
	}

	/**
	 *This method will return the string representation of the object
	 *
	 *@return str This is the string representation of the object of class ActuatorData
	 */
	@Override
	public String toString() {
		return "ActuatorData [time=" + this.getTime() + ", name=" + this.getName() + ", val=" + this.getVal() + ", sampleCount=" + this.getSampleCount() + "]";
	}
	
	/**
	 *This will increase the sampleCount value by 1
	 */
	public void addValue()
	{
		this.setSampleCount(this.getSampleCount()+1);
		
	}
}
