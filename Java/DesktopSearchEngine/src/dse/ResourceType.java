//package dse;

import java.util.Set;

public class ResourceType {
	
	private String description;
	private KeywordCollector collector;
	
	public ResourceType(String desc, KeywordCollector collector) {
		if(desc.equals("")) {
			throw new IllegalArgumentException();
		}
		if(collector == null) {
			throw new NullPointerException();
		}
		this.description = desc;
		this.collector = collector;
	}
	
	public String getDescription() {
		return description;
	}
	
	public KeywordCollector getCollector() {
		return collector;
	}
	
}
