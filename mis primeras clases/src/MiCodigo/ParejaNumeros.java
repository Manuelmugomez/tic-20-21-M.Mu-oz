package MiCodigo;

public class ParejaNumeros {
	//Aqui van los atributos
	int num1;
	int num2;
	
	//El constructor
	public ParejaNumeros(int NuevoNum1, int NuevoNum2){
		num1=NuevoNum1;
		num2=NuevoNum2;
		
		
		
		
	}
	
	
	//Resto de metodos
	public int devuelveSuma(){
		return(num1+num2);

	}
	public int devuelveResta() {
		return(num1-num2);
	}
	public float devuelveDivision(){
		float division;
		 division=(num1/num2);
		 return(division);
	}
	public int devuelveMultiplicacion(){
		return(num1*num2);
	}
}