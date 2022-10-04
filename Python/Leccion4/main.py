# Lista Ariel Liliana Natalia Osvaldo
# Colecciones en Python

# Las listas en otros lenguajes son conocidas como arreglos o vectores

nombres = ["Naty", "Osvaldo", "Lily", "Ariel"]
print(nombres)
print(nombres[0:2]) # Solo muestra el indice 0 y 1 pero no el 2
# ir del inicio de la lista al indice (sin incluirlo)
print(nombres[ :3]) # Indices a mostrar 0, 1, 2
# Desde el ndice indicado hasta el final
print(nombres[1: ])
# Modificamos un valor
nombres[2] = 'Liliana'
nombres[0] = 'Natalia'
print(nombres)
# Iterar una lista
for nombre in nombres: # nombre es singular, la lista es plural
    print(nombre)
else:
    print('Se acabaron los elementos de la lista')

# Preguntamos cuantos elementos tiene
print(len(nombres)) # le pasamos como parametro la lista

# Agregamos un elemento
nombres.append('Marcelo')
nombres.append([1, 2, 3])
nombres.append(True)
nombres.append(10.45)
nombres.append([4, 5])
nombres.append(7)
print(nombres)

# Insertar un elemento en un indice especifico
nombres.insert(1, 'Alberto')
print(nombres)
nombres.insert(3, 'Debora')
print(nombres)

# Eliminamos un elemento
nombres.remove('Alberto')
print(nombres)

# Eliminar el ultimo elemento
nombres.pop()
print(nombres)

# Eliminamos un indice especifico
del nombres[2] #del significa delete (eliminar)
print(nombres)

# Eliminar borrar o limpiar todos los elementos
nombres.clear()
print(nombres)

# Eliminar la lista
del nombres
# print(nombres) #Aqui mostrara un error

# Definimos una Tuplas
cocina = ('cuchara', 'cuchillo', 'tenedor')
print(len(cocina))

# Acceder a un elemento, para esto utilizamos corchetes no parentesis
print(cocina[0])
# Mostrar de manera inversa
print(cocina[-1])

# Acceder a un rango
print(cocina[0 : 2])

# Ejemplo
verduras = ('papa',) # Una tupla necesita aunque sea de un elemeto la coma
# de lo contrario solo seria un tipo str cadena

# Recorremos los elementos de una tupla
for cocinar in cocina: # print esta usando \n para saltos de lineas
    print(cocinar, end=' ') # Usamos end= para eliminar los saltos de linea

cocinaLista = list(cocina)
cocinaLista[0] = 'plato'
cocina = tuple(cocinaLista)
print('\n', cocina)

# del cocina esto es para eliminar una tupla

# Tipo set
planetas = {'Marte', 'Jupiter', 'Venus'}
print(len(planetas)) # Usamos la funcion len = length significa largo

# Revisar si un elemento esta dentro de set
print('Marte' in planetas)

# Agregamos un elemento
planetas.add('Tierra') # Add es una funcion para añadir en conjuntos
print(planetas)

# Eliminar elementos, puede arrojar error si el elemento no existe
planetas.remove('Jupiter') # Esta funcion ante un mal ingreso u inexistencia del elemento da error
print(planetas)
planetas.discard('tierra') # Esta funcion no nos presenta ningun tipo error
print(planetas)

# Limpiar set
planetas.clear()
print(planetas)

# Eliminar set
# del planetas
# print(planetas) # Al eleiminar el set nos muestra un error

# 'maradona': 10 <- Un diccionario esta compuesto por dos elementos
# UNA LLAVE Y UN VALOR
# dict(key, value)
diccionario = {
    'IDE':'Integrated Development Environment',
    'POO':'Programacion Orientada a Objetos',
    'SABD':'Sistema de Administracion de Base de Datos'
}
# Verificar la cantidad de elementos del diccionario
print(diccionario)
print(len(diccionario))

