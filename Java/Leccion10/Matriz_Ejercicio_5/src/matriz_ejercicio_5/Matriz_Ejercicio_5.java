/*
Ejecicio 5: Crear y cargar una matriz de tamaño n x m, mostrar la suma
de cada fila y cada columna
 */
package matriz_ejercicio_5;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class Matriz_Ejercicio_5 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int matriz[][],filas,col,sumaFilas,sumaCol;
        int posFila,posCol;
        
        filas = Integer.parseInt(JOptionPane.showInputDialog("Digite la cantidad de filas: "));
        col = Integer.parseInt(JOptionPane.showInputDialog("Digite la cantidad de col: "));
        
        matriz = new int [filas][col];
        int fila[] = new int[filas];
        int columna[] = new int[col];
        
        System.out.println("Llenamos la matriz: ");
        for(int i=0;i<filas;i++){
            for(int j=0;j<col;j++){
                System.out.println("Matriz ["+i+"]["+j+"]: ");
                matriz[i][j] = entrada.nextInt();
            }
        }
        
        System.out.println("\nMostramos nuestra matriz: ");
        for(int i=0;i<filas;i++){
            for(int j=0;j<col;j++){
                System.out.println(matriz[i][j]+" ");
            }
            System.out.println("");
        }
        //Pasamos a sumar las filas
        posFila=0;
        for(int i=0;i<filas;i++){
            sumaFilas = 0;
            for(int j=0;j<col;j++){
                sumaFilas += matriz[i][j];
            }
            fila[posFila] = sumaFilas;
            posFila++;
        }
        
        //Pasamos a sumar las columnas
        posCol=0;
        for(int j=0;j<col;j++){
            sumaCol = 0;
            for(int i=0;i<filas;i++){
                sumaCol += matriz[i][j];
            }
            columna[posCol] = sumaCol;
            posCol++;
        }
        System.out.println("\nLa suma de filas es: ");
        for(int i=0;i<filas;i++){
            System.out.println(fila[i]+" - ");
        }
        System.out.println("");
        
        System.out.println("\nLa suma de columnas es: ");
        for(int i=0;i<col;i++){
            System.out.println(columna[i]+" - ");
        }
        System.out.println("");

        
    }
    
}
