/*
Ejercicio 4: Pedir numeros hasta que se ingrese uno negativo,
mostrar cuantos numeros se han introducido.
Realiza el ejercicio con clase Scanner y despues con
JOptionPane.
*/
package Ciclos04;

import javax.swing.JOptionPane;

public class Ejercicio04 {
    public static void main(String[] args) {
        int numero, conteo = 0;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while(numero >= 0){
            JOptionPane.showMessageDialog(null, "El numero :"+numero+" es Positivo");
            conteo++;
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));
            
        }
        JOptionPane.showMessageDialog(null, "Se ingresaron: "+conteo+" numeros Positivos");
    }
    
}