# Acceder a un diccionario con la llave(key)
print(diccionario['IDE'])

# Otra forma de recuperar un elemento
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

# Modificar los elementos
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

# Como recorrer los elementos
for termino in diccionario: # Recorremos mostrando solo las llaves
    print(termino)


for termino, valor in diccionario.items(): # Con la funcion .items podemos recorrer tanto las llaves con su valor
    print(termino, valor)

# Otras maneras de acceder a un diccionario
for termino in diccionario.keys():
    print(termino) # Muestra solo las llaves

for valor in diccionario.values(): # Usamos una funcion para acceder a los valores
    print(valor)

# Comprobar la existencia de un elemento
print('IDE' in diccionario) # devuelve un valor booleano

# Agregar un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)

# Eliminar un elemento
diccionario.pop('SABD')
print(diccionario)

# Vaciar un diccionario
diccionario.clear()
print(diccionario)

# Eliminar diccionario
del diccionario

# Concatenamos listas
lista1 = [1, 2, 3, 1]
lista2 = [4, 5, 6, 1]
lista3 = lista1+lista2 # Concatenacion
print(lista3)

lista3.extend([7, 8, 9, 1]) # Funcion para agregar varios elementos a la lista
print(lista3)

print(lista3.index(5)) # Funcion para ubicar en que indice esta el valor ingresado
# print(lista3.index(0)) esto nos daria un error  por no ser el elemento parte de la lista

# Como saber cuantos valores repetidos hay dentro de la lista
print(lista3.count(1)) # Cuenta cuantos valores iguales estan dentro de la lista

# Para poner al reves una lista
lista3.reverse()
print(lista3)

# Para que una lista se multiplique repitiendo sus elemantos
lista3 = lista3 * 2
print(lista3)

# Metodo de ordenamiento en Python con funcion
lista3.sort() # Ordena los elementos ascendentemente
print(lista3)
lista3.sort(reverse=True) # Ordena descendentemente
print(lista3)

# Repaso de Tuplas
tupla = (4, 'Hola', 6.78, [1, 2, 78], 4, 'Hola') # Puede tener diferentes tipos de datos dentro
print(tupla)

print(4 in tupla) # Accion booleana, su respuesta es de tipo booleano
# Lo que podemos usar dentro de tuplas son: index, count, len
# En tuplas se puede convertir de tupla a lista y viceversa

# Repaso de seto conjunto
# para definir un conjunto
conjunto2 = set()
conjunto1 = {'bye', } # Con las llaves {} solas no se pueden inicializar un conjunto
conjunto2.add(7)
conjunto2.add('Hola')
print(conjunto2)
conjunto1.add('hola')
print(conjunto1)
print(3 not in conjunto1) # Preguntamos si el numero 3 no esta dentro del conjunto

# Como hacer la igualdad de dos conjuntos
print(conjunto1 == conjunto2) # Nos devuelve una respuesta booleana

# Operaciones en conjuntos
conjunto3 = conjunto1 | conjunto2 # La linea une los conjuntos
print(conjunto3)

conjunto3 = conjunto1 & conjunto2 # Que elemento tienen en comun
print(conjunto3)

conjunto3 = conjunto1 - conjunto2 # Asigna el valor que esta en el conjunto1 y no en el conjunto2
print(conjunto3)
conjunto3 = conjunto2 -conjunto1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2 # Elementos que no comparten o que son diferentes entre los conjutos
print(conjunto3)
# quede en la clase 3 por ver video 20
conjunto3 = conjunto1 | conjunto2
print(conjunto2.issubset(conjunto3)) # Aqui preguntamos si un conjunto es subconjunto de otro
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))

print(conjunto3.issuperset(conjunto1)) # Preguntamos si los elementos del conjunto1 y conjunto2 estan dentro del 3
print(conjunto3.issuperset(conjunto2)) # Si es verdadero quiere decir que el conjunto3 es un superconjunto
print(conjunto2.issuperset(conjunto3))

