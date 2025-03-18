import json
from collections import defaultdict

def cargar_peliculas():
    with open('peliculas.json', 'r') as file:
        return json.load(file)['peliculas']


# 1. Listar información
def listar_titulos_y_anios(peliculas):
    print("Títulos y años de lanzamiento:")
    for pelicula in peliculas:
        print(f"Título: {pelicula['titulo']}, Año: {pelicula['anio']}")


# 2. Contar información (modificado)
def contar_peliculas_por_genero(peliculas):
    conteo_generos = defaultdict(int) 
    for pelicula in peliculas:
        for genero in pelicula['genero']:
            conteo_generos[genero] += 1
            
    print("\nCantidad de películas por género:")
    for genero, cantidad in conteo_generos.items():
        print(f"{genero}: {cantidad}")


# 3. Buscar o filtrar información
def buscar_peliculas_por_anio(peliculas):
    anio = int(input("Introduce un año: "))
    print(f"Películas lanzadas en {anio}:")
    for pelicula in peliculas:
        if pelicula['anio'] == anio:
            print(f"- {pelicula['titulo']}")


# 4. Buscar información relacionada
def buscar_peliculas_por_actor(peliculas):
    actor_busqueda = input("Introduce el nombre de un actor: ")
    print(f"Películas en las que ha participado {actor_busqueda}:")
    for pelicula in peliculas:
        for actor in pelicula['actores']:
            if actor['nombre'].lower() == actor_busqueda.lower():
                print(f"- {pelicula['titulo']}")

# 5. Película con calificación más alta
def pelicula_con_calificacion_mas_alta(peliculas):
    if not peliculas:  
        print("No hay películas disponibles.")
        return

    # Filtra las películas que tienen la clave 'calificacion'
    peliculas_con_calificacion = [p for p in peliculas if 'calificacion' in p]
    if not peliculas_con_calificacion:  
        print("No hay películas con calificación disponible.")
        return

    mejor_pelicula = max(peliculas_con_calificacion, key=lambda p: p['calificacion'])
    print(f"La película con la calificación más alta es '{mejor_pelicula['titulo']}' "
          f"con una calificación de {mejor_pelicula['calificacion']} y fue dirigida por "
          f"{mejor_pelicula['director']['nombre']}.")

def salir_del_programa():
    print("Programa terminado")
    exit()


def mostrar_menu():
    print("\n--- Menú de Opciones ---")
    print("1. Listar títulos y años de lanzamiento")
    print("2. Contar películas por género")
    print("3. Buscar películas por año")
    print("4. Buscar películas por actor")
    print("5. Mostrar película con la calificación más alta")
    print("6. Salir")
