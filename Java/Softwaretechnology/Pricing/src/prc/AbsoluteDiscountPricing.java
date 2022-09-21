//package prc;

public class AbsoluteDiscountPricing implements ISalePricing{

	private long discount;
	private long threshold;
	
	public AbsoluteDiscountPricing(long discount, long threshold) {
		if(discount <= 0) {
			throw new IllegalArgumentException();
		}
		if(threshold <= 0) {
			throw new IllegalArgumentException();
		}
		
		this.discount = discount;
		this.threshold = threshold;
	}
	
	@Override
	public long getTotal(Sale sale) {
		if(sale == null) {
			throw new NullPointerException();
		}
		long tmp = sale.getPreDiscountTotal() - discount;
		if(sale.getPreDiscountTotal() < threshold) {
			return sale.getPreDiscountTotal();
		}
		if(tmp < threshold) {
			return threshold;
		}
		return tmp;
	}

}
