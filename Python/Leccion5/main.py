# Comenzamos con Funciones
# mi_funcion() # No se puede llamar a una funcion antes de definirla
# Definimos una Funcion
def mi_funcion(): # Para identificar a la funcion utilizamos parentesis
    print('Saludos a todos los alumnos de la Tecnicatura')

mi_funcion() # Estamos llamando a la funcion
mi_funcion() # Se puede llamar a una funcion N cantidad de veces

# Desempaquetado de listas o list Unpacking
def show(name, lastname):
    print(name+' '+lastname)
person = ["Nicolas", "Guala"]
show(person[0], person[1]) # Pasamos uno por uno los datos de la lista a la funcion
show(*person) # Esto es lo mismo que lo anterior pero le pasamos todo junto
person2 = ("Claudia", "Guala") # desempaquetamos a traves de una tupla
show(*person2)
person3 = {"lastname": "Guala", "name": "Marcela"}
show(**person3)

numbers = [1, 2, 3, 4, 5] # Aunque este vaia la lista el else se mostraria igual
for n in numbers:
    print(n)
    if n == 3:
        break # Esta es la unica manera para que no se mostrase el else
else:
    print('Esto se termino: ')

# List comprehension
names = ["Paolo", "Rodrigo", "Lupe", "Pepe"]
alongP = [p for p in names if p[0] == 'P']
print(alongP)

bottleC = [{"name": "Quilmes", "country": "Arg"},
           {"name": "Corona", "country": "Mx"},
           {"name": "Stella Artois", "country": "Belgium"},
           ]
Arg = [b for b in bottleC if b["country"] == "Arg"]
print(Arg)
print(bottleC)

# Paso de Argumentos (Funciones)
def mi_funcion2(name, lastname): # aca definimos parametros a la funcion
    print("Saludos a todos los que ven a traves del canal de YouTube: ")
    print(f'Nombre: {name}, apellido: {lastname}')
mi_funcion2('Pablo', 'Guala') # aca le damos los argumentos o valores a la fucion
mi_funcion2('Claudia', 'Guala')
mi_funcion2('Joaquin', 'Guala')

# La palabra return en funciones
# Creamos una funcion para sumar
def sumar(a, b):
    return a + b
# resultado = sumar(78, 22)
# print(f'El resultado de la suma es: {resultado}')
print(f'El resultado de la suma es: {sumar(55, 45)}')

def sumar2(a = 0, b = 0):
    return a + b
resultado = sumar2()
print(f'Resultado de la suma: {resultado}')
print(f'Resultado de la suma: {sumar2(22, 66)}')

# Argumentos variables en funciones
def listarNombres(*nombres): # Normalmente se utiliza *args
    for nombre in nombres: #Se va a convertir en una tupla
        print(nombre)
listarNombres('Lucas', 'Jose', 'Claudia', 'Rosa', 'Maria')
listarNombres('Marcos', 'Daniel', 'Romina', 'Marcela', 'Carlos')