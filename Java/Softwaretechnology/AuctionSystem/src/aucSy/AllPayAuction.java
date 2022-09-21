//package aucSy;

public class AllPayAuction extends Auction {

	@Override
	public String generateItemString(Item item) {
		if(item == null) {
			throw new NullPointerException();
		}
		
		if(item.getAllBids().size() == 0) {
			return item.toString() + "\n" + "No bids placed";
		}
		
		String tmp = "All bids:";
		
		for(Bid bid : item.getAllBids()) {
			tmp +=  "\n" + bid.toString();
		}
		return item.toString() + "\n" + "Highest bid: "
								+ String.valueOf(item.getHighestBid())
								+ "\n" + tmp;
	}
}
