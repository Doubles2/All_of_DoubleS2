package classexample;

public class PersonTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Person personLee = new Person("ÀÌ¸ù·æ");
		
		personLee.height = 180;
		personLee.weight = 85;
//		personLee.name = "ÀÌ¸ù·æ";
		
		String name = personLee.getName();
		personLee.setName("Lee");
		System.out.println(name);
		
		
		System.out.println(personLee.showPersonInfo());
		
		Person personKim = new Person("±èÀ¯½Å", 100, 188);
		
//		personKim.height = 188;
//		personKim.weight = 100;
//		personKim.name = "±èÀ¯½Å";
		
		System.out.println(personKim.showPersonInfo());
		
		System.out.println(personLee);
		System.out.println(personKim);
	}

}
