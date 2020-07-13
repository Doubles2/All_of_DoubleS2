package object;

public class StringTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		String java = new String("java");
		String android = new String("android");
		
//		java = java.concat(android);
//		System.out.println(java);
		
		System.out.println(System.identityHashCode(java));
		java = java.concat(android);
		System.out.println(System.identityHashCode(java));
		
		StringBuilder buffer = new StringBuilder();
		buffer.append("java");
		buffer.append("android");
		buffer.append("javascript");
		
		String all = buffer.toString();
		System.out.println(all);
	}

}
