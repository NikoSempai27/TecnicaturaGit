# Ejercicio 1: Eliminar duplicados de una lista
# Escribir un programa donde tenga una lista y que a continuacion
# elimine los elementos repetidos, por ultimo mostrar la lista.

#Creamos una lista
lista = [1, 2, 3, "Ariel", 7, 7, 3, "Alberto", 1, "Ariel", 2, "Alberto"]
# conjunto = set(lista)
# lista = list(conjunto)
lista = list(set(lista))
print(lista)