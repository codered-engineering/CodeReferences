//package preIt;

public class StartsWith implements Predicate<String> {
	
	private String prefix;
	
	public StartsWith(String prefix) {
		if(prefix == null) {
			throw new IllegalArgumentException();
		}
		this.prefix = prefix;
	}
	
	@Override
	public boolean test(String value) {
		if(value == null || prefix.length() > value.length()) {
			return false;
		}
		if (value.equals("")) {
			return true;
		}
		for (int i = 0; i < prefix.length(); i++) {
			if(prefix.charAt(i) != value.charAt(i)){
				return false;
			}
		}
		return true;
	}
}
