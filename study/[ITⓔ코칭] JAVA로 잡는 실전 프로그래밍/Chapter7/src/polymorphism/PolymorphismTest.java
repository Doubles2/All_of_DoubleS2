package polymorphism;

import java.util.ArrayList;

import inheritance.GoldMemberShip;
import inheritance.MemberShip;

public class PolymorphismTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		ArrayList<MemberShip> memberList = new ArrayList<MemberShip>();
		
		MemberShip memberLee = new MemberShip(10001, "Lee");
		MemberShip memberKim = new GoldMemberShip(10002, "Kim");
		
		memberList.add(memberLee);
		memberList.add(memberKim);
		
		int price = 10000;
		for(MemberShip member : memberList){
			int newPrice = member.calcPrice(price);
			System.out.println(newPrice);
		}
	}

}
