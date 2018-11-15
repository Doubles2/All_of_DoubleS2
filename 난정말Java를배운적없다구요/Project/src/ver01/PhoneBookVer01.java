package ver01;


/*
 * 전화번호 관리 프로그램 구현 프로젝트
 *  ver : 01
 */
class PhoneInfo{
	String name;
	String phoneNumber;
	String birthDay;
	
	public PhoneInfo(String _name, String _phoneNumber, String _birthDay) {
		this.name = _name;
		this.phoneNumber = _phoneNumber;
		this.birthDay = _birthDay;
	}
	
	public PhoneInfo(String _name, String _phoneNumber) {
		this.name = _name;
		this.phoneNumber = _phoneNumber;
		this.birthDay = null;
	}
	
	public void showPhoneInfo() {
		System.out.println("name : " + name);
		System.out.println("phone number : " + phoneNumber);
		if(birthDay != null)
			System.out.println("birtday : " + birthDay);
	}
}

class PhoneBookVer01 {
	public static void main(String[] args) {
	PhoneInfo pInfo1 = new PhoneInfo("소순원1", "012-3456-7890", "1990-01-01");
	PhoneInfo pInfo2 = new PhoneInfo("소순원2", "0987-6543-210");
	pInfo1.showPhoneInfo();
	pInfo2.showPhoneInfo();
	}
}