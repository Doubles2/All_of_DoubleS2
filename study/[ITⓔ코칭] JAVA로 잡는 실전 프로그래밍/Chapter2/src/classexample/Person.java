package classexample;

public class Person {
	
	public int height;
	public int weight;
	private String name;
	
//	public Person() {}
	
	public Person(String pName){
		name = pName;
	}
	
	public Person(String pName, int pWeight, int pHeight){
		name = pName;
		height = pHeight;
		weight = pWeight;
	}
	public String showPersonInfo(){
		return "이름은 " + name + "이고, 키는 " + height + "이고, 몸무게는 " + weight + "입니다.";
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}
	
//	public String getName(){
//		return name;
//	}
//	
//	public void setName(String pName){
//		name = pName;
//	}

}
