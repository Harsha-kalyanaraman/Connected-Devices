package schooldomain.studentname.connecteddevices.labs.module07;

import java.net.InetAddress;
import java.net.InetSocketAddress;
import java.net.SocketException;

import org.eclipse.californium.core.CoapServer;
import org.eclipse.californium.core.network.CoapEndpoint;
import org.eclipse.californium.core.network.EndpointManager;

import com.labbenchstudios.edu.connecteddevices.common.ConfigConst;
import com.labbenchstudios.edu.connecteddevices.common.ConfigUtil;

/**
 * This class creates an instance of TempResourceHandler and initializes the Server
 * 
 * @author khars
 *
 */
public class CoapServerConnector extends CoapServer {
	private final int COAP_PORT;
	
	public CoapServerConnector(ConfigUtil config) throws SocketException {
		COAP_PORT = config.getIntegerProperty(ConfigConst.COAP_GATEWAY_SECTION, ConfigConst.PORT_KEY);
		
		
		//Add the endpoints and the server resources while initializing the server
		addEndpoints();
		
		add(new TempResourceHandler());		

		
	}
	
	/**
	 * This method combines CoAP server to the end-point
	 */
	private void addEndpoints()
	{
		for (InetAddress addr : EndpointManager.getEndpointManager().getNetworkInterfaces()) {
    		// only binds to localhost
			if (addr.isLoopbackAddress()) {
				InetSocketAddress bindToAddress = new InetSocketAddress(addr, COAP_PORT);
				addEndpoint(new CoapEndpoint(bindToAddress));
			}
		}
	}
}