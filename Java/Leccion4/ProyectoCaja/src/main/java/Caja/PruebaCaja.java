/*
Proyecto Caja:
Ejercicio 1: Crear un proyecto segun las especificaciones 
mostradas a continuacion.
La formula es: volumen = ancho * alto * profundidad;
 */
package Caja;

public class PruebaCaja {
    public static void main(String[] args) {
        int deAncho = 2;
        int deAlto = 4;
        int deProfundidad = 6;
         
        Caja caja1 = new Caja();
        caja1.ancho = deAncho;
        caja1.alto = deAlto;
        caja1.profundidad = deProfundidad;
        int resultado = caja1.calcularVolumen();
        System.out.println("El volumen de la caja1 es: "+resultado);
    
        Caja caja2 = new Caja(5, 7, 3);
        System.out.println("El volumen de la caja2 es: "+caja2.calcularVolumen());
        
    }
}

