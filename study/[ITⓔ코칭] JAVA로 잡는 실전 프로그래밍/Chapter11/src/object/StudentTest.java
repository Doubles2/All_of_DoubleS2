package object;

public class StudentTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Student studentKim = new Student("KIM", 1001);
		System.out.println(studentKim);
		
		
		Student studentKim2 = new Student("KIM", 1001);
		System.out.println(studentKim2);
		
		System.out.println(studentKim == studentKim2);
		System.out.println(studentKim.equals(studentKim2));
		
		System.out.println(studentKim.hashCode());
		System.out.println(studentKim2.hashCode());
		
		String str = new String("test");
//		System.out.println(str);
		
		String str2 = new String("test");
		
		System.out.println(str == str2);
		System.out.println(str.equals(str2));
		
		System.out.println(str.hashCode());
		System.out.println(str2.hashCode());
	}

}
