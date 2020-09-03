package template;

public abstract class Car {

	public void startCar(){
		System.out.println("�õ��� �մϴ�.");
	}
	
	public void turnOff(){
		System.out.println("�õ��� Ů�ϴ�.");
	}
	
	public abstract void drive();
	public abstract void stop();
	
	public final void run(){
		startCar();
		drive();
		stop();
		turnOff();
	}
}
