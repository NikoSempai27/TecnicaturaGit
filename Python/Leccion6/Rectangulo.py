class Rectangulo:
    """
    Crear una clase llamada rectangulo, debe tener 2 atributos: altura y base
    el nombre del metodo sera calcular area utilizando la formula:
    area = base * altura. Pero la base y la altura deben ser ingresadas por
    el usuario y los objetos deben se tres
    """

    def __init__(self, altura, base):
        self.altura = altura
        self.base = base

    def calcular_area(self):
        return self.altura * self.base

# Pedimos al usuario que nos ingrese los valores para los tres rectangulos
altura1 = int(input('Digite el valor para la altura: '))
base1 = int(input('Digite el valor para la base: '))

altura2 = int(input('Digite el valor para la altura: '))
base2 = int(input('Digite el valor para la base: '))

altura3 = int(input('Digite el valor para la altura: '))
base3 = int(input('Digite el valor para la base: '))

# Creamos los tres objetos
rectangulo1 = Rectangulo(altura1, base1)
print(f'El area del primer rectangulo es: {rectangulo1.calcular_area()}')

rectangulo2 = Rectangulo(altura2, base2)
print(f'El area del segundo rectangulo es: {rectangulo2.calcular_area()}')

rectangulo3 = Rectangulo(altura3, base3)
print(f'El area del tercer rectangulo es: {rectangulo3.calcular_area()}')

# Quede ppor ver el video 75 de la clase 9 de Python y por empezar la clase 8 de Java

