//package aucSy;

import java.util.*;

public class Item {

	private String name;
	private String description;
	private long minPrice;
	private List<Bid> allBids;
	private Bid highestBid;
	
	public Item(String name, String description, long minPrice) {
		if(name.equals("")) {
			throw new IllegalArgumentException();
			}
		if(description.equals("")) {
			throw new IllegalArgumentException();
		}
		if(minPrice <= 0) {
			throw new IllegalArgumentException();
		}
		
		this.name = name;
		this.description = description;
		this.minPrice = minPrice;
		allBids = new ArrayList<Bid>();
	}
	
	public void addBid(Person bidder, long price) {
		if(bidder == null) {
			throw new NullPointerException();
		}
		if(price <= 0) {
			throw new IllegalArgumentException();
		}
		
		Bid tmp = new Bid(bidder, price);
		if(allBids.isEmpty() && price >= minPrice) {
			allBids.add(tmp);
			highestBid = tmp;
		}
		else if(highestBid != null) {
			if(price > highestBid.getPrice()) {
				allBids.add(tmp);
				highestBid = tmp;
			}
		}
	}
	
	public List<Bid> getAllBids(){
		return allBids;
	}
	
	public String getName() {
		return name;
	}
	
	public String getDescription() {
		return description;
	}
	
	public Bid getHighestBid() {
		return highestBid;
	}
	
	public String toString() {
		//<name>: <description> (minimum bidding price: <minPrice> EUR)
		return getName() + ": " + getDescription() 
				+ " (minimum bidding price: " + String.valueOf(minPrice)
				+ " EUR)";
	}
	
}
