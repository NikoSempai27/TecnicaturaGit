anio = int(input('Digite un año: '))
while True:
    if anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0:
        print('El anio es biciesto')
    else:
        print('El anio no es biciesto')
    opcion = int(input("Ingresar una opcion: "))
    if opcion == 1:
        continue
    else:
        break