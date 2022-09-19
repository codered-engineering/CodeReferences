//package prc;

import java.util.*;

public abstract class ComplexPricing implements ISalePricing{
	public List<ISalePricing> pricings;

	public ComplexPricing(ISalePricing pricing) {
		if(pricing == null) {
			throw new NullPointerException();
		}
		pricings = new ArrayList<ISalePricing>();
		pricings.add(pricing);
	}
	
	public void add(ISalePricing pricing) {
		if(pricing == null) {
			throw new NullPointerException();
		}
		pricings.add(pricing);
	}
	
	public List<ISalePricing> getPricings(){
		return pricings;
	}
}
