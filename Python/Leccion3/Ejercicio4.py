suma = 0
calificacionBaja = 11
for i in range(0,10):
    calificacion = int(input('Digite una calificacion: '))
    suma = suma + calificacion

    if calificacionBaja > calificacion:
        calificacionBaja = calificacion

print("El promedio de las calificaciones es ", suma / 10)
print('La calificacion mas baja es: ', calificacionBaja)
