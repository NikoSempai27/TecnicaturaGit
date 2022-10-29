
package Operaciones;

public class Aritmetica {
    //Atributos de la clase
    int a;
    int b;
    
    //El constructor es un metodo especial
    public Aritmetica(){ //constructor 1
        System.out.println("Seesta ejecutando este constructor numero uno");
    }
    // Estamos viendo lo que se llama sobrecarga de constructores
    public Aritmetica(int a, int b){ //constructor 2
        this.a = a;
        this.b = b;
        System.out.println("Se esta ejecutando el constructor numero dos");
    }
    
    //Metodo
    public void sumarNumeros(){
        int resultado = a + b;
        System.out.println("resultado = " + resultado);
    }
    
    public int sumarConRetorno(){
        //int resultado = a + b;
        return a + b;
    }
    
    public int sumarConArgumentos(int arg1, int arg2){ // Nunca debe ponerse la inferencia de tipo dentro de los parentesis del metodo o parametro
        this.a = arg1; // El argumento a se asigna al atributo this.a
        this.b = arg2;
        //return a + b;
        return sumarConRetorno();
    }
}
