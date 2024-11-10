import random
from funciones import *
from mensajes import *


def jugar():
    '''

    Funcion que no recibe ningun argumento.
    Comienza el juego con la llamada de Opcion 1 desde el menú.

    Inicializan todas las variables a utilizar.

    '''

    #Ingreso nombre de jugador.
    jugador = input("Ingrese el nombre del jugador: ")
    #Se valida que no se ingrese un string vacio o con espacios.
    while jugador.strip() == "":
        #Caso omiso, se pide el reingreso del nombre.
        mecanografiar("Debe ingresar un nombre.")
        jugador = input("\nIngrese nuevamente el nombre del jugador:")

    #Opciones posibles a seleccionar durante el juego.
    opciones = ["Piedra","Papel","Tijera"]

    #Ronda inicial.
    partida= 1

    #Rondas maximas a jugar.
    total_partidas = 10

    #Victorias, derrotas y empates del jugador.
    victoria_jugador = 0
    victoria_vader = 0
    empate = 0
    
    #Puntaje y racha para el multiplicador/modo berserk
    puntaje = 0
    racha = None
    contador_racha = 0
    multiplicador = 1
    berserk = None
    berserk_gana = None

    #Bucle para validar que no se hayan jugado las 10 rondas aun.
    while partida <= total_partidas:

        #Aviso de numero de rondas
        print(f"\nPartida {partida} de {total_partidas}")

        #Eleccion y validación de nuestro movimiento.
        eleccion_jugador = input("\nElegir en entre: Piedra | Papel | Tijera\nIngresar: \n").capitalize()
        while eleccion_jugador != "Piedra" and eleccion_jugador != "Papel" and eleccion_jugador != "Tijera":
            print("Eligió una opcion invalida, vuelva a intentar.")
            eleccion_jugador = input("\nElegir en entre: Piedra | Papel | Tijera\nIngresar: \n").capitalize()
        
        #Seleccion random de vader.
        eleccion_vader= random.choice(opciones)
        mecanografiar(f"\nDarth Vader ataca con {eleccion_vader}.\n")
        
        '''
        Diccionario, validacion del ganador, racha de victorias.

        | Piedra > Tijera |
        | Tijera > Papel  | 
        | Papel > Piedra  |
        
        GANADOR:
        Utilizamos la clave para almacenar el valor a cual le gana,
        de esta manera podemos comparar el VALOR de la clave seleccionada
        con la CLAVE ya sea la del jugador con la de Vader o la de Vader con la del jugador.
        Caso de que ambas partes seleccionen lo mismo, se da un empate.

        RACHA:
        Cuando ganemos 2 rondas consecutivas entraremos en racha, esto hará
        que desbloqueemos un multiplicador de puntos que aumentará entre mayor sea la racha.
        En caso de perder 2 consecutivas se nos restaran 10 puntos.

        BERSERK:
        Hay una probabilidad de activarse a partir de la 3er ronda consecutiva que ganemos.
        Podremos perder todo el juego al perder una ronda en este modo.

        2 victorias seguidas → Multiplicador x 1.25.
        3 victorias seguidas → Multiplicador x 1.5.     Posibilidad de Berserk 33.3%
        4 victorias seguidas → Multiplicador x 1.75.    Posibilidad de Berserk 50%
        5 victorias seguidas → Multiplicador x 2.       Posibilidad de Berserk 100%

        '''

        #Diccionario para validar ganador.
        gana = {'Piedra': 'Tijera', 'Tijera': 'Papel', 'Papel': 'Piedra'}
        #Comparacion del VALOR (Jugador) y la CLAVE (Vader). 
        if gana[eleccion_jugador] == eleccion_vader:
            mecanografiar(f"\n{verde}El jedi {jugador} ganó la ronda {partida}.{blanco}")
            #Contador victorias del jugador.
            victoria_jugador += 1

            #Comprobacion del ganador de la ronda previa.
            if racha == "Jugador":

                #Aumenta la racha en caso de haber ganado previamente.
                contador_racha += 1

                #Multiplicadores de puntos
                if contador_racha == 2:
                    multiplicador = 1.25
                elif contador_racha == 3:
                    multiplicador = 1.5
                    #POSIBILIDAD de berserk a partir de la 3er victoria CONSECUTIVA en adelante.
                    habilitar_berserk(contador_racha, berserk)
                elif contador_racha == 4:
                    multiplicador = 1.75
                    habilitar_berserk(contador_racha, berserk)
                elif contador_racha == 5:
                    multiplicador = 2
                    habilitar_berserk(contador_racha, berserk)
            else:
                #Se reinicia la racha en caso de no haber sido el ganador previo.
                contador_racha = 1
                multiplicador = 1
            #Actualizamos el ganador de la ronda
            racha = "Jugador"
            #Suma de puntaje con el multiplicador correspondiente ( 1 | 1.25 | 1.5 | 1.75 | 2 )
            puntaje += 10 * multiplicador
            mecanografiar(f"\nPuntaje actual: {puntaje}\n")

        #El jugador no ganó? Comparamos si ganó Vader.
        elif gana[eleccion_vader] == eleccion_jugador:
            #Revisamos si esta habilitado el modo berserk.
            if berserk == True:
                #Berserk habilitado, se le suma una derrota al jugador y Vader gana el juego.
                berserk_gana = True
                victoria_vader += 1
                break
            
            #Berserk deshabilitado, Vader gana la ronda y el juego sigue.
            mecanografiar(f"{rojo}Darth Vader ganó la ronda {partida}.{blanco}")
            #Contador derrotas del jugador.
            victoria_vader += 1

            if puntaje > 0:
                #Racha vader
                if racha == "Vader":
                    contador_racha -= 1
                    #Restamos puntaje si tenemos 2 o mas derrotas consecutivas.
                    if contador_racha <= -2:
                        puntaje -= 10
                else: #Caso contrario establecemos la racha negativa.
                    contador_racha = -1
                racha = "Vader"
            mecanografiar(f"\nPuntaje actual: {puntaje}\n")
        else:
            #Empate.
            mecanografiar(f"\n{amarillo}Empate!{blanco}\n")
            empate += 1

        #Comprobamos empate, caso 'Si', se extiende el juego 1 ronda.
        while total_partidas == partida and victoria_jugador == victoria_vader:
            total_partidas += 1
            mecanografiar("\nHa ocurrido un empate entre los jedi y el lado oscuro... RONDA DEFINITORIA!!!")

        #Contador de rondas.
        partida += 1
    
    #Berserk ganó.
    if berserk_gana == True:
        mecanografiar(f"\n{rojo}Vader modo berserk ha vencido... No hubo escapatoria...{blanco}")
        print(vader_gana)
        playsound('audios/vader_gana.mp3')
    #Jugador ganó.
    elif victoria_jugador > victoria_vader:
        mecanografiar(f"\n{verde}Felicidades has derrotado a Darth Vader!!!{blanco}")
        print(vader_pierde)
        playsound('audios/vader_pierde.mp3')
    #Jugador perdió.
    elif victoria_jugador < victoria_vader:
        mecanografiar(f"\n{rojo}Darth Vader te ha derrotado!!!{blanco}")
        print(vader_gana)
        playsound('audios/vader_gana.mp3')
    #Estadisticas de la partida.
    mecanografiar(f'''
Tu puntación ha sido de: {puntaje} puntos.
{amarillo}Victorias:{blanco} {victoria_jugador}
{amarillo}Derrotas:{blanco} {victoria_vader}
{amarillo}Empates:{blanco} {empate}
Has sido agregado al ranking de jugadores, {jugador}.
''')

    #Agregado al ranking.
    agregar_jugador_ranking(jugador, puntaje, victoria_jugador)