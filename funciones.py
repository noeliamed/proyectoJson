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




def mostrar_menu():
    print("\n--- Menú de Opciones ---")
    print("1. Listar títulos y años de lanzamiento")
    print("2. Contar películas por género")
    print("3. Buscar películas por año")
    print("4. Buscar películas por actor")
    print("5. Mostrar película con la calificación más alta")
    print("6. Salir")
