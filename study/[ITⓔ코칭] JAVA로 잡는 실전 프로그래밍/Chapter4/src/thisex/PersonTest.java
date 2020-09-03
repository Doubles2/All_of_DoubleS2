package thisex;

public class PersonTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Person p = new Person("James", "Seoul");
		p.showInfo();
		
		Person p2 = new Person();
		p2.showInfo();
		
		System.out.println(p2);
		System.out.println(p2.returnSelf());
	}

}
