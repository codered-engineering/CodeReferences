//package dse;

import java.util.*;

public class DefaultCollector implements KeywordCollector {

	@Override
	public Set<String> getKeywords(Resource res) {
		if(res == null) {
			throw new NullPointerException();
		}
		Set<String> tmp = new HashSet<String>();
		tmp.add(res.getName());
		return tmp;
	}

}
