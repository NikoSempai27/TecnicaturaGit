/*
Ejercicio 2: Leer un numero e indicar si es positivo o
negtivo. Repetir hasta que se introduzca un cero
Tarea: Reahacer este mismo ejercicio con la clase JOptionPane
*/
package Ciclos02;

import javax.swing.JOptionPane;

public class Ciclos02 {
    public static void main(String[] args) {
        int numero;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero:"));
        while(numero != 0){
            if(numero > 0){
                System.out.println("El numero "+numero+" es positivo");
            }
            else{
                System.out.println("El numero "+numero+" es negativo");
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero:"));
        }
        System.out.println("El numero "+numero+" Finaliza el programa");
        /*
         Con JOptionPane.showMessageDialog()nos muestra los mensajes
        a traves de la misma ventana emergente de JOptionPane sin 
        necesidad de utilizar la consola de NetBeans
        */

 
    }
}
