//package promanager;

public abstract class ProjectItem {
	private String name;
	private String details;
	private double rate;
	
	public ProjectItem(String name, String details, double rate) {
		if (name.equals("")) {
			throw new IllegalArgumentException();
		}
		if (details.equals("")) {
			throw new IllegalArgumentException();
		}
		if (rate < 0) {
			throw new IllegalArgumentException();
		}
		
		this.name = name;
		this.details = details;
		this.rate = rate;
	}
	
	public void setDetails(String newDetails) {
		if (newDetails.equals("")) {
			throw new IllegalArgumentException();
		}
		details = newDetails;
	}
	
	public long getCostEstimate() {
		return Math.round(rate*getTimeRequired()) + getMaterialCost();
	}
	
	public abstract double getTimeRequired();
	
	public abstract long getMaterialCost();
}
