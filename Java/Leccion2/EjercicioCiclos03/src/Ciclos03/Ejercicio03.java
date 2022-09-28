/*
Ejercicio 3: Leer numeros hasta que se introduzca un cero
indicar para cada uno si es par o impar 
hacerlo en clase Scanner y en JOptionPane
*/
package Ciclos03;

import javax.swing.JOptionPane;

public class Ejercicio03 {
    public static void main(String[] args) {
        int numero;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while(numero != 0){
            if(numero % 2 == 0){
                JOptionPane.showMessageDialog(null, "El numero: "+numero+" es Par");
            }
            else{
                JOptionPane.showMessageDialog(null, "El numero: "+numero+" es Impar");
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));
        }
        JOptionPane.showMessageDialog(null, "El numero: "+numero+" Finaliza el Programa");
        //Quede en el video 19 de la 3er clase 
    }
    
}
