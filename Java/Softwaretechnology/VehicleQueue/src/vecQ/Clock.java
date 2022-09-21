//package vecQ;

import java.util.*;

public class Clock implements ClockObserver{
	
	private int currentTime = 0;
	private int endOfTime;
	private Set<ClockObserver> observers;
	
	
	public Clock(int endOfTime) {
		if(endOfTime <= 0) {
			throw new IllegalArgumentException();
		}
		this.endOfTime = endOfTime;
	}
	
	public void addObserver(ClockObserver observer) {
		observers.add(observer);
	}
	
	public void removeObserver(ClockObserver observer) {
		observers.remove(observer);
	}
	
	public int getCurrentTime() {
		return currentTime;
	}
	
	public void run() {
		while (currentTime < endOfTime){
			//currentTime++;
			tick(currentTime);
		}
	}
	
	@Override
	public void tick(int currentTime) {
		currentTime += 1;
	}
}
