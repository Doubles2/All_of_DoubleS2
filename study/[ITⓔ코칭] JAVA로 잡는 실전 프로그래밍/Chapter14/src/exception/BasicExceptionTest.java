package exception;

public class BasicExceptionTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		String[] strArr = new String[] {"java", "hello", "android"};
		
		try {
			for(int i = 0 ; i <= 3 ; i++) {
				System.out.println(strArr[i]);
			}	
		} catch(ArrayIndexOutOfBoundsException e) {
			System.out.println(e);
		}
		System.out.println("end");
	}

}
