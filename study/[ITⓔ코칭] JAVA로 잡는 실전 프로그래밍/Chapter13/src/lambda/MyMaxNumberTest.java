package lambda;

public class MyMaxNumberTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		MyMaxNumber maxNum = (x, y) -> { return (x >= y ) ? x: y;};
		int max = maxNum.getMax(10, 20);
		System.out.println(max);
	}

}
