package inheritance;

public class GoldMemberShip extends MemberShip {

	private double salesRatio; 
	
	public GoldMemberShip(int memberId, String memberName) {
		super(memberId, memberName);
		// TODO Auto-generated constructor stub
		memberShip = "GOLD";
		bonusRatio = 0.05;
		salesRatio = 0.05;
	}
	
	@Override
	public int calcPrice(int price){
		bonusPoint += price * bonusRatio;
		price -= price * salesRatio;
		return price;
	}
	
//	public GoldMemberShip(){
//		
//		memberShip = "GOLD";
//		System.out.println("GOLD 클래스 생성");
//	}
	
	
}
