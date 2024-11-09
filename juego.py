import random
from funciones import mecanografiar

def jugar():

    jugador = input("Ingrese el nombre del jugador: ")
    opciones = ["Piedra","Papel","Tijera"]
    partida= 1
    total_partidas = 10
    victoria_jugador = 0
    victoria_vader = 0
    empate = 0

    while partida <= total_partidas:
        print(f"Partida {partida} de")
        eleccion_jugador = input("- Elegir en entre Piedra | Papel | Tijera: ")
        pc= random.choice(opciones)
        print(pc)

        match eleccion_jugador:
            case "Piedra":
                match pc:
                    case "Piedra":
                        print("Empatan")
                        empate += 1
                    case "Papel":
                        print("PC gana.")
                        victoria_vader += 1
                    case "Tijera":

                        print(mecanografiar(f"{jugador} gana."))
                        victoria_jugador += 1
            case "Papel":
                match pc:
                    case "Piedra":
                        print(f"{jugador} gana.")
                        victoria_jugador += 1
                    case "Papel":
                        print("Empatan")
                        empate += 1
                    case "Tijera":
                        print("PC gana.")
                        victoria_vader += 1
            case "Tijera":
                match pc:
                    case "Piedra":
                        print("PC gana.")
                        victoria_vader += 1
                    case "Papel":
                        print(f"{jugador} gana.")
                        victoria_jugador += 1
                    case "Tijera":
                        print("Empatan.")
                        empate += 1
        partida += 1
    
    vader = '''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣴⣶⣯⠪⣕⢶⣦⣔⢄⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣼⣿⣿⣿⣿⣧⡙⣧⢹⣿⣷⣇⠀⠀⠀⠀
⠀⠀⠀⣸⣿⣿⣿⣿⡟⠛⢿⣾⢿⡟⠟⢛⡄⠀⠀⠀
⠀⠀⠀⣿⣿⣿⣿⢟⣯⢖⣒⣚⣭⠀⣣⣈⡨⣢⠀⠀   ¡Maldicion!
⠀⠀⠀⣿⣿⣿⢏⡛⠱⢿⣧⣿⢿⡂⠻⠭⠿⣴⠀⠀    Has ganado esta vez.
⠀⠀⣰⣿⣿⡟⢼⣿⡶⡄⣴⣶⣶⠇⠀⢶⣶⡎⡗⠀    Volvere!!!
⠀⢠⣿⣿⣿⢇⣷⣭⣃⠈⠙⠁⣠⢟⡟⡷⡙⢸⣷⠃
⢀⣿⣿⠿⢟⣸⣷⠶⠯⠍⠀⡫⢬⣬⣤⣥⡅⣊⣿⣼
⡜⣫⣴⣿⣿⣿⠁⢰⣿⣿⣿⣿⣞⠿⢛⣵⣾⡿⠛⠁
⠙⠿⠿⠿⣿⣿⣼⣬⣿⣿⣿⣿⣿⣷⠟⠉⠁⠀⠀⠀'''

    rojo = "\033[3;31m"

    if victoria_jugador > victoria_vader:
        print("Felicidades has derrotado en Darth Vader!!!")
        print(rojo +vader)
    elif victoria_jugador < victoria_vader:
        print("Darth Vader te ha derrotado!!!")