//package promanager;

import java.util.*;

public class Task extends ProjectItem {
	private List<ProjectItem> items;
	
	public Task(String name, String details, double rate) {
		super(name, details, rate);
		items = new ArrayList<ProjectItem>();
	}

	@Override
	public double getTimeRequired() {
		double time = 0;
		
		for(ProjectItem item : items)
		{
			time += item.getTimeRequired();
		}
		return time;
	}

	@Override
	public long getMaterialCost() {
		long sum = 0;
		
		for(ProjectItem item : items)
		{
			sum += item.getMaterialCost();
		}
		return sum;
	}
	
	public void addProjectItem(ProjectItem pi) {
		if (pi == null) {
			throw new NullPointerException();
		}
		items.add(pi);
	}
	
	public void removeProjectItem(ProjectItem pi) {
		if (pi == null) {
			throw new NullPointerException();
		}

		items.remove(pi);
	}
	
	public List<Deliverable> allDeliverables(){
		List<Deliverable> delis = new ArrayList<Deliverable>();
		for (ProjectItem pi : items) {
			if(pi instanceof Deliverable) {
				delis.add((Deliverable) pi);
			}
			else {
				Task tmp = (Task) pi;
				delis.addAll(tmp.allDeliverables());
			}
		}
		return delis;
	}

}

