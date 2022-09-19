//package prc;

public class BestForStorePricing extends ComplexPricing{

	public BestForStorePricing(ISalePricing pricing) {
		super(pricing);
	}
	
	@Override
	public long getTotal(Sale sale) {
		if(sale == null) {
			throw new NullPointerException();
		}
		long bestPrice = pricings.get(0).getTotal(sale);
		
		for(ISalePricing pricing : pricings) {
			if(pricing.getTotal(sale) > bestPrice) {
				bestPrice = pricing.getTotal(sale);
			}
		}
		return bestPrice;
	}
}
