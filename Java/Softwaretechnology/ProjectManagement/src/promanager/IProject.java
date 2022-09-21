//package promanager;

import java.util.*;

public interface IProject {
	public void setTask(Task newTask);
	public double getDuration();
	public long getTotalCost();
	public List<Deliverable> getDeliverables();
}
