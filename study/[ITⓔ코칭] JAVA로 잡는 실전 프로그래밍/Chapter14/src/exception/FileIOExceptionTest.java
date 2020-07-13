package exception;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

public class FileIOExceptionTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		 
		try (FileInputStream fis = new FileInputStream("a.txt")){
			 
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			System.out.println(e);			
		} catch (IOException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		} 
	}

}
