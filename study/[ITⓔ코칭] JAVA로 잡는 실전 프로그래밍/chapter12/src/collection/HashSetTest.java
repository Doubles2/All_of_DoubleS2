package collection;

import java.util.TreeSet;

public class HashSetTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

//		HashSet<Student> set = new HashSet<Student>();
//		
//		set.add(new Student("Kim", 1001));
//		set.add(new Student("Lee", 1005));
//		set.add(new Student("Park", 1003));
//		set.add(new Student("Park", 1003));
//		
//		System.out.println(set);
		
//		TreeSet<String> strSet = new TreeSet<String>();
//		strSet.add("test");
//		strSet.add("abc");
//		strSet.add("zzz");
//		
//		System.out.println(strSet);
		
		TreeSet<Student> set = new TreeSet<Student>();
		
		set.add(new Student("Kim", 1001));
		set.add(new Student("Lee", 1005));
		set.add(new Student("Park", 1003));
		set.add(new Student("Park", 1003));
		
		System.out.println(set);
	}

}
