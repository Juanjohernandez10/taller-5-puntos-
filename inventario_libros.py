libros = {}
import os
# Definimos una función para registrar películas en el diccionario
def fnt_registrar_libro(libros,titulo , autor, genero, ):
    libros[titulo] = {"genero": genero, "autor": autor}

# Definimos una función para buscar películas en el diccionario
def fnt_buscar_libro(libros, titulo):
    if titulo in libros :
        print(f"La información del libro  {titulo} es:")
        print(f"Género: {libros[titulo]['genero']}")
        print(f"autor: {libros[titulo]['autor']}")
    else:
        print("No se encontró el libro")

# Solicitamos al usuario que ingrese los datos de las películas
while True:
    os.system('cls')
    opciones = input(' ingrese una opcción \n1. registrar \n2. encontrar \n-> ')
    if opciones == '1':
        titulo = input("Ingrese el título del libro  : ")
        genero = input("Ingrese el género del libro  : ")
        autor = (input("Ingrese el autor del libro : "))
        fnt_registrar_libro(libros , titulo, autor,genero)
    if opciones == '2':
        titulo_busqueda = input("Ingrese el título deñ titulo  que desea buscar : ")
        fnt_buscar_libro(libros, titulo_busqueda)
        break