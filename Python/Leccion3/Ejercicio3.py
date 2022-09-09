conteoPositivos = 0
conteoNegativos = 0
conteoNeutros = 0

for i in range(0,10):
    num = int(input("Digite un numero: "))
    if num > 0:
        conteoPositivos +=1
    elif num < 0:
        conteoNegativos +=1
    else:
        conteoNeutros +=1

print("La cantidad de numeros positivos es: ", conteoPositivos)
print("La cantidad de numeos negativos es: ", conteoNegativos)
print("La cantidad de numeros neutros es: ", conteoNeutros)