# En esta clase veremos la sentencia if/else
"""
condicion = True
if condicion == True:
    print('Condicion Verdadera')
elif condicion == False:
    print('Condicion Falsa')
else:
    print('Condicionn sin especificar')
"""
'''
num = int(input('Digite un numero en el rango del 1 al 3: '))
numTexto = ''
if num == 1:
    numTexto = 'Numero uno'
elif num == 2:
    numTexto = 'Numero dos'
elif num == 3:
    numTexto = 'Numero tres'
else:
    numTexto = 'Has ingresado un numero fuera del rango'
print(f'El numero ingresado es: {num} - {numTexto}')
'''

condicion = True
# if condicion:
#     print('Condicion Verdadera')
# else:
#     print('Condicion Falsa')

print('Condicion Verdadera') if condicion else print('Condicion Falsa')







