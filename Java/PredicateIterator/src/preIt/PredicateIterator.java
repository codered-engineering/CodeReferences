//package preIt;

import java.util.*;

public class PredicateIterator<T> implements java.util.Iterator<T>{
	
	private Iterator<T> iter;
	private Predicate<T> predicate;

	public PredicateIterator(Iterator<T> iter, Predicate<T> predicate) {
		if(iter == null) {
			throw new NullPointerException();
		}
		if(predicate == null) {
			throw new NullPointerException();
		}
		
        ArrayList<T> tmp = new ArrayList<T>();
        while(iter.hasNext() == true){
            T it_tmp = iter.next();
            if(predicate.test(it_tmp) == true){
                tmp.add(it_tmp);
            }
        }

		this.iter = tmp.iterator();
		this.predicate = predicate;
	}

	@Override
	public boolean hasNext() {
		return iter.hasNext();
	}

	@Override
	public T next() {
		return iter.next();
	}
	


}
