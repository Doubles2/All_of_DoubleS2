package exception;

import java.io.FileInputStream;
import java.io.FileNotFoundException;

public class ThrowException {

	public Class loadClass(String filename, String className) throws FileNotFoundException, ClassNotFoundException{
		FileInputStream fis = new FileInputStream(filename);
		Class c = Class.forName(className);
		return c;
	}
	public static void main(String[] args) {
		ThrowException test = new ThrowException();
		try {
			test.loadClass("a2.txt",  "test");
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		}
	}
}
