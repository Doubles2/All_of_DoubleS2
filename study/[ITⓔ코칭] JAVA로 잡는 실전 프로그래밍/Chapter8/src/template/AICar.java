package template;

public class AICar extends Car{

	@Override
	public void drive(){
		System.out.println("자율 주행 합니다.");
		System.out.println("알아서 방향전환 합니다.");
	}
	
	@Override
	public void stop(){
		System.out.println("장애물이 있으면 스스로 멉춥니다.");
	}
}
