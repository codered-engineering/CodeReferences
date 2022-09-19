//package dse;

import java.util.*;

public class Index {
	private Map<String, List<Resource>> index;
	
	public Index() {
		index = new HashMap<String, List<Resource>>();
	}
	
    public void add(Resource res){
		if(res == null) {
			throw new NullPointerException();
		}
        Set<String> tmp = res.getType().getCollector().getKeywords(res);
        
         for(String st : tmp){
             if(index.containsKey(st)){
                List<Resource> tmpL = index.get(st);
                if(!tmpL.contains(res)) {
                	tmpL.add(res);
                }
             }
             else{
                 List<Resource> list = new ArrayList<Resource>();
                 list.add(res);
                 index.put(st, list);
             }
         }
    }
	
	public List<Resource> getResources(String keyword) {
		if(keyword == null) {
			throw new NullPointerException();
		}
		if(keyword.equals("")) {
			throw new IllegalArgumentException();
		}

		if(index.containsKey(keyword)) {
			return index.get(keyword);
		}
		return new ArrayList<Resource>();
		
		
	}
}
