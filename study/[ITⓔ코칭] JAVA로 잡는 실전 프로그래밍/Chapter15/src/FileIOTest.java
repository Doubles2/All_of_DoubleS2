import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.Socket;

public class FileIOTest {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub

		FileOutputStream fos = new FileOutputStream("a.txt");
		fos.write(97);
		fos.write(98);
		fos.write(99);
		fos.close();
		
		
		FileInputStream fis = new FileInputStream("a.txt");
		InputStreamReader isr = new InputStreamReader(fis);
//		int i = fis.read();
		int i;
		while( ( i = isr.read()) != -1){
			System.out.println(i + " " + (char)i);
		}		
		isr.close();
		
		Socket socket = new Socket();
		BufferedReader br = 
				new BufferedReader(new InputStreamReader(socket.getInputStream()));
		
	}

}
