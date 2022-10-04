# Ejercicio 2: Operaciones de Conjuntos con Listas
# Escriba un programa que tenga 2 listas y que a continuacion
# cree las siguientes listas (en las que no deben haber repeticion)
# 1 Lista de palabras que aparecen en las listas
# 2 Listas de palabras que aparecen en la primera lista, pero no en la segunda
# 3 Lista de palabras que aparecen en la segunda lista, pero no en la primera
# 4 Lista de palabras que aparecen en ambas listas

lista1 = [1, 2, 3, 4, 5, 4, 3, 2, 2, 1, 5]
lista2 = [4, 5, 6, 7, 8, 4, 5, 6, 7, 7, 8]

# Pasamos a eliminar los elementos repetidos de cada lista (convertimos a conjunto)
conjunto1 = set(lista1)
conjunto2 = set(lista2)

unirConjuntos = list(conjunto1 | conjunto2)
leer1 = list(conjunto1 - conjunto2)
leer2 = list(conjunto2 - conjunto1)
ambas = list(conjunto1 & conjunto2)
print(f"Lista de palabras que aparecen en las listas: {unirConjuntos}")
print(f"Listas de palabras que aparecen en la primera lista, pero no en la segunda: {leer1}")
print(f"Lista de palabras que aparecen en la segunda lista, pero no en la primera: {leer2}")
print(f"Lista de palabras que aparecen en ambas listas: {ambas}")