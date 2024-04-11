inventario = {}
import os 
# Definimos una función para agregar productos al inventario
def agregar_producto(inventario, nombre, cantidad):
    inventario[nombre] = cantidad

# Definimos una función para buscar productos en el inventario
def buscar_producto(inventario, nombre):
    if nombre in inventario:
         return inventario[nombre]
    else:
        return None

# Solicitamos al usuario que ingrese los datos de los productos
while True:
    os.system ('cls')
    nombre = input("Ingrese el nombre del producto (o escriba 'fin' para terminar): ")
    if nombre == "fin":
        break
    cantidad = int(input("Ingrese la cantidad disponible del producto: "))
    agregar_producto(inventario, nombre, cantidad)

# Solicitamos al usuario que busque un producto por su nombre
nombre_busqueda = input("Ingrese el nombre del producto que desea buscar: ")

# Buscamos el producto en el diccionario
cantidad_busqueda = buscar_producto(inventario, nombre_busqueda)
if cantidad_busqueda is not None:
    print(f"La cantidad disponible del producto {nombre_busqueda} es {cantidad_busqueda}")
else:
    print("No se encontró el producto")