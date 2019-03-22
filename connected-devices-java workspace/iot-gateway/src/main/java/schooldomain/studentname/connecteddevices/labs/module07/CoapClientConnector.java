package schooldomain.studentname.connecteddevices.labs.module07;
import org.eclipse.californium.core.CoapClient;
import org.eclipse.californium.core.CoapResponse;
import org.eclipse.californium.core.coap.MediaTypeRegistry;

/**
 * This class connects to the CoAP server
 * 
 * @author khars
 */
public class CoapClientConnector {
	private CoapClient client;
	private String serverUri;
	public CoapClientConnector(String serverUri)
	{
		this.serverUri = serverUri;
		client = new CoapClient(this.serverUri);
	}
	
	/**
	 * The method pings the CoAP server and waits for a reply
	 */
	public void ping()	
	{
		if(!client.ping(2000))
		{
			System.out.println(this.serverUri + " doesn't respond to ping, exiting...");
			System.exit(-1);
		}
		else
		{
			System.out.println(this.serverUri + " responds to ping");
		}
	}
	
	/**
	 * Get Method
	 */
	public void get()
	{
		printResponse(client.get());
	}
	
	/**
	 * Post Method
	 * 
	 * @param jsonData JSON data to be posted to server
	 */
	public void post(String jsonData)
	{		
		printResponse(client.post(jsonData, MediaTypeRegistry.APPLICATION_JSON));
	}
	
	/**
	 * Put method
	 * 
	 * @param jsonData JSON data to be posted to server
	 */
	public void put(String jsonData)
	{		
		printResponse(client.put(jsonData, MediaTypeRegistry.APPLICATION_JSON));
	}
	
	/**
	 * Delete method
	 */
	public void delete()
	{
		printResponse(client.delete());
	}
	
	/**
	 * Prints respose of coAP server
	 * 
	 * @param response Response received from server
	 */
	private void printResponse(CoapResponse response)
	{
		if (response!=null) {
	        
        	System.out.println( response.getCode() );
        	System.out.println( response.getOptions() );
        	System.out.println( response.getResponseText() );
        	
        } else {
        	
        	System.out.println("Request failed");
        	
        }
	}
	
}
