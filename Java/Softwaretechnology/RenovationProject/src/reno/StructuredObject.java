//package reno;

import java.util.*;

public class StructuredObject extends RenovationObject{
	
	public Set<RenovationObject> parts;
	
	public StructuredObject() {
		parts = new HashSet<RenovationObject>();
		mats = new HashMap<String, Integer>();
		
	}
	
	public void add(RenovationObject renovationObject) {
		if(renovationObject == null) {
			throw new NullPointerException();
		}
		
		parts.add(renovationObject);
	}

	@Override
	public double getPrice() {
		double price = 0.0;
		for(String mat : mats.keySet()) {
			price += mats.get(mat);
		}
		return price;
	}

	@Override
	public Map<String, Integer> addMaterialRequirements(Map<String, Integer> materials) {
		if(materials == null) {
			throw new NullPointerException();
		}
		if(materials.containsKey(null)) {
			throw new NullPointerException();
		}
		if(materials.containsValue(null)) {
			throw new NullPointerException();
		}
		
		mats.putAll(materials);
		return mats;
	}
	
	

}
