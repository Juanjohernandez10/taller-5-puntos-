# Creamos un diccionario vacío para almacenar la información de los estudiantes
estudiantes = {}
import os

# Definimos una función para agregar estudiantes al diccionario
def agregar_estudiante(estudiantes, nombre, edad, carrera):
    estudiantes[nombre] = {"edad": edad, "carrera": carrera}

# Definimos una función para buscar estudiantes en el diccionario
def buscar_estudiante(estudiantes, nombre):
    if nombre in estudiantes:
        print(f"La información del estudiante {nombre} es:")
        print(f"Edad: {estudiantes[nombre]['edad']}")
        print(f"Carrera: {estudiantes[nombre]['carrera']}")
    else:
        print("No se encontró el estudiante")

# Solicitamos al usuario que ingrese los datos de los estudiantes
while True:
    os.system('cls')
    opciones = input (' ingrese una opcuion \n1. registrar \n2. encontrar \n-> ')
    if opciones  == '1':
        nombre = input("Ingrese el nombre del estudiante : ")
        edad = int(input("Ingrese la edad del estudiante: "))
        carrera = input("Ingrese la carrera del estudiante: ")
        agregar_estudiante(estudiantes, nombre, edad, carrera)
    if opciones == '2':
        nombre_busqueda = input("Ingrese el nombre del estudiante que desea buscar: ")
        buscar_estudiante(estudiantes, nombre_busqueda)
        break 