package interfaceex;

public class CompleteCalculator extends Calculator{

	@Override
	public int times(int num1, int num2) {
		// TODO Auto-generated method stub
		return num1 * num2;
	}

	@Override
	public int divide(int num1, int num2) {
		// TODO Auto-generated method stub
		if( num2 == 0 ) {
			return Calc.ERROR;
		}
		return num1 / num2;
	}

}
