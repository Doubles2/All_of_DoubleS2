package bookshelf;

import java.util.ArrayList;

public class Shelf extends Object{

	protected ArrayList<String> shelf;
	
	public Shelf() {
		shelf = new ArrayList<String>();
	}
	
	public int getCount() {
		return shelf.size();
	}
}
