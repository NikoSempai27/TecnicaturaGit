'''
Sintaxis de range(inicio<opcional>, fin <requerido>, incremento <opcional>)
Ejercicio 1: Iterae un rango de 0 al 10 e imprimir los numeros divisibles por 3
Ejemplo 0, 3, 6, 9
'''

for i in range(0 , 10):
    if (i % 3 == 0 ):
        print(i)
'''
Ejercicio 2: Crear un rango de numeros de 2 al 7 e imprimirlos
Ejemplo: 2, 3, 4, 5, 6
'''
numeros = []
for i in range(2 , 7):
    numeros.append(i)
print(numeros)
'''
Ejercicio 3: Crear un rango de 3 al 10 con un incremento de 2 en 2, 
Ejemplo: 3, 5, 7, 9
'''
for i in range(3 , 10, 2):
    print(i)

