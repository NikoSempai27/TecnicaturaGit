/*
Ejecicio 3: Leer 5 numeros por teclado, almacenarlos en
un arreglo y a continuacion realizar la media de los 
numeros positivos, la media de los negativos y contar el 
numerode ceros.
 */
package arreglos_ejercicio_3;

import java.util.Scanner;

public class Arreglos_Ejercicio_3 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        float numeros[] = new float[5];
        float negativos = 0, positivos = 0, mediaNegativos, mediaPositivos;
        int contar0 = 0, conteoNegativos = 0, conteoPositivos = 0;
        
        System.out.println("Se guardan los datos");
        for(int i = 0; i < 5; i++){
            System.out.println((i+1)+". Digite un numero: ");
            numeros[i] = entrada.nextFloat();
            if(numeros[i]>0){
                positivos += numeros[i];
                conteoPositivos++;
            }
            else if(numeros[i]<0){
                negativos += numeros[i];
                conteoNegativos++;
            }
            else{
                    contar0++;
            }
        }
        if(conteoPositivos == 0){
            System.out.println("\nNo se puede sacar la media de los positivos");
        }
        else{
                mediaPositivos = positivos/conteoPositivos;
                System.out.println("\nLa media de los positivos es: "+mediaPositivos);
        }
        if(conteoNegativos == 0){
            System.out.println("\nNo se puede sacar la media de los negativos");
        }
        else{
                mediaNegativos = negativos/conteoNegativos;
                System.out.println("\nLa media de los negativos es: "+mediaNegativos);
        }
        System.out.println("La cantidad de ceros es: "+contar0);
    }
    
}
