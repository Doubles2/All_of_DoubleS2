
public class SCE {
	public static void main(String[] args) {
		int num1 = 0, num2 = 0;
		boolean result;
		
		result = (num1 += 10) < 0 && (num2 += 10) > 0;
		System.out.println("result = " + result);
		System.out.println("num1 = " + num1 + ", num2 : " + num2);
		
		result = (num1 += 10) < 0 || (num2 += 10) > 0;
		System.out.println("result = " + result);
		System.out.println("num1 = " + num1 + ", num2 : " + num2);
		
		int a = 3 + 6;
		System.out.println(a);
		System.out.println(a+=9);
		System.out.println(a+=12);
	}

}
