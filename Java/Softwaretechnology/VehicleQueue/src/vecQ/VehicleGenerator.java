//package vecQ;

import java.util.*;

public class VehicleGenerator {
	private Random randomGenerator;
	
	public VehicleGenerator() {
		
	}
	
	public Vehicle createVehicle() {
		Vehicle tmp;
		//if(randomGenerator == Bus)
		tmp = new Bus();
		tmp = new Car();
		tmp = new Bicycle();
		return tmp;
	}
}
