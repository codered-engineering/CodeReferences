//package aucSy;

public class Person {
	private String name;
	
	public Person(String name) {
		if(name.equals("")) {
			throw new IllegalArgumentException();
			}
		
		this.name = name;
	}
	
	public String getName() {
		return name;
	}
	
	public String toString() {
		return name;
	}
}
