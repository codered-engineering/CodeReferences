//package aucSy;

public class Bid {
	private long price;
	private Person bidder;
	
	public Bid(Person bidder, long price){
		if(bidder == null) {
			throw new NullPointerException();
		}
		if(price <= 0) {
			throw new IllegalArgumentException();
		}
		
		this.price = price;
		this.bidder = bidder;
		
	}
	
	public Person getBidder() {
		return bidder;
	}
	
	public long getPrice() {
		return price;
	}
	
	public String toString() {
		//<price> EUR by <name of bidder>
		return String.valueOf(price) + " EUR by " + bidder.getName();
	}
}
