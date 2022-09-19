//package prc;

public class Sale {
	
	private long preDiscountTotal;
	private ISalePricing pricing;
	
	public Sale(long preDiscountTotal, ISalePricing pricing) {
		if(preDiscountTotal <= 0) {
			throw new IllegalArgumentException();
		}
		if(pricing == null) {
			throw new NullPointerException();
		}
		
		this.preDiscountTotal = preDiscountTotal;
		this.pricing = pricing;
	}
	
	public long getPreDiscountTotal() {
		return preDiscountTotal;
	}
	
	public void setPricing(ISalePricing pricing) {
		if(pricing == null) {
			throw new NullPointerException();
		}
		this.pricing = pricing;
	}
	
	public long getTotal() {
		return pricing.getTotal(this);
	}
	
	public static ISalePricing createPricing(DiscountType discountType, double percentage, long discount, long threshold) {
		if(discountType == null) {
			throw new NullPointerException();
		}
		if(percentage < 0) {
			throw new IllegalArgumentException();
		}
		if(discount < 0) {
			throw new IllegalArgumentException();
		}
		if(threshold < 0) {
			throw new IllegalArgumentException();
		}

		ISalePricing tmpPricing = null;
		if(discountType == DiscountType.PERCENTAGEDISCOUNT) {
			if(percentage == 0 || discount != 0 || threshold != 0) {
				throw new IllegalArgumentException();
			}
			else {
				tmpPricing = new PercentageDiscountPricing(percentage);
			}
		}
		if(discountType == DiscountType.ABSOLUTEDISCOUNT) {
			if(percentage != 0 || discount == 0 || threshold == 0) {
				throw new IllegalArgumentException();
			}
			else {
				tmpPricing = new AbsoluteDiscountPricing(discount, threshold);
			}
				
		}
		

		return tmpPricing;
	}

}
