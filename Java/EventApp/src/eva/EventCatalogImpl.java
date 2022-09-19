//package eva;

import java.util.*;

public class EventCatalogImpl extends java.util.TreeMap<Event, Set<Time>> implements EventCatalog {

	private static final long serialVersionUID = 4L;
	public Set<Time> times;
	
	@Override
	public boolean addCatalogEntry(Event e, Set<Time> tSet) {
		if(e == null) {
			throw new NullPointerException();
		}
		if(tSet == null) {
			throw new NullPointerException();
		}
		
		for(Time t : tSet) {
			if (t == null) {
				throw new NullPointerException();
			}
		}
		
		if(this.containsKey(e)) {
			return false;
		}

		
		if(this.containsKey(e)) {
			return false;
		}
		this.put(e, tSet);
		return true;
	}

	@Override
	public boolean addTimeToEvent(Event e, Time t) {
		if(e == null) {
			throw new NullPointerException();
		}
		if(t == null) {
			throw new NullPointerException();
		}
		
        if(this.containsKey(e)) {
            Set<Time> tmp = this.get(e);
            return tmp.add(t);
        }	
        return false;
	}

	@Override
	public Set<Event> getAllEvents() {
		return this.navigableKeySet();
	}

	@Override
	public Set<Time> getTimesOfEvent(Event e) {
		if(e == null) {
			throw new NullPointerException();
		}
		if(this.containsKey(e)) {
			return this.get(e);
			}
		return null;
	}

	@Override
	public Map<Event, Set<Time>> filterByEventCategory(EventCategory category) {
		if(category == null) {
			throw new NullPointerException();
		}
		Map<Event, Set<Time>> tmpMap = new HashMap<Event, Set<Time>>();
		Set<Event> tmpEvents = this.keySet();
		
		for(Event e : tmpEvents) {
			if(e.getCategory() == category) {
				tmpMap.put(e, this.get(e));
			}
		}
		return tmpMap;
	}

	@Override
	public Set<Time> deleteEvent(Event e) {
		if(e == null) {
			throw new NullPointerException();
		}
		if(this.containsKey(e)) {
			Set<Time> tmp = this.get(e);
			this.remove(e);
			return tmp;
		}
		return null;
	}

	@Override
	public boolean deleteTime(Event e, Time t) {
		if(e == null) {
			throw new NullPointerException();
		}
		if(t == null) {
			throw new NullPointerException();
		}
		if(this.containsKey(e)) {
			Set<Time> tmp = this.get(e);
			if(tmp.contains(t)) {
				tmp.remove(t);
				return true;
			}
		}
		return false;
	}
	



}
