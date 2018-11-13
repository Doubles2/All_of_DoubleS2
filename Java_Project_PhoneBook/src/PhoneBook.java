class PhoneInfo{
	String name;
	String phoneNumber;
	String birthday;
	
	public PhoneInfo(String _name, String _phoneNumber, String _birthday) {
		this.name = _name;
		this.phoneNumber = _phoneNumber;
		this.birthday = _birthday;
	}
	
	public PhoneInfo(String _name, String _phoneNumber) {
		this.name = _name;
		this.phoneNumber = _phoneNumber;
		this.birthday = null;
	}
	
	public void showInfo() {
		System.out.println("name : " + name);
		System.out.println("number : " + phoneNumber);
		System.out.println("brthday : " + birthday);
	}
}
public class PhoneBook {
	public static void main(String[] args) {
    PhoneInfo pi = new PhoneInfo("Sosoonwon", "012-345-6789", "1990-05-30");
    pi.showInfo();
	}
}
