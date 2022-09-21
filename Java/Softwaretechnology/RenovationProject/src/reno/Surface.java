//package reno;

import java.util.*;

public class Surface extends RenovationObject{
	private double length;
	private double width;
	private Material mat = null;
	
	public Surface(double length, double width) {
		if(length <= 0) {
			throw new IllegalArgumentException();
		}
		if(width <= 0) {
			throw new IllegalArgumentException();
		}
		
		this.length = length;
		this.width = width;
	}
	
	public void setMaterial(Material material) {
		if(material == null) {
			throw new NullPointerException();
		}
		mat = material;
	}
	
	public double getArea() {
		return length * width;
	}
	
	public double getLength() {
		return length;
	}
	
	public double getWidth() {
		return width;
	}
	
	@Override
	public double getPrice() {
		return mat.getPriceOfASurface(this);
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
		
		if(mat != null) {
			mats.putAll(materials);
			return mats;
		}
		
		return null;
	}

}
