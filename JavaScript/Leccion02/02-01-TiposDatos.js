//Tipo de Datos en JavaScript
/*
La sintaxis en lo que es comentario
es muy similar a la de Java 
realmente diriamos que es identica
*/

var nombre = 'Ariel'; //Tipo Str
console.log(typeof nombre);
nombre = 7;
console.log(typeof nombre);
nombre = 12.3;
console.log(typeof nombre);
var numero = 3000; // Tipo numerico
console.log(numero);

var objeto = {
    nombre : "Ariel",
    apellido : "Betancud",
    telefono : "264831058"
}
console.log(objeto);

// Tipo de Datos booleanos
var bandera = true;
console.log(bandera);

//Tipo de Datos Funcion
function miFuncion(){}
console.log(typeof miFuncion);

// Tipo de Datos Symbol
var simbolo = Symbol("Mi simbolo");
console.log(typeof simbolo);

//Tipo de Datos Clase
class Persona{
    constructor(nombre,apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
}

console.log(typeof Persona);

