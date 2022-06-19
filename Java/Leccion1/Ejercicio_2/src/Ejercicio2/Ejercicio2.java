
package Ejercicio2;

import java.util.Scanner;

public class Ejercicio2 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int horasSemanales ;
        float salarioHora, SalarioTotal ;
        
        System.out.println("Digte las horas semanales trabajadas: ");
        horasSemanales = Integer.parseInt(entrada.nextLine());
        System.out.println("Digite el valor de la hora: ");
        salarioHora = Float.parseFloat(entrada.nextLine());
        
        SalarioTotal = horasSemanales * salarioHora;
        System.out.println("\n El salario semanal es: US$"+ SalarioTotal);
        
        
    }
}
