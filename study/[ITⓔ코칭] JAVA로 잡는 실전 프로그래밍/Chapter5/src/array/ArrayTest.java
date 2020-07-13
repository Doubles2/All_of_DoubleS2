package array;

public class ArrayTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] numbers = new int [] {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
		
		int total = 0;
		for(int i = 0 ; i < numbers.length ; i++) {
			total += numbers[i];
		}
		
		System.out.println(total);
	}

}
