//package dse;

import java.util.*;

public class DesktopSearch {
	
	private Map<String, ResourceType> types;
	private Index index;
	
	public DesktopSearch() {
		types = new HashMap<String, ResourceType>();
		index = new Index();
	}
	
	public void registerType(String extension, ResourceType type) {
		if(extension == null) {
			throw new NullPointerException();
		}
		if(type == null) {
			throw new NullPointerException();
		}
		if(extension.equals("")) {
			throw new IllegalArgumentException();
		}
		
		if(!types.containsKey(extension)) {
			types.remove(extension);
			
		}
		types.put(extension, type);
		
	}
	
	public ResourceType getType(String extension) {
		if(extension == null) {
			return null;
		}
		if(extension.equals("")) {
			throw new IllegalArgumentException();
		}
			
		if(types.containsKey(extension)) {
			return types.get(extension);
		}
		return null;
	}
	
	public void unregisterType(String extension) {
		if(extension.equals("")) {
			throw new IllegalArgumentException();
		}
		types.remove(extension);
	}
	
	public void registerResource(Resource res) {
		if(res == null) {
			throw new NullPointerException();
		}
		index.add(res);
	}
	
	public List<Resource> processRequest(String request){
		if(request.equals("")) {
			throw new IllegalArgumentException();
		}
		
		return index.getResources(request);
	}
}
