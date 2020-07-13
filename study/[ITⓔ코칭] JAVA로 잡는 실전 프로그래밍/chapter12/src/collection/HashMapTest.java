package collection;

import java.util.HashMap;
import java.util.TreeMap;

public class HashMapTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		HashMap<Integer, String> map = new HashMap<Integer, String>();
		map.put(100, "test");
		map.put(200, "abc");
		map.put(300, "zzz");
		
		System.out.println(map);
		
		String str = map.get(100);
		System.out.println(str);
		
		
		TreeMap<Integer, String> treeMap = new TreeMap<Integer, String>();
		treeMap.put(100, "test");
		treeMap.put(300, "abc");
		treeMap.put(200, "zzz");
		
		System.out.println(treeMap);
	}

}
