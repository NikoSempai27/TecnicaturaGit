class Persona2:
    def __init__(self, nombre, apellido, edad):  # Esta encapsulado
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalle(self):
        print(f'Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}')

    @property  # decorador
    def nombre(self):  # Metodo Getter
        print('Estamos usando el metodo get')
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):  # Metodo Setter
        print('Estamos usndo el metodo set')
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def __del__(self):
        print(f'Persona2: {self._nombre} {self._apellido} {self._edad}')


if __name__ == '__main__':
    persona1 = Persona2("Ariel", "Betancud", 41)
    # print(persona1._nombre) <- eso esta mal no debemos hacerlo, indica que no sabemos nada de la sintaxis de Python
    print(persona1.nombre)  # Llamamos al metodo Getter
    print(persona1.apellido)
    print(persona1.edad)

    persona1.nombre = 'Juan Pedro'  # Llamamos al metodo Setter
    print(persona1.nombre)  # Otra vez con el metodo Getter
    print(persona1.mostrar_detalle())  # Llamamos al metodo mostrar detalle
    # Atributo read-only seria la edad porque no tiene metodo Setter
    print(persona1.edad)
    # Tarea crear tres objetos mas, utilizando los metodos getter and setter
    # para modificar y mostrar los cambios con el metodo mostrar detalle

    # Creamos el objeto y pasamos sus parametros
    persona2 = Persona2('Horacio', 'Lagraña', 70)
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2.edad)
    # Hacemos la modificacion
    persona2.nombre = 'Joaquin'
    persona2.apellido = 'Zuniga'
    persona2.edad = 17
    print(persona2.mostrar_detalle())

    # Creamos el objeto y pasamos sus parametros
    persona3 = Persona2('Marcela', 'Guala', 35)
    print(persona3.nombre)
    print(persona3.apellido)
    print(persona3.edad)
    # Hacemos la modificacion
    persona3.nombre = 'Mateo'
    persona3.apellido = 'Brusco'
    persona3.edad = 18
    print(persona3.mostrar_detalle())

    # Creamos el objeto y pasamos sus parametros
    persona4 = Persona2('Javier', 'Garrido', 30)
    print(persona4.nombre)
    print(persona4.apellido)
    print(persona4.edad)
    # Hacemos la modificacion
    persona4.nombre = 'Claudia'
    persona4.apellido = 'Guala'
    persona4.edad = 57
    print(persona4.mostrar_detalle())

    print(__name__)
