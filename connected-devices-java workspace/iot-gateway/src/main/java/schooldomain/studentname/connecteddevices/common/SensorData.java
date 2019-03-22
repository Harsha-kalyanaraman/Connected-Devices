/**
 *Created on Feb 17, 2019
 *
 *@author hkalyan
 */
package schooldomain.studentname.connecteddevices.common;
/**
 * Class which stores Sensor variables of Raspberry pi
 */


import java.text.SimpleDateFormat;
import java.util.Date;

/**
 * @author Venkat Prasad Krishnamurthy
 *
 */
public class SensorData {
	private Double curVal;
	private Double maxVal;
	private Double minVal;
	private Double totVal;
	private Double diffVal;
	private Double avgVal;
	private String timeStamp;
	private Integer sampleCount = 0;
	private String name;
	
	/*
	 * Constructor to initialize a Sensor Data object
	 * @param maxVal = Maximum sensor Value
	 * @param minVal = Minimum sensor Value
	 * @param   time =  time
	 * @param   name =  sensor name
	 */
	
	public SensorData(Double maxVal, Double minVal, String time, String name) {
		super();
		this.maxVal = maxVal;
		this.minVal = minVal;
		this.totVal = 0.0;
		this.timeStamp = time;
		this.name = name;
	}
		
	public Integer getSampleCount() {
		return sampleCount;
	}

	public void setSampleCount(Integer sampleCount) {
		this.sampleCount = sampleCount;
	}

	public Double getAvgVal() {
		return avgVal;
	}

	public void setAvgVal(Double avgVal) {
		this.avgVal = avgVal;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public Double getCurVal() {
		return curVal;
	}
	public void setCurVal(Double curVal) {
		this.curVal = curVal;
	}
	public Double getMaxVal() {
		return maxVal;
	}
	public void setMaxVal(Double maxVal) {
		this.maxVal = maxVal;
	}
	public Double getMinVal() {
		return minVal;
	}
	public void setMinVal(Double minVal) {
		this.minVal = minVal;
	}
	public Double getTotVal() {
		return totVal;
	}
	public void setTotVal(Double totVal) {
		this.totVal = totVal;
	}
	public Double getDiffVal() {
		return diffVal;
	}
	public void setDiffVal(Double diffVal) {
		this.diffVal = diffVal;
	}
	public String getTime() {
		return this.timeStamp;
	}
	public void setTime(String time) {
		this.timeStamp = time;
	}
	
	/*
	 * (non-Javadoc)
	 * @see java.lang.Object#toString()
	 * function to present the object in customized human readable form
	 */
	@Override
	public String toString()
	{
		String str = "Current Value: "+this.getCurVal()+"\nTime: "+this.getTime()+"\nAverage Value: "+this.getAvgVal()+"\nMinimum Value: "+this.getMinVal()+"\nMaximum Value: "+this.getMaxVal();
		return str;
		
	}
	
	/*
	 * Updates the timestamp to current time
	 */
	public void updateTimeStamp() {
		this.timeStamp = new SimpleDateFormat("yyyy.MM.dd HH:mm.ss").format(new Date());
	}
	
	/*
	 * Function adds current value to calculate average value
	 * @param val - Current sensor value
	 */
	public void updateValue(float val) {
		updateTimeStamp();
		++this.sampleCount;
		this.curVal = (double) val;
		this.totVal += val;
		if (this.curVal < this.minVal) {
			this.minVal = this.curVal;
		}
		if (this.curVal > this.maxVal) {
			this.maxVal = this.curVal;
		}
		if (this.totVal != 0 && this.sampleCount > 0) {
			this.avgVal = this.totVal / this.sampleCount;
		}
	}
	
}
