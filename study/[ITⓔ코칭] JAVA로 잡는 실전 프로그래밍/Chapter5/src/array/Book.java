package array;

public class Book {
	String title;
	String author;
	
	public Book(String title, String author){
		this.title = title;
		this.author = author;
	}
	
	public void showBookInfo(){
		System.out.println(title + "," + author);
	}
}
