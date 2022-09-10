
package Leccion2;

import java.util.Scanner;

public class Leccion2 {
    public static void main(String[] args) {
//        var condicion = true;
//        if (condicion){
//            System.out.println("Condicion verdadera"); // condicion simple
//        }
//        else{
//            System.out.println("Condicon falsa"); // condicion doble
//        }
//        
//        var numero = 2;
//        var numeroTexto = "Numero desconocido";
//        if(numero == 1){
//            numeroTexto = "Numero uno";
//        }
//        else if(numero == 2){
//            numeroTexto = "Numero dos";
//        }
//        else if(numero == 3){
//            numeroTexto = "Numero tres";
//        }
//        else if(numero == 4){
//            numeroTexto = "Numero cuatro";
//        }
//        else{
//            numeroTexto = "Numero no encontrado";
//        }
//        System.out.println("numeroTexto = " + numeroTexto);

        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un numero entre 1 y 4: ");
        var numero = Integer.parseInt(entrada.nextLine());
        var numeroTexto = "Valor desconocido";
        switch(numero){
            case 1 :
                numeroTexto = "Numero uno";
                break;
            case 2:
                numeroTexto = "Numero dos";
                break;
            case 3:
                numeroTexto = "Numero tres";
                break;
            case 4:
                numeroTexto = "Numero cuatro";
                break;
            default:
                numeroTexto = "Caso no encontrado";
                
        }
        System.out.println("numeroTexto = " + numeroTexto);





        
    }
}
