/*

 */
package Caja;

public class Caja {
    // Atributos de la clase
    int ancho;
    int alto;
    int profundidad;
    
    //Constructores 1 y 2
    public Caja(){
        
    }
    
    public Caja(int ancho, int alto, int profundidad){
        this.ancho = ancho;
        this.alto = alto;
        this.profundidad = profundidad;
    }
    
    //Metodo
    public int calcularVolumen(){
        return ancho * alto * profundidad;
        
        
    }
    
    
}
