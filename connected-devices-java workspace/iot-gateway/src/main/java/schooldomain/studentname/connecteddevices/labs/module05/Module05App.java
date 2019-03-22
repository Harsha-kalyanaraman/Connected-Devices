/**
 *Created on Feb 17, 2019
 *
 *@author hkalyan
 */
package schooldomain.studentname.connecteddevices.labs.module05;
import java.util.logging.Logger; 
import com.labbenchstudios.edu.connecteddevices.common.BaseDeviceApp;
import com.labbenchstudios.edu.connecteddevices.common.DeviceApplicationException;

/**
 *This is the main class which executes this app
 *
 */
public class Module05App extends BaseDeviceApp
{
	// static variable to print a simple logger
	private static final Logger _Logger =
		Logger.getLogger(Module05App.class.getSimpleName());
	
	/**
	 * main method
	 * 
	 * @param args accepts a string array of arguments 
	 * starts the app when called and stops the app
	 */
	public static void main(String[] args)
	{
		Module05App app = new Module05App();
		try {
			app.start();
			app.stop();
		} catch (DeviceApplicationException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	// private var's
	
	
	// constructors
	
	/**
	 * Default constructor of this class.
	 * 
	 */
	public Module05App()
	{
		super();
	}
	
	/**
	 * Constructor.
	 * 
	 * @param appName accepts an appName
	 */
	public Module05App(String appName)
	{
		super(appName);
	}
	
	/**
	 * Constructor.
	 * 
	 * @param appName accepts an appName
	 * @param args a string array of arguments 
	 */
	public Module05App(String appName, String[] args)
	{
		super(appName, args);
	}
	
	// protected methods
	
	/* (non-Javadoc)
	 * @see com.labbenchstudios.edu.connecteddevices.common.BaseDeviceApp#start()
	 * calls the TempManagementApp.demo() method to run the app
	 */
	@Override
	protected void start() throws DeviceApplicationException
	{
		_Logger.info("Hello - module05 here!");
		TempManagementApp.demo();
		
	}
	
	/* (non-Javadoc)
	 * @see com.labbenchstudios.edu.connecteddevices.common.BaseDeviceApp#stop()
	 */
	@Override
	protected void stop() throws DeviceApplicationException
	{
		_Logger.info("Stopping module05 app...");
	}
	
}
