
package test;

import domain.Cliente;
import domain.Empleado;
import java.util.Date;

public class TestHerencia {
    public static void main(String[] args) {
        Empleado empleado1 = new Empleado("Ariel", 57000.00);
        System.out.println("empleado1 = " + empleado1);
        
        //Creamos el objeto para la clase cliente
        Cliente cliente1 = new Cliente(new Date(), true, "Nicolas", 'M', 32, "San Juan 162");
        System.out.println("cliente1 = " + cliente1);
    }
}
