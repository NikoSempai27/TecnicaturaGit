
package test;

public class TestArreglos {
    public static void main(String[] args) { //lado derec. instanciamos un objeto del tipo Object
        int edades[] = new int [3]; //el lado izq. declaramos la variable
        System.out.println("edades = " + edades);
        
        edades[0] = 17;
        System.out.println("edades 0 = " + edades [0]);
        
        //Tarea:
        
        edades[1] = 32;
        System.out.println("edades 1 = " + edades [1]);
        
        edades[2] = 25;
        System.out.println("edades 2 = " + edades [2]);
        
        //edades[3] = 7; //Fuera de rango de ejecucion
        
        for(int i = 0; i < edades.length; i++){
            System.out.println("edades y sus elementos: "+i+": "+edades[i]);
            
        }
        
    }
}
