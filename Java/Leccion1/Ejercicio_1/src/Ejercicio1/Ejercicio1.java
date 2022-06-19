//Tienda de Libros
package Ejercicio1;

import java.util.Scanner;

public class Ejercicio1 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite el nombre del Libro: ");
        String nombreLibro = entrada.nextLine();
        System.out.println("Digite el ID del Libro: ");
        int idLibro = Integer.parseInt(entrada.nextLine());
        System.out.println("Digite el precio del Libro: ");
        double precioLibro = Double.parseDouble(entrada.nextLine());
        System.out.println("Confirmar si el envio es gratuito: ");
        boolean envioGratuito = Boolean.parseBoolean(entrada.nextLine());
        
        System.out.println(nombreLibro +" #"+idLibro);
        System.out.println("Precio del Libro: $"+ precioLibro);
        System.out.println("El envio del libro es gratuito: "+ envioGratuito);
        
    }
}
