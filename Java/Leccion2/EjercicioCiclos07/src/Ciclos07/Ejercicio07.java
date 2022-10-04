/*
Ejercicio 7: Pedir un numero hasta que se introduzca uno negativo
y calcular la media 
 */
package Ciclos07;

import javax.swing.JOptionPane;

public class Ejercicio07 {
    public static void main(String[] args) {
        int numero, suma = 0, conteo = 0;
        float promedio = 0;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while(numero >= 0){
            suma += numero;
            conteo++;
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));
        }
        if(conteo == 0){
            JOptionPane.showMessageDialog(null, "Error la divicion entre cero no existe: ");
        }
        else{
            promedio = (float)suma/conteo;
            JOptionPane.showMessageDialog(null, "El promedio de los numeros ingresados es: "+promedio);
        }
    }
    
}
