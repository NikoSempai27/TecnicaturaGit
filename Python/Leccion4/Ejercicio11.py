# Ejercicio 11: Agenda telefonica
# Hacer un programa que simule una agenda de contactos. Crear un
# diccionario donde la clave sea nombre del usuario y el valor
# sea el telefono, el programa tendra el siguiente menu de opciciones
#      1. Nuevo contacto
#      2. Borrar contacto
#      3. Ver contactos existentes
#      4. Salir
agenda = {}
while True:
    print('\t.:MENU:.')
    print('1. Nuevo contacto')
    print('2. Borrar contacto')
    print('3. Ver contactos existentes')
    print('4. Salir')
    opcion = int(input('Digite una opcion: '))
    if opcion == 1:
        nombre =input('Digite el nombre del contacto: ')
        telefono = input('Digite el numero: ')
        if nombre not in agenda:
            agenda[nombre] = telefono
            print('Contacto agregado: ')
        else:
            print('Este contacto ya existe: ')
    elif opcion == 2:
        nombre = input('Cual es el nombre del contacto: ')
        if nombre in agenda:
            del(agenda[nombre])
            print('El contacto se elimino exitosamente: ')
        else:
            print('Este contacto no existe en su agenda: ')
    elif opcion == 3:
        print('Agenda de Contactos:')
        for clave, valor in agenda.items():
            print(f'Nombre: {clave}, Telefono: {valor}')
    elif opcion == 4:
        print('Gracias por utlizar su agenda de contactos')
        break
    else:
        print('Opcion incorrecta:')
        print()