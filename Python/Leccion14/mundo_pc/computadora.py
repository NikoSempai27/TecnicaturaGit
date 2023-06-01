from mundo_pc.monitor import Monitor
from mundo_pc.raton import Raton
from mundo_pc.teclado import Teclado


class Computadora:

    contador_computadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadoras += 1
        self._id_computadora = Computadora.contador_computadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self):
        return f'''
        Nombre: {self._nombre} Id: {self._id_computadora} 
        Monitor: {self._monitor}
        Teclado: {self._teclado}
        Raton: {self._raton}
        '''

#Hacemos una prueba
if __name__ == '__main__':
    teclado1 = Teclado('HP', 'USB')
    raton1 = Raton('HP', 'USB')
    monitor1 = Monitor('HP', '15 Pulgadas')
    computadora1 = Computadora('HP', monitor1, teclado1, raton1)
    print(computadora1)

    raton2 = Raton('Acer', 'Bluetooth')
    teclado2 = Teclado('Gamer', 'Bluetooth')
    monitor2 = Monitor('Acer', '27 Pulgadas')
    computadora2 = Computadora('Acer', monitor2, teclado2, raton2)
    print(computadora2)