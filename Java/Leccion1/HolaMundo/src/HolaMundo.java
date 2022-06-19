
import java.util.Scanner;

public class HolaMundo {

    public static void main(String[] args) {
        /* System.out.println("Hola Mundo desde Java");
        
        int miVariable = 10;
        System.out.println(miVariable);
        miVariable = 5;
        System.out.println(miVariable);
        // Tipo String
        String miVariableCadena = "Bienvenidos";
        System.out.println(miVariableCadena);
        miVariableCadena = "Sigamos creciendo en Programacion";
        System.out.println(miVariableCadena);
         */

        //Var - Inferencia de tipos en Java
        /*var miVariableEntera2 = 10;
        var miVariableCadena2 = "Seguimos estudiando";
        System.out.println("miVariableEntera2 = " + miVariableEntera2);
        System.out.println("miVariableCadena2 = " + miVariableCadena2);
        //soutv + tab
        //Para ejecutarmanualmente precionamos shift + F6
        //Reglas para definir una variable en Java 

        var usuario = "Osvaldo";
        var titulo = "Ingeniero";
        var union = titulo + " " + usuario;
        System.out.println("union = " + union);
        
        var a = 8;
        var b = 4;
        System.out.println(usuario + (a + b));
        //Ejercicio Caracteres Especiales con Java
        var nombre = "Natalia";
        System.out.println("\nNueva linea: \n"+nombre); //Diagonal inversa y letra n
        System.out.println("Tabulador: \t"+nombre); //Tabulador un espacio para centrar
        System.out.println("\t\t.:MENU:.");
        System.out.println("Retroseso: \b\b"+nombre); //caracter de retroseso
        System.out.println("Comillas simple: \'"+nombre+"\'");
        System.out.println("Comillas dobles: \""+nombre+"\"");*/
        //Clase Scanner
        /*Scanner entrada = new Scanner(System.in);
        System.out.println("Digite su nombre: ");
        var usuario2 = entrada.nextLine();
        System.out.println("usuario2 = " + usuario2);
        System.out.println("Escriba el titulo: ");
        var titulo2 = entrada.nextLine();
        System.out.println("Resultado: "+titulo2+" "+usuario2);*/
        //Ejercicio Libro
        /*Scanner scanner = new Scanner(System.in);
        System.out.println("Proporciona el titulo: ");
        String titulo = scanner.nextLine();
        System.out.println("Proporciona el autor: ");
        String autor = scanner.nextLine();
        System.out.println(titulo + " fue escrito por " + autor);*/
        //Tipos Primitivos en Java
        /*byte numEnteroByte = 127;
        System.out.println("numEnteroByte = " + numEnteroByte);
        System.out.println("Valor minimo del Byte: "+ Byte.MIN_VALUE);
        System.out.println("Valor maximo del Byte: "+ Byte.MAX_VALUE);
        
        short numEnteroShort = 32767;
        System.out.println("numEnteroShort = " + numEnteroShort);
        System.out.println("Valor minimo del Short: "+ Short.MIN_VALUE);
        System.out.println("Valor maximo del Short: "+ Short.MAX_VALUE);
        
        int numEnteroInt = 2147483647;
        System.out.println("numEnteroInt = " + numEnteroInt);
        System.out.println("Valor minimo del Int: "+ Integer.MIN_VALUE);
        System.out.println("Valor maximo del Int: "+ Integer.MAX_VALUE);
        
        long numEnteroLong = 9223372036854775807L;
        System.out.println("numEnteroLong = " + numEnteroLong);
        System.out.println("Valor minimo del Long: "+ Long.MIN_VALUE);
        System.out.println("Valor maximo del Long: "+ Long.MAX_VALUE);*/
        //Tipos Flotantes en Java
        /*float numFloat = 3.4028235E38F;
        System.out.println("numFloat = " + numFloat);
        System.out.println("El valor minimo del float: "+ Float.MIN_VALUE);
        System.out.println("El valor maximo del float: "+ Float.MAX_VALUE);
        
        double numDouble = 1.7976931348623157E308;
        System.out.println("numDouble = " + numDouble);
        System.out.println("El valor minimo del double: "+ Double.MIN_VALUE);
        System.out.println("El valor maximo del double: "+ Double.MAX_VALUE);*/
        //Inferencias de tipo var y tipo primitivos
        /*var numEntero = 20; //Laas literales sin punto son automaticamente del tipo Int
        System.out.println("numEntero = " + numEntero);
        var numFloat = 10.0F; //Automaticamente con el punto se transforma en tipo Double
        System.out.println("numFloat = " + numFloat);
        var numDouble = 10.0;
        System.out.println("numDouble = " + numDouble);*/
        //Tipos primitivos Char
        /*char miVariableChar = 'a';
        System.out.println("miVariableChar = " + miVariableChar);
        
        char varCaracter = '\u0024'; //Indicamos a Java la asignacion con el codigo unigode
        System.out.println("varCaracter = " + varCaracter);
        char varCaracterDecimal = 36; //Valor decimal del juego de caracteres unicode
        System.out.println("varCaracterDecimal = " + varCaracterDecimal);
        char varCaracterSimbolo = '$'; //Un caracter especial, podemos copar y pegar desde unicode
        System.out.println("varCaracterSimbolo = " + varCaracterSimbolo);
        
        var varCaracter1 = '\u0024'; //Indicamos a Java la asignacion con el codigo unigode
        System.out.println("varCaracter1 = " + varCaracter1);
        var varCaracterDecimal1 = (char)36; //Valor decimal del juego de caracteres unicode
        System.out.println("varCaracterDecimal1 = " + varCaracterDecimal1);
        var varCaracterSimbolo1 = '$'; //Un caracter especial, podemos copar y pegar desde unicode
        System.out.println("varCaracterSimbolo1 = " + varCaracterSimbolo1);
        
        int varEnteroChar = '$';
        System.out.println("varEnteroChar = " + varEnteroChar);
        int caracterChar = 'b';
        System.out.println("caracterChar = " + caracterChar);*/
        //Tipos primitivos tipos Booleanos
        /*var varBool = false;
        System.out.println("varBool = " + varBool);
        
        if(varBool){
            System.out.println("La bandera es Verde");
        }
        else{
            System.out.println("La bandera es Roja");
        }
        
        //Agoritmo: ¿Eres mayor de edad?
        var edad = 18; //Literal tener presente la inferencia de tipos
        //var adulto = edad >= 18; //Esta es una exprecion Booleana
        if(edad >=18){
            System.out.println("Eres mayor de edad");
        }
        else{
            System.out.println("Eres menor de edad");
        }*/
        //Conversion de tipos primitivos
        /*var edad = Integer.parseInt("20");
        System.out.println("edad = " + (edad + 1));
        var valorPI = Double.parseDouble("3.1416");
        System.out.println("valorPI = " + valorPI);
        
        //Pedir un valor
        var entrada = new Scanner(System.in);
       System.out.println("Digite su edad");
        edad = Integer.parseInt( entrada.nextLine());
        System.out.println("edad = " + edad);
        
        //Conversion de tipos primitivos en Java parte 2
        var edaeTexto = String.valueOf(10);
        System.out.println("edaeTexto = " + edaeTexto);
        
        var fraseChar = "programadores".charAt(4);
        System.out.println("fraseChar = " + fraseChar);
        
        System.out.println("Digite un caracter");
        fraseChar = entrada.nextLine().charAt(0);
        System.out.println("fraseChar = " + fraseChar);*/
        /*int num1 = 5, num2 = 4;
        var solucion = num1 + num2;
        System.out.println("solucion de la suma = " + solucion);
        
        solucion = num1 - num2;
        System.out.println("solucion de la resta = " + solucion);
        
        solucion = num1 * num2;
        System.out.println("solucion de la multiplicacion = " + solucion);
        
        solucion = num1 / num2;
        System.out.println("solucion de la divicion = " + solucion);
        
        var solucion2 = 3.4 / num2;
        System.out.println("solucion2 resultado de la divicion = " + solucion2);
        
        solucion = num1 % num2; //guarda el residuo entero de la divicion
        System.out.println("solucion el residuo es = " + solucion);
        
        if (num2 % 2 == 0)
            System.out.println("Es un umero par");
        else
            System.out.println("Es un numero impar");*/
        /*int varNum1 = 1, varNum2 = 4;
        int varNum3 = varNum1 + 6 - varNum2; //Una operacion 
        System.out.println("varNum3 = " + varNum3);
        
        varNum1 += 1; //varNum1 = varNum1 + 1; 
        System.out.println("varNum1 = " + varNum1);
        
        varNum1 -= 1;
        System.out.println("varNum1 = " + varNum1);
        
        varNum3 *= 3;
        System.out.println("varNum3 = " + varNum3);
        
        varNum2 /= 2;
        System.out.println("varNum2 = " + varNum2);
        
        varNum3 %= 6;
        System.out.println("varNum3 = " + varNum3);*/
        // Operadores Unarios: Cambio de Signo
        /*var varA = 7;
        var varB = -varA;
        System.out.println("varA = " + varA);
        System.out.println("varB = " + varB); //El resultado sera un numero negativo
        
        //Operador de Negacion 
        var varC = true; //Esta literal por default en Java es de tipo Boolean
        var varD = !varC; // Aqui esta invertido el valor 
        System.out.println("varC = " + varC);
        System.out.println("varD = " + varD);
        
        //Operadores Unarios de Incremento: Preincremento
        var varE = 9; //Se va a modificar su valor 
        var varF = ++varE; //Simbolo antes de la variable
        //Primero se incrementa la variable y despues se usa su valor
        System.out.println("varE = " + varE); //Se incremanta en la unidad
        System.out.println("varF = " + varF); //Va a sumar uno
        
        //Post incremento (El signo va despues de la variable)
        var varG = 3;
        var varH = varG++; //Primero el valor de la variable, luego el incremento
        System.out.println("varG = " + varG);
        System.out.println("varH = " + varH);
        
        //Operadores Unarios de Decemento: Predecremento
        var varI = 4;
        var varJ = --varI;
        System.out.println("varI = " + varI); //La variable ya va a estar con decremento
        System.out.println("varJ = " + varJ);
        
        //Post decremento (El signo va despues de la variable)
        var varK = 8;
        var varL = varK--; //Primero el valor de la variable, luego el decremento
        System.out.println("varK = " + varK); //Aqui va a decrementar en 1
        System.out.println("varL = " + varL);*/
        //Operadres de Igualdad y Racionales 
        /*var aNum = 5;
        var bNum = 4;
        var cNum = (aNum == bNum);
        System.out.println("cNum = " + cNum);

        var dNum = aNum != bNum;
        System.out.println("dNum = " + dNum);

        var cadenaA = "Hello";
        var cadenaB = "Bye bye";
        var cVar = cadenaA == cadenaB;
        System.out.println("cVar = " + cVar);

        var fVar = cadenaA.equals(cadenaB);
        System.out.println("fVar = " + fVar);

        var gVar = aNum > bNum; // > >= < <= == !=
        System.out.println("gVar = " + gVar);

        if (aNum % 2 == 0) {
            System.out.println("El numero es par");
        } else {
            System.out.println("El numero es impar");
        }
        
        var edad = 30;
        var adulto = 18;
        if (edad >= adulto){
            System.out.println("Es mayor de edad");
        }
        else{
            System.out.println("Es menor de edad");
        }*/
        //Operador Condicional And
        /*var valorA = 7;
        var valorMinimo = 0; //rango del 0 al 10
        var valorMaximo = 10;
        var respuesta = valorA >= 0 && valorA <= 10;
        
        if (respuesta)
            System.out.println("Esta dentro del rango establecido");
        else
            System.out.println("Esta fuera del rango establecido");
        
        //Operador Condicional Or
        var vacaciones = true;
        var diaLibre = false;
        if (vacaciones || diaLibre)
            System.out.println("Papa puede asistir al juego de su hijo");
        else
            System.out.println("Papa no puede asistir al juego de su hijo");*/
        
        //Operador Ternario
        /*var resultadoT = (5 > 4) ? "Verdaero" : "Falso";
        System.out.println("resultadoT = " + resultadoT);
        
        var numeroT = 7;
        resultadoT = (numeroT % 2 == 0) ? "Es Par" : "Es Impar";
        System.out.println("resultadoT = " + resultadoT);*/
        
        //Prioridad de los Operadores
        var x =5;
        var y = 10;
        var z = ++x + y--; 
        System.out.println("x = " + x); //6
        System.out.println("y = " + y); //9
        System.out.println("z = " + z); //16
        
        var solucionAritmica = 4 + 5 * 6 / 3; //(5*6=30), (30/3=10), (10+4=14) 14
        System.out.println("solucionAritmica = " + solucionAritmica);
        
        solucionAritmica = (4 + 5) * 6 / 3; // (5+4=9), (9*6=54), (54/3=18)
        System.out.println("solucionAritmica = " + solucionAritmica);
        
    }
}
