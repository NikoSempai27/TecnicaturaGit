
package Ejercicio3;

import java.util.Scanner;


public class Ejercicio3 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int alto, ancho;
        int area, perimetro;
        
        System.out.println("Digite el alto del rectangulo: ");
        alto = Integer.parseInt(entrada.nextLine());
        System.out.println("Digite el ancho del rectangulo: ");
        ancho = Integer.parseInt(entrada.nextLine());
        
        area = alto * ancho;
        perimetro = (alto + ancho)* 2;
        System.out.println("El area del rectangulo es = " + area);
        System.out.println("El perimetro del rectangulo es = " + perimetro);
        
    }
}
