# Ejercicio 7: Juego adivina el numero
# Realizar un juego para adivinar un numero. Para ello se debe
# generar un numero aleatorio entre 1-100 y luego ir pidiendo
# numeros indicando "es mayor" o "es menor" segun sea mayor o menor
# con respecto a N. El proceso termina cuando el usuario acierta
# y alli se debe mostrar el numeros de intentos
import random
print("\t.:Juego Adivina el Numero:.")
aleatorio = random.randint(0, 100)
contador = 0
while True:
    numero = int(input("Digite un numero: "))
    contador += 1
    if numero > aleatorio:
        print("\tNo es el numero, digita un numero menor: ")
    elif numero < aleatorio:
        print("\tNo es el numero, digita un numero mayor. ")
    else:
        print(f'Felicidades acabas de adivinar el numero: {aleatorio}')
        break
print(f'Adivinaste el numero en {contador} intentos')