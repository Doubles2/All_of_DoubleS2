package polymorphism;

class Shape {
	public void draw() {
		System.out.println("draw shape");
	}
}

class Rectangle extends Shape{
	public void draw() {
		System.out.println("draw reectangle");
	}
}

class Circle extends Shape{
	public void draw() {
		System.out.println("draw Circle");
	}
}
public class ShapeTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Shape s = new Shape();
		Rectangle r = new Rectangle();
		Circle c = new Circle();
		
		drawShape(s);
		drawShape(r);
		drawShape(c);
	}

	public static void drawShape(Shape s){
		s.draw();
	}
}
