from Orden import Orden
from Producto import Producto

producto1 = Producto('Camiseta', 100.00)
producto2 = Producto('Pantalon', 150.00)
producto3 = Producto('Gorra', 70.00)
producto4 = Producto('Campera', 250.00)
producto5 = Producto('Buzo', 300.00)
producto6 = Producto('Medias', 45.00)
producto7 = Producto('Sweter', 95.00)
producto8 = Producto('Blusa', 75.00)

productos1 = [producto1, producto2]  # Lista de productos
orden1 = Orden(productos1)  # Primer objeto orden pasando la lista de productos
orden1.agregar_producto(producto6)
orden1.agregar_producto(producto8)
print(orden1)
print(f'Total de la orden1: {orden1.calcular_total()}')
productos2 = [producto3, producto4, producto5]
orden2 = Orden(productos2)
orden2.agregar_producto(producto7)
orden2.agregar_producto(producto6)
print(orden2)
print(f'Total de la orden2: {orden2.calcular_total()}')