# Ejercicio Etapas de la Vida segun la edad
edad = int(input('Digite su Edad: '))
mensaje = None
if 0 <= edad < 10:
    mensaje = 'La infancia es increible y bella'
elif 10 <= edad < 20:
    mensaje = 'Tienes muchos cambios, mucho que estudiar'
elif 20 <= edad < 30:
    mensaje = 'Amor y comienza el trabajo'
elif 30 <= edad < 40:
    mensaje = 'Llega el primer bebe, noches sin dormir'
else:
    mensaje = 'Error Etapa de vida no reconocida'
print(f'Tu edad es {edad}, {mensaje} ')
