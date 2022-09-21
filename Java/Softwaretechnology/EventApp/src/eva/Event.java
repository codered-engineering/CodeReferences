//package eva;

public class Event implements java.lang.Comparable<Event>{
	private String title;
	private EventCategory category;
	
	public Event(String title, EventCategory category) {
		if(title.equals("")) {
			throw new IllegalArgumentException();
		}
		if(category == null) {
			throw new NullPointerException();
		}
		
		this.title = title;
		this.category = category;
	}
	
	public String getTitle() {
		return title;
	}
	
	public EventCategory getCategory() {
		return category;
	}

	@Override
	public int compareTo(Event o) {
		if(o == null) {
			throw new NullPointerException();
		}
		int tmp = title.compareTo(o.getTitle());
		if(tmp == 0) {
			return category.compareTo(o.getCategory());
		}
		return tmp;
		}
	
}
