var nombre = 'Jose';
var apellido = 'Montes';
var nombreCompleto = nombre+' '+apellido; //Primera Concatenacion
console.log(nombreCompleto);
var nombreCompleto2 = 'Ariel'+' '+'Betancud'; //Segunda concatenacion
console.log(nombreCompleto2);
var juntos = nombre + 219; //Lee de izq a der siguiendo la cadena lee elnumero como str
console.log(juntos);
juntos = nombre + 78 +17; // Aqui se puede diferenciar a traves de los parentesis
console.log(juntos);
juntos = 78 + 17 + nombre;
console.log(juntos)

nombre += apellido; //Tercera concatenacion usando el operador simplificado
console.log(nombre);
