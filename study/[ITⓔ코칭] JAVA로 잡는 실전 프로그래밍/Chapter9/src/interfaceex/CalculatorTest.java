package interfaceex;

public class CalculatorTest{

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int num1 = 10;
		int num2 = 2;
		
		Calc calculator = new CompleteCalculator();
		System.out.println(calculator.add(num1, num2));
		System.out.println(calculator.substract(num1, num2));
		System.out.println(calculator.times(num1, num2));
		System.out.println(calculator.divide(num1, num2));
	}

}
