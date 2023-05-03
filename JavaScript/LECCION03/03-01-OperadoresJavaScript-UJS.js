//Ejercicio para encontrar numeros pares e impares
let parImpar = 10;
if(parImpar % 2 == 0){
    console.log("Es un numero PAR");
}
else{
    console.log("Es un numero IMPAR");
}

//Ejercicio: Es mayor de edad
let edad = 18, adulto = 18;
if(edad >= adulto){
    console.log('Usted es una persona adulta');
}
else{
    console.log('Usted es una persona menor de edad')
}

//Ejercicio dentro de un Rago
let dentroRango = 5; //Aqui vamos a ir cambiando el valor
let valMin =0, valMax = 10;
if(dentroRango >= valMin && dentroRango <= valMax){
    console.log('El valor esta dentro del Rango');
}
else{
    console.log('El valor esta fuera del Rango')
}

// Ejercicio: Si el padre puede asistir al juego de su hijo
let vacaciones = false, diaDescanso = true;
if(vacaciones || diaDescanso){
    console.log("El padre puede asistir al juego de su hijo")
}
else{
    console.log("El padre No puede asistir al juego de su hijo")
}

//Operador Ternario
let resultado2 = 3 > 2 ? "verdadero" : "falso";
console.log(resultado2);
let numero = 9;
resultado2 = numero % 2 == 0 ? "Esun numero PAR" : "Es un numero IMPAR";
console.log(resultado2);

//Convertir Stinng a Number
let miNumero = "10"; //Es una cadena
console.log(typeof miNumero);
let edad2 = Number(miNumero); //Esta es una funcion
console.log(typeof edad2);
//Funcion isNaN
if(isNaN(edad2)){ //No es un numero = Is Not a Number(devuelve un resultado Booleano)
    console.log("Esta variable no contiene solo numeros")
}
else{
    if(edad2 >= 18){
        console.log("Puede votar");
    }
    else{
        console.log("Muy joven para votar");
    }
}

//Operador Ternario
let resultado3 = edad2 >= 18 ? "Puede votar" : "Muy joven para votar";
console.log(resultado3);


