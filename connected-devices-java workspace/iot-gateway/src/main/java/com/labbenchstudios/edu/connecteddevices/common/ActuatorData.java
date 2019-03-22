package com.labbenchstudios.edu.connecteddevices.common;

import java.text.SimpleDateFormat;
import java.util.Date;

/**
 * @author khars
 * 
 * ActuatorData - class defines the ActuatorData object of Actuator
 */
public class ActuatorData {

	// Command, Status and Error case type definition
	public static final int COMMAND_OFF = 0;
	public static final int COMMAND_ON = 1;
	public static final int COMMAND_SET = 2;
	public static final int COMMAND_RESET = 3;
	public static final int STATUS_IDLE = 0;
	public static final int STATUS_ACTIVE = 1;
	public static final int ERROR_OK = 0;
	public static final int ERROR_COMMAND_FAILED = 1;
	public static final int ERROR_NON_RESPONSIBLE = -1;

	/**
	 * 
	 * @param timeStamp: date , time stamp
	 * @param name: name of actuator data
	 * @param hasError: boolean to check error
	 * @param command: type of command
	 * @param errCode: type of error
	 * @param statusCode: type of status
	 * @param stateData: data of the ActuatorData's state
	 * @param val: ActuatorData value
	 */

	private String name = "Actuator Data";
	private String timeStamp = null;
	private boolean hasError = false;
	private int command = 0;
	private int errCode = 0;
	private int statusCode = 0;
	private String stateData = null;
	private float val = 0.0f;

	/**
	 * ActuatorData constructor.
	 */
	public ActuatorData() {
		super();
		updateTimeStamp();
	}

	/**
	 * method updates the date and time.
	 */
	private void updateTimeStamp() {
		timeStamp = new SimpleDateFormat("yyyy.MM.dd HH:mm.ss").format(new Date());
	}

	/**
	 * Returns the name Actuator data
	 * 
	 * @return: The name of the Actuator data
	 */
	public String getName() {
		return name;
	}

	/**
	 * method to override the previous value stored in the container name
	 * 
	 * @param name: String
	 */
	public void setName(String name) {
		this.name = name;
	}

	/**
	 * method to return the date and time
	 * 
	 * @return 'timeStamp', String in yyyy.MM.dd HH:mm.ss
	 */
	public String getTimeStamp() {
		return timeStamp;
	}

	/**
	 * method to override the values stored in the container date and time
	 * 
	 * @param timeStamp: String of Date and time in yyyy.MM.dd HH:mm.ss
	 */
	public void setTimeStamp(String timeStamp) {
		this.timeStamp = timeStamp;
	}

	/**
	 * method to check error boolean
	 * 
	 * @return: 'hasError', true if ActuatorData has error else false
	 */
	public boolean isHasError() {
		return hasError;
	}

	/**
	 * method to override the values stored in the container hasError
	 * 
	 * @param hasError: boolean value
	 */
	public void setHasError(boolean hasError) {
		this.hasError = hasError;
	}

	/**
	 * method which returns the command type
	 * 
	 * @return: 'command',0 - OFF, 1 - ON, 2 - SET, 3 - RESET command type
	 */
	public int getCommand() {
		return command;
	}

	/**
	 * method which overrides the value of container command type
	 * 
	 * @param command: 0 - OFF, 1 - ON, 2 - SET, 3 - RESET command type
	 */
	public void setCommand(int command) {
		this.command = command;
	}

	/**
	 * method to return error code type
	 * 
	 * @return: 'errCode', 0 - Okay, 1 - failed, -1 - not responsive
	 */
	public int getErrCode() {
		return errCode;
	}

	/**
	 * method which overrides the value of container error code type
	 * 
	 * @param 'errCode': 0 - Okay, 1 - failed, -1 - not responsive
	 */
	public void setErrCode(int errCode) {
		this.errCode = errCode;
	}

	/**
	 * method which returns the status type
	 * 
	 * @return: 'statusCode', 0 for Idle else 1 for Active
	 */
	public int getStatusCode() {
		return statusCode;
	}

	/**
	 * method which overrides the value of the container status type
	 * 
	 * @param statusCode: 0 for Idle else 1 for Active
	 */
	public void setStatusCode(int statusCode) {
		this.statusCode = statusCode;
	}

	/**
	 * method which returns the data of the ActuatorData's state
	 * 
	 * @return: 'stateData',String
	 */
	public String getStateData() {
		return stateData;
	}

	/**
	 * method which overrides the data of the ActuatorData's state
	 * 
	 * @param stateData: String data
	 */
	public void setStateData(String stateData) {
		this.stateData = stateData;
	}

	/**
	 * method returns ActuatorData value
	 * 
	 * @return: 'val', float
	 */
	public float getVal() {
		return val;
	}

	/**
	 * method which overrides the value stored in ActuatorData value
	 * 
	 * @param val: float
	 */
	public void setVal(float val) {
		this.val = val;
	}

	/**
	 * method to update the ActuatorData
	 * 
	 * @param data: ActuatorData
	 */
	public void updateData(ActuatorData data) {
		this.command = data.getCommand();
		this.statusCode = data.getStatusCode();
		this.errCode = data.getErrCode();
		this.stateData = data.getStateData();
		this.val = data.getVal();
	}

	/**
	 * returns ActuatorData object to string representation.
	 * 
	 * @return: 'st' - ActuatorData object in string.
	 */
	public String toString() {
		String st;
		st = ("Name: " + name + "\n" + "time: " + timeStamp + "\n" + "Command: " + command + "\n" + "Status Code: "
				+ statusCode + "\n" + "Error Code: " + errCode + "\n" + "State Data: " + stateData + "\n" + "Value: "
				+ val + "\n");
		return st;
	}

}

