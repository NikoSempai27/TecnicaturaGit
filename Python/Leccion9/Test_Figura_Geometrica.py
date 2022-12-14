from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

cuadrado1 = Cuadrado(5, 'Azul')
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(f'El cuadrado es de color: {cuadrado1.color}')
print(f'Calculo del Area del cuadrado: {cuadrado1.calcular_area()}')

# MRO = Method Resolution Order
print(Cuadrado.mro())

print(cuadrado1)

rectangulo1 = Rectangulo(3, 8, 'Amarillo')
print(f'Calcular el area del rectangulo: {rectangulo1.calcular_area()}')
print(rectangulo1)