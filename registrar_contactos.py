contactos = {}
import os

sw = True
# Solicitamos al usuario que ingrese los datos de los contactos
while sw ==True:
    os.system('cls')
    nombre = input("Ingrese el nombre del contacto (o escriba 'fin' para terminar): ")
    if nombre == "fin":
        break
    telefono = input("Ingrese el número de teléfono del contacto: ")
    contactos[nombre] = telefono

# Solicitamos al usuario que busque un contacto por su nombre
nombre_busqueda = input("Ingrese el nombre del contacto que desea buscar: ")

# Buscamos el contacto en el diccionario
if nombre_busqueda in contactos:
    telefono_busqueda = contactos[nombre_busqueda]
    print(f"El número de teléfono del contacto {nombre_busqueda} es {telefono_busqueda}")
else:
    print("No se encontró el contacto")
