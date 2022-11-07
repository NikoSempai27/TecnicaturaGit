class Cubo:
    """
    Crear la clase Cubo con los atributos, ancho, alto y profundidad con
    un metodo calcular_volumen que tendra la formula
    volumen = ancho * alto * profundidad
    que el usuario ingrese los valores
    """

    def __init__(self, ancho, alto, profundidad):
        self.ancho = ancho
        self.alto = alto
        self.profundidad = profundidad

    def calcular_volumen(self):
        return self.ancho * self.alto * self.profundidad


# Pedimos al usuario que ingrese los valores para el cubo
ancho = int(input('Digite un valor para el ancho: '))
alto = int(input('Digite un valor para el alto: '))
profundidad = int(input('Digite un valor para la profundidad: '))

# Creamos el objeto
cubo = Cubo(ancho, alto, profundidad)
print(f'El volumen del cubo es: {cubo.calcular_volumen()}')
