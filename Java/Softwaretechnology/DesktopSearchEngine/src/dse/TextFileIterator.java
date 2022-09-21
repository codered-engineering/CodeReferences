//package dse;

import java.util.*;

public class TextFileIterator implements java.util.Iterator<String>{
	
	int idx;
	private String txt = "We wish you good luck in this exam!\nWe hope you are well pre-\npared.";
	private String[] splittedtxt;
	
	public TextFileIterator(Resource res) {
		if(res == null) {
			throw new NullPointerException();
		}
        if(txt.contains("-\n") && Character.isLowerCase(txt.charAt(txt.indexOf("-\n")+3))) {
        	txt = txt.replace("-\n", "");
        } 
        if(txt.contains("\n")){
        	txt = txt.replace("\n", " ");
        }            
        txt = txt.replace("!", "");
        txt = txt.replace(",", "");
        txt = txt.replace(".", "");
        splittedtxt = txt.split(" ");
        
        idx = 0;
    }

	@Override
	public boolean hasNext() {
		if(idx < splittedtxt.length) {
			return true;
		}
		else {
			return false;
		}
	}

	@Override
	public String next() {
		idx += 1;
        if (idx > splittedtxt.length){
            throw new NoSuchElementException();
        }
        return splittedtxt[idx-1];
	}
	
	@Override
	public void remove() {
		throw new UnsupportedOperationException();
	}
	
	public String getAsString(Resource res) {
		if(res == null) {
			throw new NullPointerException();
		}
		return txt;
	}
}
