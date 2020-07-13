package innerclass;


class Outer{

	public Runnable getRunnable(){

		return new Runnable() {

			@Override
			public void run() {
				// TODO Auto-generated method stub
				System.out.println("run()");
			}
			
		};
//		class MyRunnable implements Runnable{
//
//			@Override
//			public void run() {
//				// TODO Auto-generated method stub
//				System.out.println("run()");
//			}
//			
//		}
//		return new MyRunnable();
	}
	
	Runnable runner = new Runnable() {
		@Override
		public void run() {
			// TODO Auto-generated method stub
			System.out.println("runner");
		}
	};
}

public class AnonymousInnerTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Outer outer = new Outer();
		Runnable runnable = outer.getRunnable();
		runnable.run();
	}

}
