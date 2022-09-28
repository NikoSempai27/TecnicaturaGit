/*
Ejercicio 4: Pedir numeros hasta que se ingrese uno negativo,
mostrar cuantos numeros se han introducido.
Realiza el ejercicio con clase Scanner y despues con
JOptionPane.
*/
package Ciclos04;

import java.util.Scanner;

public class Ciclos04 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, conteo = 0;
        System.out.println("Digite un numero: ");
        numero = Integer.parseInt(entrada.nextLine());
        while(numero >= 0){
            System.out.println("El numero "+numero+" es Positivo");
            conteo++;
            System.out.println("Digite otro numero: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("Se ingresaron: "+conteo+" numeros positivos");
    
    }
    
}
