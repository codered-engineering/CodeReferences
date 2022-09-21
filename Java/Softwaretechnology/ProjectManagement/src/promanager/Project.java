//package promanager;

import java.util.*;
import java.time.LocalDate;

public class Project {
	private String name;
	private String description;
	private Task maintask;
	
	public Project(String name, String description, double rate) {
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
		maintask = newTask;
	}
	
	public double getDuration() {
		return maintask.getTimeRequired();
	}
	
	public long getTotalCost() {
		return maintask.getCostEstimate();
	}
	
	public Map<LocalDate, List<Deliverable>> allDeliverables(){
		Map<LocalDate, List<Deliverable>> mapTmp = new HashMap<LocalDate, List<Deliverable>>();
		List<Deliverable> tmpAllDelis = maintask.allDeliverables();
		
        for (Deliverable x : tmpAllDelis){
            LocalDate lookup = x.getDate();
            if (mapTmp.containsKey(lookup)){
            	mapTmp.get(lookup).add(x);
            }
            else{
                List<Deliverable> toinsert = new ArrayList<Deliverable>();
                toinsert.add(x);
                mapTmp.put(lookup, toinsert);
            }
        }
        return mapTmp;
	}
}
