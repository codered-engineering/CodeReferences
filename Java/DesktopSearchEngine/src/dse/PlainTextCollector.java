//package dse;

import java.util.*;

public class PlainTextCollector implements KeywordCollector{

	@Override
	public Set<String> getKeywords(Resource res) {
		if(res == null) {
			throw new NullPointerException();
		}
		
		TextFileIterator tfi = new TextFileIterator(res);
		Set<String> setTmp = new HashSet<String>();
		
		while (tfi.hasNext()) {
			setTmp.add(tfi.next());
		}
		
		return setTmp;
	}

}
