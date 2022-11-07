/*

 */
package test;

import dominio.Persona;

public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Osvaldo", 57.000, false);
        System.out.println("persona1 = " + persona1);
        System.out.println("Persona1 su nombre es: "+persona1.getNombre());
        // Modicar a traves de los metodos
        persona1.setNombre("Juan Ignacio");
        // persona1.nombre = "Juan Ignacio"; Ya no se puede utilizar
        //System.out.println("Nombre es: "+persona1.nombre); Error
        System.out.println("Persona1 su nombre modificado es: "+persona1.getNombre());
        System.out.println("persona1 el resultado para el sueldo: "+persona1.getSueldo());
        System.out.println("persona1 para obtener el booleano: "+persona1.isEliminado());
        // Tarea: Crear otro objeto de tipo persona, asignar valores de manera inicial
        //y imprimir , luego modificar sus valores y volver a imprimir
        System.out.println("persona1 = " + persona1);
        
        Persona persona2 = new Persona("Marcela", 97650.20, false);
        System.out.println("Elnombre de persona2 es: "+persona2.getNombre());
        System.out.println("Su sueldo es de: "+persona2.getSueldo());
        System.out.println("Es correcto su nombre y sueldo: "+persona2.isEliminado());
        
        // Modificamos
        persona2.setNombre("Claudia Alejandra");
        persona2.setSueldo(110780.69);
        persona2.setEliminado(true);
        // Imprimimos los valores modificados 
        System.out.println("Elnombre de persona2 es: "+persona2.getNombre());
        System.out.println("Su sueldo es de: "+persona2.getSueldo());
        System.out.println("Es correcto su nombre y sueldo: "+persona2.isEliminado());
        
        
        
        
        
        
        
        
        
        
        
        
    }
    
}
