//package reno;

public class Paint extends Material{

	private static double limit = 0.02;
	private int numberOfCoats;
	private double squareMetersPerLiter;
	
	public Paint(String name, double price, int numberOfCoats, double squareMetersPerLiter) {
		super(name, price);
		
		if(numberOfCoats <= 0) {
			throw new IllegalArgumentException();
		}
		if(squareMetersPerLiter <= 0) {
			throw new IllegalArgumentException();
		}
		
		this.numberOfCoats = numberOfCoats;
		this.squareMetersPerLiter = squareMetersPerLiter;
	}
	
	public int getNumberOfCoats() {
		return numberOfCoats;
	}
	
	public double getSquareMetersPerLiter() {
		return squareMetersPerLiter;
	}

	@Override
	public int getMaterialRequirements(Surface surface) {
		if(surface == null) {
			throw new NullPointerException();
		}
		double tmp = Math.round((surface.getArea()*getNumberOfCoats())/getSquareMetersPerLiter()*100)/100 - limit;
		tmp = Math.round(tmp * 100) / 100;
		int out = (int) ((tmp - limit + 1) * 2);
		
		
		return out;

	}

}
