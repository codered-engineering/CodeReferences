//package vecQ;

import java.util.*;

public class VehicleQueue implements ClockObserver {

	private double entryDelay;
	private double exitDelay;
	private int trafficLightRate;
	private boolean greenLight = false;
	private List<Vehicle> queue;
	private VehicleGenerator generator;
	
	public VehicleQueue(double entryDelay, double exitDelay, int trafficLightRate, VehicleGenerator generator) {
		if(entryDelay < 0) {
			throw new IllegalArgumentException();
		}
		if(exitDelay < 0) {
			throw new IllegalArgumentException();
		}
		if(trafficLightRate <= 0) {
			throw new IllegalArgumentException();
		}
		if(generator == null) {
			throw new NullPointerException();
		}
		
		this.entryDelay = entryDelay;
		this.exitDelay = exitDelay;
		this.trafficLightRate = trafficLightRate;
		this.generator = generator;
		queue = new ArrayList<Vehicle>();
	}
	
	public void enter() {
		queue.add(generator.createVehicle());
		//entryDelay;
	}
	
	public void leave() {
		
		for(int i = 0; i < getSize(); i++) {
			if(greenLight) {
				queue.remove(i);
				//exitDelay;
			}
		}
	}
	
	public double getLength() {
		// Bus 18m, car 6m, bike 1.5m
		double len = 0;
		for(Vehicle veh : queue) {
			len += veh.getLength();
		}
		return len;
	}
	
	public int getSize() {
		//number of vehicles
		return queue.size();
	}
	
	
	@Override
	public void tick(int currentTime) {
		// TODO Auto-generated method stub
		
	}

	
}
