
package ar.com.codesystem.ventas.test;

import ar.com.codesystem.ventas.*;

public class VentasTest {
    public static void main(String[] args) {
        Producto producto1 = new Producto("Pantalon", 9500.00);
        Producto producto2 = new Producto("Campera", 29900.00);
        
        Orden orden1 = new Orden();
        //Agregamos productos al arreglo
        orden1.agregarProducto(producto1);
        orden1.agregarProducto(producto2);
        orden1.mostrarOrden();
        
        //Tarea
        //Crear mas objetos de tipo Producto = 10
        //Crear mas objetos de tipo Orden = 2
        
        Producto producto3 = new Producto("Remera", 5000.00);
        Producto producto4 = new Producto("Camisa", 7500.00);
        Producto producto5 = new Producto("Piluso", 2900.00);
        Producto producto6 = new Producto("Zapatillas", 10000.00);
        
        Orden orden2 = new Orden();
        //Agregamos productos al arreglo
        orden2.agregarProducto(producto4);
        orden2.agregarProducto(producto5);
        orden2.agregarProducto(producto1);
        orden2.mostrarOrden();
        
        Producto producto7 = new Producto("Buzo", 12000.00);
        Producto producto8 = new Producto("Polera", 6000.00);
        Producto producto9 = new Producto("Minifalda", 5000.00);
        Producto producto10 = new Producto("Top", 4500.00);
        Producto producto11 = new Producto("Gorra", 2700.00);
        Producto producto12 = new Producto("Medias", 2000.00);
        
        Orden orden3 = new Orden();
        //Agregamos productos al arreglo
        orden3.agregarProducto(producto8);
        orden3.agregarProducto(producto9);
        orden3.agregarProducto(producto10);
        orden3.agregarProducto(producto6);
        orden3.mostrarOrden();
        
        
        
        
    }
}
