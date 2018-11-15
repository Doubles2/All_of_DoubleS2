package ver03;
/*
 * 전화번호 관리 프로그램 구현 프로젝트
 *  ver : 03
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

class PhoneBookManager{
	final int MAX_CNT = 100;
	PhoneInfo[] infoStorage = new PhoneInfo[MAX_CNT];
	int curCnt = 0;
	
	public void inputData() {
		System.out.println("데이터 입력을 시작합니다..");
		
		System.out.println("이름 : ");
		String name = MenuViewer.keyboard.nextLine();
		System.out.println("전화번호 : ");
		String phone = MenuViewer.keyboard.nextLine();
		System.out.println("생년월일 : ");
		String birth = MenuViewer.keyboard.nextLine();
		
		infoStorage[curCnt++] = new PhoneInfo(name, phone, birth);
		System.out.println("데이터 입력이 완료되었습니다. \n");
	}
	
	public void searchData() {
		System.out.println("데이터 검색을 시작합니다..");
		System.out.println("이름 : ");
		String name = MenuViewer.keyboard.nextLine();
		
		int dataIdx = search(name);
		if(dataIdx < 0)
			System.out.println("해당하는 데이터가 존재하지 않습니다.\n");
		else {
			infoStorage[dataIdx].showPhoneInfo();
			System.out.println("데이터 검색이 완료되었습니다.\n");
		}
	}
	
	public void deleteData() {
		System.out.println("데이터 삭제를 시작합니다..");
		System.out.println("이름 : ");
		String name = MenuViewer.keyboard.nextLine();
		
		int dataIdx = search(name);
		if(dataIdx < 0)
			System.out.println("해당하는 데이터가 존재하지 않습니다.\n");
		else {
			for(int idx = dataIdx ; idx < (curCnt - 1) ; idx++)
				infoStorage[idx] = infoStorage[idx+1];
			curCnt--;
			System.out.println("데이터 삭제가 완료되었습니다.\n");
		}
	}
	
	private int search(String name) {
		for(int idx = 0 ; idx < curCnt ; idx++) {
			PhoneInfo curInfo = infoStorage[idx];
			if(name.compareTo(curInfo.name) == 0)
				return idx;
		}
		return -1;
	}
}

class MenuViewer{
	public static Scanner keyboard = new Scanner(System.in);
	
	public static void showMenu() {
		System.out.println("선택하세요...");
		System.out.println("1. 데이터 입력");
		System.out.println("2. 데이터 검색");
		System.out.println("3. 데이터 삭제");
		System.out.println("4. 프로그램 종료");
		System.out.print("선택 : ");
	}
}

class PhoneBookVer03{
	public static void main(String[] args) {
		PhoneBookManager manager = new PhoneBookManager();
		int choice;
		
		while(true) {
			MenuViewer.showMenu();
			choice = MenuViewer.keyboard.nextInt();
			MenuViewer.keyboard.nextLine();
			
			switch(choice) {
			case 1:
				manager.inputData();
				break;
			case 2:
				manager.searchData();
				break;
			case 3:
				manager.deleteData();
				break;
			case 4:
			default:
				return;
			}
		}
	}
}

/*
 * 내가 짜려했던 코드나...책에서 나온 코드나..입력 밀리는거 똑같은데...
 * 그냥 내 코드로 밀고 나갈껄...후 열받네
 */

/*
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

class PhoneBookVer03 {
	
	final static int max_person = 100;
	static PhoneInfo[] PhoneBook = new PhoneInfo[max_person]; // 인스턴스 배열 선언
	static Scanner keyboard = new Scanner(System.in); // 입출력 선언
	static int index = 0; // 기준 index
	
	public static void main(String[] args) {		
		// 메인 시작
		while(true) {
			menu();
			// 메뉴 선택 시작
			int selection = keyboard.nextInt();			
			keyboard.nextLine(); 
			switch(selection) {
				case 1:
					input_info(); // 등록
					break;
				case 2:
					search_info();
					break;
				default:
					return; // 종료
			}
		}
	}
	
	public static void menu() {
		System.out.println("선택하세요...");
		System.out.println("1. 데이터 입력");
		System.out.println("2. 데이터 검색");
		System.out.println("3. 데이터 삭제");
		System.out.println("4. 프로그램 종료");
		System.out.print("선택 : ");		
	}
	
	public static void input_info() {
		System.out.println("데이터 입력을 시작합니다..");		
		System.out.print("이름 : ");
		String _name = keyboard.nextLine();
		System.out.print("전화번호 : ");
		String _phonenum = keyboard.nextLine();
		System.out.print("생일 : ");
		String _bday = keyboard.nextLine();
		
		PhoneBook[index++] = new PhoneInfo(_name, _phonenum, _bday);
		System.out.println("데이터 입력이 완료되었습니다.");
	}
	
	public static void search_info() {
		System.out.println("데이터 검색을 시작합니다..");
		System.out.print("이름 : ");
		String _name = keyboard.nextLine();
		
		int search_index = 0;
		
		for(int i = 0; i < index ; i++) {
			PhoneInfo PI = PhoneBook[i];			
			if(_name.compareTo(PI.name) == 0)
				search_index = i;				
		}
		System.out.println("name : " + PhoneBook[search_index].name);
		System.out.println("phone : " + PhoneBook[search_index].phoneNumber);
		System.out.println("birth : " + PhoneBook[search_index].birthDay);
	}
}
*/