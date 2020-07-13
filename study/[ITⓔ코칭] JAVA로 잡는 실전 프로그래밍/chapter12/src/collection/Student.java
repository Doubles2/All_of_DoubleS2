package collection;

public class Student implements Comparable<Student>{

	String studentName;
	int studentId;
	
	public Student(String studentName, int studentId) {
		this.studentId = studentId;
		this.studentName = studentName;
	}
	
	@Override
	public String toString() {
		// TODO Auto-generated method stub
//		return super.toString();
		return studentName + "," + studentId;
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

	@Override
	public int compareTo(Student student) {
		// TODO Auto-generated method stub
		
//		return (this.studentId - student.studentId) * (-1);
		return (this.studentName.compareTo(student.studentName));
	}
}
