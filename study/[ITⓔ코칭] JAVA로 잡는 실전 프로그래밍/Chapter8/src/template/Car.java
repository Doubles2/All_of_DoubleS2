package template;

public abstract class Car {

	public void startCar(){
		System.out.println("시동을 켭니다.");
	}
	
	public void turnOff(){
		System.out.println("시동을 큽니다.");
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
