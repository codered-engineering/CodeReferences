//package preIt;

public class EndsWith implements Predicate<String> {
	
	private String suffix;
	
	public EndsWith(String suffix) {
		if(suffix == null) {
			throw new IllegalArgumentException();
		}
		this.suffix = suffix;
	}
	
	@Override
	public boolean test(String value) {
		if(value == null || suffix.length() > value.length()) {
			return false;
		}
		if (value.equals("")) {
			return true;
		}
		for (int i = 0; i < suffix.length(); i++) {
			if(suffix.charAt(suffix.length() - 1 - i) != value.charAt(value.length() - 1 - i)){
				return false;
			}
		}
		return true;
	}

}
