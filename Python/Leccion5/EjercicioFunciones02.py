# Ejercicio 2: Funcion con * ars para multiplicar
# Crear una funcion para multiplicar los valores recibidos
# de tipo numerico, utilizando argumentos variables +args
# como parametros de la funcion y regresar como resultado
# la multiplicacion de todos los valores pasados como argumentos

# Definimos la funcion
def multiplicar_valores(*numeros):
    resultado = 1
    for numero in numeros:
        resultado *= numero
    return resultado



# Llamamos a la funcion
print(multiplicar_valores(3, 5, 15, 3))


