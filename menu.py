from funciones import *
from juego import jugar

azul = "\033[3;34m"
blanco = "\033[0;37m"

mensaje = azul +'''
*********** MENÚ PRINCIPAL ***********                                   

1. Jugar: Duelo de Piedra, Papel o Tijeras
2. Ver tu nivel de la Fuerza (Estadísticas de victorias)
3. Salir de la Galaxia

Elige una opción (1-4): ''' + blanco

continuar = True

while continuar:
    opcion = input(mensaje)

    match opcion:
        case "1":
            jugar()
        case "2":
            mostrar_ranking_puntuaciones()
        case "3":
            print("Saliendo del programa...")
            continuar = False
        case _:
            opcion = input("Opción invalida. Vuelva a ingresar: ")