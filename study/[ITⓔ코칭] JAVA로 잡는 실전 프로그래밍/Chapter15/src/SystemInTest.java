import java.io.IOException;
import java.io.InputStreamReader;

public class SystemInTest {

	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub

		int i = 0;
		InputStreamReader isr = new InputStreamReader(System.in);
		while( (i = isr.read()) != 'q'){
			System.out.println(i + "," + (char) i );
		}
		
		
//		Scanner scanner = new Scanner(System.in);
//		System.out.println("이름 : ");
//		String name = scanner.nextLine();
//		System.out.println("번호 : ");
//		int num = scanner.nextInt();
//		
//		System.out.println(name);
//		System.out.println(num);
	}

}
