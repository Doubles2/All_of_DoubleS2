import java.util.Scanner;

class ScanningMethdos {
	public static void main(String[] args) {
		Scanner keyboard = new Scanner(System.in);
		
		// 문자열 입력
		System.out.print("당신의 이름은?");
		String str = keyboard.nextLine();
		System.out.println("안녕하세요 " + str + "님");
		
		// boolean 입력
		System.out.print("당신은 스파게티를 좋아한다는데, 진실입니까?");
		boolean isTrue = keyboard.nextBoolean();
		if(isTrue)
			System.out.println("오 ~ 좋아하는 군요");
		else
			System.out.println("이런 아니군요");
		
		// double 입력
		System.out.println("당신과 동생의 키는 어떻게 되나요?");
		double num1 = keyboard.nextDouble();
		double num2 = keyboard.nextDouble();
		double diff = num1 - num2;
		if(diff > 0)
			System.out.println("당신이 " + diff + "만큼 더 크군요");
		else
			System.out.println("당신이 " + -diff + "만큼 더 작군요");
	}
}