# Como saber si ambos conjuntos son disconexos, esto es si no comparten elementos en comun
print(conjunto1.isdisjoint(conjunto2)) # No hay cosas en comun

# Convertir un conjunto totalmente en inmutable
conjunto1 = frozenset # Esta funcion hace que el conjunto sea totalmente inmutable
# No se puede agregar, modificar ni eliminar elementos del conjunto

# Repaso Diccionarios
diccionarioNuevo = {'Azul': 'Blue', 'Rojo': 'Red', 'Verde': 'Green', 'Amarillo': 'Yellow'}
print(diccionarioNuevo)

# Como eliminar
del (diccionarioNuevo['Azul'])
print(diccionarioNuevo)

# Los diccionarios pueden almacenar diferentes tipos de datos
diccionario2 = {'Ariel': {'Edad': 40, 'Altura': 1.83}, 'Osvaldo': [45, 1.85], 'Natalia': [35, 1.67]}
print(diccionario2)

seleccionArgentina = {
    10: {'Nombre': 'Lionel Messi', 'Edad': 35, 'Altura': 1.70, 'Precio': '50 Millones', 'Posicion': 'Extremo Derecho'},
    11: {'Nombre': 'Angel Di Maria', 'Edad': 34, 'Altura': 1.80, 'Precio': '12 Millones', 'Posicion': 'Extremo Derecho'},
    21:{'Nombre': 'Paulo Dybala', 'Edad': 28, 'Altura': 1.77, 'Precio': '35 Millones', 'Posicion': 'Media Punta'},
    19: {'Nombre': 'Nicolas Otamendi', 'Edad': 34, 'Altura': 1.83, 'Precio': '3.5 Millones', 'Posicion': 'Defensor Central'},
    1: {'Nombre': 'Franco Armani', 'Edad': 35, 'Altura': 1.89, 'Precio': '3.5 Millones', 'Posicion': 'Arquero'},
    27: {'Nombre': 'Julian Alvarez', 'Edad': 22, 'Altura': 1.70, 'Precio': '51 Millones', 'Posicion': 'Delantero'},
    8: {'Nombre': 'Marcos Acuña', 'Edad': 30, 'Altura': 1.72, 'Precio': '15 Millones', 'Posicion': 'Defensor'},
    25: {'Nombre': 'Lisandro Martinez', 'Edad': 24, 'Altura': 1.75, 'Precio': '50 Millones', 'Posicion': 'Defensor'},
    22: {'Nombre': 'Lautaro Martinez', 'Edad': 25, 'Altura': 1.74, 'Precio': '106 Millones', 'Posicion': 'Delantero'}
} # Agregamos como tarea a los jugadores: Lautaro Martinez, Marcos Acuña, Lisandro Martinez y a Julian Alvarez
print(seleccionArgentina)

for llave, valor in seleccionArgentina.items():
    print(llave, valor)

# Como tarea agregar por lo menos 4 jugadores mas al diccionario: seleccionArgentina
print('Tenems cargados en el diccionario la cantidad de jugadores: ', end=' ')
print(len(seleccionArgentina))

# Pilas usando listas
pila = [1, 2, 3]
print(pila)
# Agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

# Sacamos elementos desde el final
elementoBorrado = pila.pop() # Quita el elemento y guarda en la variable
print(f'sacamos el elemento {elementoBorrado}')
print(f'La pila ahora quedo asi: {pila}')

# Colas con listas
# Estructura de datos de tipo fifo (first input/ first output)
cola = ['Ariel', 'Osvaldo', 'Liliana', 'Pilar']

# Agregamos elementos al final de la cola
cola.append('Natalia')
cola.append('Jose')
print(cola)

# Sacamos elementos de le cola
seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

# Seguimos mostrando como recorrer un diccionario con el ciclo for
for i in seleccionArgentina:
    print(f'{i} -> {seleccionArgentina[i]}')
