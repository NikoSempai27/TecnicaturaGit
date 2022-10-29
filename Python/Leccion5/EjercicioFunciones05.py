# Ejercicio 5: Convertidor de temperaturas
# Realizar dos funciones para convertir de grados celsius
# a fahrenheit y viserversa
# Investigar la formula

# Convertidor 1 de Celsius a Fahrenheit
def celsius_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

# Convertidor 2 de Fahrenheit a Celsius
def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) *5 / 9

celsius = float(input('Digite un valor para celsius: '))
resultado = celsius_fahrenheit(celsius)
print(f'{celsius} de C. a F. -> {resultado:.2f}')

fahrenheit  = float(input('Digite un valor para fahrenheit: '))
resultado = fahrenheit_celsius(fahrenheit)
print(f'{fahrenheit} de F. a C. -> {resultado:.2f}')