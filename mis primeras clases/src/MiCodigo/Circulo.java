package Micodigo;

public class Circulo{
	private double radio;
	//private double centro_x;
	//private double centro_y;
	public Circulo(double radio) {
		this.setRadio(radio);
		radio=reader.nextlnt();
		for(int i=0;i<radio; i++) {
			System.out.printf("*");
		}
	}
	public double getRadio() {
		return radio;
	}
	public void setRadio(double radio) {
		this.radio = radio;
	}
}