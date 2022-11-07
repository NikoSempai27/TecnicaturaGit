class Persona: # Creamos la clase
    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs): # Se lo llama metodo init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self._dni = dni # Este atributo esta encapsulado de una manera sugerida
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostrar_detalle(self): # self es igual que this
        print(f'La clase Persona tiene los siguientes datos: {self.nombre} {self.apellido} {self._dni} {self.edad}, la direccion es: {self.args}, los datos importantes son: {self.kwargs} ')


persona1 = Persona('Ariel', 'Betancud', 32846257, 40) # Necesitamos enviar argumentos
# print(persona1.nombre) # Tearea: hacer el print igual que con el objeto2
# print(persona1.apellido)
# print(persona1.edad)
print(f'El objeto1 de la clase persona es: {persona1.nombre} {persona1.apellido} y su edad es: {persona1.edad}')

persona2 = Persona('Osvaldo', 'Giordanini', 30321456, 45)
print(f'El objeto2 de la clase persona es: {persona2.nombre} {persona2.apellido} y su edad es: {persona2.edad}')

persona1.nombre = 'Liliana'
persona1.apellido = 'Buccella'
persona1.edad = 40
print(f'El objeto1 de la clase persona es: {persona1.nombre} {persona1.apellido} y su edad es: {persona1.edad}')

# Los atributos son: caracteristicas
# Los metodos son: el comportamiento que van a tener los objetos (acciones)
persona1.mostrar_detalle() # La referencia en este caso se pasa de manera automatica
persona2.mostrar_detalle()

# Persona.mostrar_detalle(persona1) # Debemos pasarle una referencia para el self o dara error
persona1.telefono = '44445555289'
print(f'este es el telefono de : {persona1.nombre}  {persona1.telefono}')

# print(persona2.telefono) el objeto no tiene este atributo, da error
persona3 = Persona('Rogelio', 'Romero', 35789456, 22, 'Tefefono', '2614445557', 'Calle Lopez', 823, 'Manzana', 77, 'Casa', 18, Altura=1.83, Peso=105, CFavorito='Azul', Auto='Citroen', Modelo=2021 )
persona3.mostrar_detalle()
# print(persona3._dni) esto no se debe utilizar (esta encapsulado), esto dice que desconocemos Python
# persona3.__nombre esta totalmente encapsulado No se puede modificar

persona4 = Persona('Claudia', 'Guala', 57, 'Tefefono', '15537758', 'Calle San Juan', 162, 'Manzana', 5, 'Casa', 14, Altura=1.67, Peso=53, CFavorito='Rojo', Auto='Renault', Modelo=2022)
persona4.mostrar_detalle()




