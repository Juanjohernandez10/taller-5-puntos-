
peliculas = {}
import os
# Definimos una función para registrar películas en el diccionario
def fnt_registrar_pelicula(peliculas, titulo, genero, año):
    peliculas[titulo] = {"genero": genero, "año": año}

# Definimos una función para buscar películas en el diccionario
def fnt_buscar_pelicula(peliculas, titulo):
    if titulo in peliculas:
        print(f"La información de la película {titulo} es:")
        print(f"Género: {peliculas[titulo]['genero']}")
        print(f"Año: {peliculas[titulo]['año']}")
    else:
        print("No se encontró la película")

# Solicitamos al usuario que ingrese los datos de las películas
while True:
    os.system('cls')
    opciones = input(' ingrese una opcción \n1. registrar \n2. encontrar \n-> ')
    if opciones == '1':
        titulo = input("Ingrese el título de la película : ")
        genero = input("Ingrese el género de la película : ")
        año = int(input("Ingrese el año de la película : "))
        fnt_registrar_pelicula(peliculas, titulo, genero, año)
    if opciones == '2':
        titulo_busqueda = input("Ingrese el título de la película que desea buscar : ")
        fnt_buscar_pelicula(peliculas, titulo_busqueda)
        break
