package classexample;

public class PersonTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Person personLee = new Person("�̸���");
		
		personLee.height = 180;
		personLee.weight = 85;
//		personLee.name = "�̸���";
		
		String name = personLee.getName();
		personLee.setName("Lee");
		System.out.println(name);
		
		
		System.out.println(personLee.showPersonInfo());
		
		Person personKim = new Person("������", 100, 188);
		
//		personKim.height = 188;
//		personKim.weight = 100;
//		personKim.name = "������";
		
		System.out.println(personKim.showPersonInfo());
		
		System.out.println(personLee);
		System.out.println(personKim);
	}

}
