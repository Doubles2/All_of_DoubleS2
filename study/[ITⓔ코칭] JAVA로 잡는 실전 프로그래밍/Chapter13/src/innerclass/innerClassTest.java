package innerclass;

class outClass{
	
	private InClass inClass;
	private int num = 100;
	private static int snum = 300;
	
	public outClass() {
		inClass = new InClass();
	}
	
	class InClass{
		
		int inNum = 200;
		
		void inTest() {
			System.out.println(num);
			System.out.println(inNum);
			System.out.println(snum);
		}
	}
	
	public void usingInMethod() {
		inClass.inTest();
	}
}

public class innerClassTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		outClass outer = new outClass();
		outer.usingInMethod();
		
		// private 걸리면 못함
//		outClass.InClass inClass = outer.new InClass(); //가능은 함
		
		
		
	}

}
