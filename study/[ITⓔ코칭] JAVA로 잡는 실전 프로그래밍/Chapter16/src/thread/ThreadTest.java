package thread;

class MyThread extends Thread{
	
	public void run(){
		int i;
		for(i = 0 ; i <= 200 ; i++){
			System.out.print(i + "\t");
			try {
				sleep(100);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
	}
}

public class ThreadTest {

	public static void main(String[] args){
		
		System.out.println("main start");
		MyThread thread1 = new MyThread();
		thread1.start();
		
		MyThread thread2 = new MyThread();
		thread2.start();
		System.out.println("main end");
		
	}
}
