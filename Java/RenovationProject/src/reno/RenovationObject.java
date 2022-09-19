//package reno;

import java.util.*;

public abstract class RenovationObject {
	
	public static Map<String, Integer> mats;
	
	public abstract double getPrice();
	
	public abstract Map<String, Integer> addMaterialRequirements(Map<String, Integer> materials);
	
}
