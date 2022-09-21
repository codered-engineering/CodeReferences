//package aucSy;

public class EnglishAuction extends Auction{
	
	@Override
	public String generateItemString(Item item) {
		if(item == null) {
			throw new NullPointerException();
		}
		
		if(item.getAllBids().size() == 0) {
			return item.toString() + "\n" + "No bids placed";
		}
		return item.toString() + "\n" + "Highest bid: "
								+ String.valueOf(item.getHighestBid());
	}
}
