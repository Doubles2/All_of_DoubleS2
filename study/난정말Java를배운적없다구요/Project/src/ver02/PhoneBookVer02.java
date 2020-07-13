package ver02;
/*
 * 전화번호 관리 프로그램 구현 프로젝트
 *  ver : 02
 */

import java.util.Scanner;

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

class PhoneBookVer02 {
	// 입출력 선언
	static Scanner keyboard = new Scanner(System.in);
	
	public static void main(String[] args) {		
		// 메인 시작
		while(true) {
			System.out.println("선택하세요...");
			System.out.println("1. 데이터 입력");
			System.out.println("2. 프로그램 종료");
			System.out.print("선택 : ");
			
			// 메뉴 선택 시작
			int selection = keyboard.nextInt();			
			keyboard.nextLine(); 
			switch(selection) {
				case 1:
					input_info(); // 등록
					break;
				case 2:
				default:
					return; // 종료
			}
		}
	}
	
	public static void input_info() {
		System.out.print("이름 : ");
		String _name = keyboard.nextLine();
		System.out.print("전화번호 : ");
		String _phonenum = keyboard.nextLine();
		System.out.print("생일 : ");
		String _bday = keyboard.nextLine();
		
		PhoneInfo tmp_PhoneInfo = new PhoneInfo(_name, _phonenum, _bday);
		System.out.println("입력된 정보 출력...");
		tmp_PhoneInfo.showPhoneInfo();
	}
}