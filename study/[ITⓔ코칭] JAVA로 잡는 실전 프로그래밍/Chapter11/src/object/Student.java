package object;

public class Student {

	String name;
	int studentId;
	
	public Student(String name, int studentId) {
		this.name = name;
		this.studentId = studentId;
	}

	@Override
	public String toString() {
		// TODO Auto-generated method stub
//		return super.toString();
		return name + "," + studentId;
	}

	@Override
	public boolean equals(Object obj) {
		// TODO Auto-generated method stub
//		return super.equals(obj);
		if ( obj instanceof Student) {
			Student std = (Student) obj;
			if(this.studentId == std.studentId) {
				return true;
			}
			else { return false;}
		}
		return false;
	}

	@Override
	public int hashCode() {
		// TODO Auto-generated method stub
//		return super.hashCode();
		return studentId;
	}
	
	
}
