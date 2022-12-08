class Vehiculo:
    '''
    Definir una clase padre llamada Vehiculo y dos clases hijas llamadas
    Auto y Bicicleta, las cuales heredan de la clase pade Vehiculo. La clase
    padre debe tener los siguientes atributos y metodos:

    Vehiculo (clase padre)
    -Atributos(color, ruedas)
    -Metodos(__init__(color, ruedas) y __str__())

    Auto(clase hija de Vehiculo)
    -Atributos(velocidad(km/hr))
    -Metodos(__init__(color, ruedas, velocidad) y __str__())

    Bicicleta(clase hija de Vehiculo)
    -Atributos(tipo(urbana/montaña/etc.)
    -Metodos(__init__(color, ruedas, tipo) y __str__())

    Crear un objeto para cada clase
    '''
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return 'Color: '+self.color+', Ruedas: '+str(self.ruedas)

class Auto(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return super().__str__()+', Velocidad km/h: '+str(self.velocidad)


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__()+', Tipo: '+self.tipo


# Primer objeto
vehiculo = Vehiculo('Azul', 4)
print(vehiculo)

# Segundo objeto
auto = Auto('negro', 4, 230)
print(auto)

# Tercer objeto
bicicleta = Bicicleta('Roja', 2, 'Montaña')
print(bicicleta)
