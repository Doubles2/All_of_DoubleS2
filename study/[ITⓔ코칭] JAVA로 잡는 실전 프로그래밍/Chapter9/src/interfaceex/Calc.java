package interfaceex;

public interface Calc {

	public static final int ERROR = -9999999;
	
	int add(int num1, int num2);
	int substract(int num1, int num2);
	int times(int num1, int num2);
	int divide(int num1, int num2);
	
	
	default void description(){
		System.out.println("정수 사칙연산을 구현합니다.");
	}
	
	
}
