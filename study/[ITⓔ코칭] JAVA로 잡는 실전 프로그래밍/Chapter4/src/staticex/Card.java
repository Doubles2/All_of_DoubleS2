package staticex;

public class Card {
	
	static int serialNum = 1000;
	int cardNumber;
	
	public Card() {
		serialNum++;
		cardNumber = serialNum;
	}

	public static int getSerialNum() {
		return serialNum;
	}

	public static void setSerialNum(int serialNum) {
		Card.serialNum = serialNum;
	}
	
	
}
