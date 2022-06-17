'''
miVariable = 3
print(miVariable)
miVariable = "Hola a todos los estudiantes de la Tecnicatura"
print(miVariable)
miVariable = 3.5
print(miVariable)
x = 10
y = 2
z = x + y
print(z)
print(id(x))
# las literales se escriben x872, la variable y = x616, la variable z = x936
print(id(y))
print(id(z))

# Tipos int, float, String, Bool
x = 10
print(x)
print(type(x))
x = 14.5
print(x)
print(type(x))
x = "Hola alumnos"
print(x)
print(type(x))
x = True
print(x)
print(type(x))
x = False
print(x)
print(type(x))

# Manejo de cadenas
miGrupoFavorito = "Rata Blanca:"
caracteristicas = "The Best Rock Band"
print("mi grupo favorito es: ", miGrupoFavorito, caracteristicas)

#numero1 = "7"
#numero2 = "8"
#print(int(numero1) + int(numero2))

# Tipos Booleanos
miBooleano = 3 > 2
print(miBooleano)

if miBooleano:
    print("El resultado es verdadero")
else:
    print("el resultado es falso")

# Procesar la entrada del usuario
# Funcion input
#resultado = input("Digite un numero: ")  # regresa un dato tipo string
#print(resultado)

# Conversion de la entrada de datos
numero1 = int(input("Escribe el primer numero: "))
numero2 = int(input("Escribe el segundo numero: "))
resultado = numero1 + numero2
print("El resultado de la suma es: ", resultado)
'''
"""
operandoA = 8
operandoB = 5
suma = operandoA + operandoB
#print("El resultado de la suma es: ", suma)
print(f'El resultado de la suma es: {suma}')

resta = operandoA - operandoB
print(f'El resultado de la resta es: {resta}')

multiplicacion = operandoA * operandoB
print(f'El resultado de la multiplicacion es: {multiplicacion}')

division = operandoA / operandoB
print(f'El resultado de la division es: {division}')
division = operandoA // operandoB
print(f'El resultado de la division (int) es: {division}')
modulo = operandoA % operandoB
print(f'El resultado de la division o residuo (modulo) es: {modulo}')

exponente = operandoA ** operandoB
print(f'El resultado del exponente es: {exponente}')
"""
'''
alto = int(input("Digite el alto del rectangulo: "))
ancho = int(input("Digite el ancho del rectangulo: "))
area = alto * ancho
perimetro = (alto + ancho) * 2
print(f'El area del rectangulo es: {area}')
print(f'El perimetro del rectangulo es: {perimetro}')
'''
"""
miVariable3 = 10
print(miVariable3)

# Operadores de reasignacion
miVariable3 = miVariable3 + 1
print(miVariable3)

miVariable3 += 1
print(miVariable3)

# mivariable3 = miVariable3 - 2
miVariable3 -= 2
print(miVariable3)

# mivariable3 = miVariable3 * 3
miVariable3 *= 3
print(miVariable3)

# mivariable3 = miVariable3 / 2
miVariable3 /= 2
print(miVariable3)

# Opedadores de comparacion

d = 4
b = 2
resultado = d == b
print(resultado)

# Operador diferente
resultado = d != b
print(resultado)

# Operador mayor que
resultado = d > b
print(resultado)

# Operador menor que
resultado = d < b
print(resultado)

# Operador menor o igual que
resultado = d <= b
print(resultado)

# Operador mayor o igual que
resultado = d >= b
print(resultado)
"""
'''
a = int(input('Digite un numero: '))
print(f'El residuo de la division es: {a % 2}')
if a % 2 == 0:
    print(f'El valor de a es: {a} es un numero PAR')
else:
    print(f'El valor de a es: {a} es un numero IMPAR')
'''
'''
edad = int(input('Digite un numero: '))
if edad >= 18:
    print(f'Tu edad es {edad} eres mayor de edad')
else:
    print(f'Tu edad es {edad} eres menor de edad')
'''

# Operadores logicos
'''
a = False
b = True
resultado = a and b
print(resultado)

# Operador or
resultado = a or b
print(resultado)

# Operador not
resultado = not a
print(resultado)
'''

# Ejercicio valor dentro del rango
"""
num = int(input('Digite un numero: '))
if num >= 0 and num <= 5:
    print(f'El numero {num} esta dentro del rango')
else:
    print(f' el numero {num} esta fuera del rango')
"""
# Ejercicio con el operador or, operador not
'''
vacaciones = True
diaLibre = False
if not (vacaciones or diaLibre):
    print('No puede ir debe trabajar')
else:
    print('Puede ir al juego de su hijo')
'''
'''

suEdad = int(input('Digite su edad: '))
veinte = suEdad >= 20 and suEdad < 30
print(veinte)
treinta = suEdad >= 30 and suEdad < 40
print(treinta)
if veinte or treinta:
    if veinte:
        print('Estas dentro del rango de los (20\'0)  años')
    elif treinta:
        print('Estas dentro del rango de los (30\'0) años')
else:
    print("Tu edad esta fuera del rango de los (20'0) a (30'0) años")

# Ejercicio mayor de dos numeros

numero1 = int(input('Digite un numero: '))
numero2 = int(input('Digite un numero: '))
if numero1 > numero2:
    print('El numero1 es el mayor')
else:
    print('El numero2 es el mayor')
'''
# Ejercicio Tienda de Libros
print('Digite los datos del libro: ')
nombreLibro = input('Digite el nombre del libro: ')
libroId = int(input('Digite el id del libro: '))
precio = float(input('Digite el precio del libro: '))
envioGratuito = input('Indicar si el el envio es gratis o no : ')
if envioGratuito == 'True':
    envioGratuito = True
elif envioGratuito == 'False':
    envioGratuito = False
else:
    envioGratuito = 'Valor incorrecto marque True o False: '
print(f'''
        Nombre: {nombreLibro}
        ID: {libroId}
        Precio: {precio}
        Envio: {envioGratuito}
''')




