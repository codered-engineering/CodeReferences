//package dse;

public class Resource {
	private String name;
	private String path;
	private ResourceType rt;
	
	public Resource(String name, String path, ResourceType rt) {
		if(name.equals("")) {
			throw new IllegalArgumentException();
		}
		if(path.equals("")) {
			throw new IllegalArgumentException();
		}
		if(rt == null) {
			throw new NullPointerException();
		}
		
		this.name = name;
		this.path = path;
		this.rt = rt;
	}

	public String getName() {
		return name;
	}
	
	public String getPath() {
		return path;
	}
	
	public ResourceType getType() {
		return rt;
	}
}
