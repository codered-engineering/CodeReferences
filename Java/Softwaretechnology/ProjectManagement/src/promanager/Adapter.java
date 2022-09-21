//package promanager;

import java.util.ArrayList;
import java.util.List;

public class Adapter implements IProject {
	
	private String name;
	private String description;
	private List<ProjectItem> items;
	
	public Adapter (String name, String description, double rate) {
		if (name.equals("")) {
			throw new IllegalArgumentException();
		}
		if (description.equals("")) {
			throw new IllegalArgumentException();
		}
		if (rate < 0) {
			throw new IllegalArgumentException();
		}
		
		this.name = name;
		this.description = description;
		items = new ArrayList<ProjectItem>();
	}
	
	public String getName() {
		return name;
	}
	
	public String getDescription() {
		return description;
	}
	
	public void setTask(Task newTask) {
		if (newTask == null) {
			throw new NullPointerException();
		}
		items = new ArrayList<ProjectItem>();
		items.add(newTask);
	}
	
	public double getDuration() {
		double time = 0;
		for(ProjectItem task : items) {
			time += task.getTimeRequired();
		}
		return time;
	}
	
	public long getTotalCost() {
		long sum = 0;
		for(ProjectItem task : items) {
			sum += task.getCostEstimate();
		}
		return sum;
	}
	
	public List<Deliverable> getDeliverables(){
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
