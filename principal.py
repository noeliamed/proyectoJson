
import json 
from funcionesPeliculas import *


def main():

    peliculas = cargar_peliculas()

    

    while True:

        mostrar_menu()

        opcion = input("Elige una opción (1-6 o 0 para salir): ")


        if opcion == "1":

            listar_titulos_y_anios(peliculas)

        elif opcion == "2":

            contar_peliculas_por_genero(peliculas)

        elif opcion == "3":

            buscar_peliculas_por_anio(peliculas)

        elif opcion == "4":

            buscar_peliculas_por_actor(peliculas)

        elif opcion == "5":

            pelicula_con_calificacion_mas_alta(peliculas)

        elif opcion == "6":
            salir_del_programa()

        else:

            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    main()
