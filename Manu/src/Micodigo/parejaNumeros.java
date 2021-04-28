package Micodigo;

public class parejaNumeros {
	//Attributes
	int num1;
	int num2;
	//constructor
	public parejaNumeros(int num1, int num2) {
		this.num1=num1;
		this.num2=num2;
		
	}
	//getters & setters
	/**
	 * @return the num1
	 */
	public double getNum1() {
		return num1;
	}
	/**
	 * @param num1 the num1 to set
	 */
	public void setNum1(int num1) {
		this.num1 = num1;
	}
	/**
	 * @return the num2
	 */
	public double getNum2() {
		return num2;
	}
	/**
	 * @param num2 the num2 to set
	 */
	public void setNum2(int num2) {
		this.num2 = num2;
	}
	//rest of methods
	public double suma() {
		return(num1+num2);
	}
	public double resta() {
		return(num1-num2);
	}
	public double producto() {
		return(num1*num2);
	}
	public double division() {
		double division;
		division=num1/num2;
		return(division);
	}

}
