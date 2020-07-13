package arraylist;

import java.util.ArrayList;

import array.Book;

public class ArrayListTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ArrayList<String> list = new ArrayList<String>();
		list.add("aaa");
		list.add("bbb");
		list.add("ccc");
		
		for(int i = 0 ; i < list.size() ; i++){
			System.out.println(list.get(i));
		}
		
		ArrayList<Book> library = new ArrayList<Book>();
		library.add(new Book("태백산맥1", "조정래"));
		library.add(new Book("태백산맥2", "조정래"));
		library.add(new Book("태백산맥3", "조정래"));
		
		for(Book book : library){
			book.showBookInfo();
			
		}
	}

}
