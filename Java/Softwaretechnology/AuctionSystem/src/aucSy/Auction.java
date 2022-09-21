//package aucSy;

import java.util.*;

public abstract class Auction {

	private boolean closed;
	private List<Item> allItems;
	private List<Person> bidders;
	
	public Auction() {
		allItems = new ArrayList<Item>();
		bidders = new ArrayList<Person>();
		closed = false;
	}
	
	public void addBid(Item bidItem, String nameOfBidder, long price) {
		if(closed) {
			throw new IllegalStateException();
		}
		if(bidItem == null) {
			throw new NullPointerException();
		}
		if(nameOfBidder.equals("")) {
			throw new IllegalArgumentException();
		}
		if(price <= 0) {
			throw new IllegalArgumentException();
		}
		if(!allItems.contains(bidItem)) {
			throw new NoSuchElementException();
		}
		Person tmp_p = new Person(nameOfBidder);
		bidItem.addBid(tmp_p, price);
		bidders.add(tmp_p);
	}
	
	public String closeAuction() {
		if(closed) {
			throw new IllegalStateException();
		}
		closed = true;
		return generateItemListString();
	}
	
	public String generateAllBidsString(Item item) {
		if(item == null) {
			throw new NullPointerException();
		}
		
		String tmp = "All bids:";
		
		for(Bid bid : item.getAllBids()) {
			tmp +=  "\n" + bid.toString();
		}
		return tmp;
	}
	
	public String generateItemListString() {
		String tmp = "";
		
		for(Item item : allItems) {
			tmp +=  generateItemString(item) + "\n";
		}
		return tmp;
	}
	
	public void registerItem(Item item) {
		if(closed) {
			throw new IllegalStateException();
		}
		if(item == null) {
			throw new NullPointerException();
		}
		for(Item tmp : allItems) {
			if(tmp.getName().equals(item.getName())) {
				throw new IllegalArgumentException();
			}
		}
		allItems.add(item);
	}
	
	public abstract String generateItemString(Item item);
	
	public List<Item> getAllItems(){
		return allItems;
	}
}
