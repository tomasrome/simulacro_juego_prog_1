import json
import time
import random
from mensajes import *
from playsound import playsound

#Colores a utilizar.
rojo = "\033[3;31m"
verde = "\033[3;32m"
azul = "\033[3;34m"
blanco = "\033[0;37m"
subrayado = "\033[4;37m"
amarillo = "\033[3;33m"

def agregar_jugador_ranking(nombre:str, puntuacion: float, victoria_jugador: int) -> None:
    '''
    Funcion que actualiza el archivo ranking_puntuaciones.json con los datos del nuevo jugador, obtenidos por los parámetros.

    Parámetros:
    Nombre del jugador: nuevo jugador (str)
    Puntuación de la partida: Puntuacion del nuevo jugador. (float)
    Cantidad de victorias: Victorias del nuevo jugador. (int)

    Abre el archivo en modo lectura y escritura (r+)
    Carga la informacion obtenida actualizando el archivo.
    '''
    with open("ranking_puntuaciones.json", mode="r+") as file:

        #Carga de contenido actual.
        lista_puntuaciones = json.load(file)

        #Corroboramos el numero del nuevo jugador en la lista.
        numero_nuevo_jugador = len(lista_puntuaciones)+1
        jugador_nuevo_key = f"jugador_{numero_nuevo_jugador}"
        
        #Se añade la informacion del jugador en el formato especificado abajo.
        lista_puntuaciones[jugador_nuevo_key] = {
            "nombre": f"{nombre}",
            "puntuacion": puntuacion,
            "victorias": victoria_jugador
        }

        #.seek(0) vuelve al inicio del JSON y escribe el archivo actualizado.
        file.seek(0)
        json.dump(lista_puntuaciones, file, indent=4)


def mostrar_ranking_puntuaciones() -> None:

    '''
    Funcion que muestra el ranking de puntuaciones de los jugadores en orden.
    Utiliza un algoritmo de ordenamiento de bubble sorting.

    Se abre el archivo de ranking_puntuaciones.json en modo lectura (r)
    Ordena los jugadores de manera descendente y lo muestra por consola.
    '''

    with open("ranking_puntuaciones.json", mode="r") as file:

        #Carga el contendio que se encuentra en el archivo.
        lista_puntuaciones = json.load(file)

    if not lista_puntuaciones:
        return mecanografiar("Todavía no hay jugadores agregados.\n")
    
    #Creamos una lista con los jugadores y su puntuación.
    lista_desordenada = []
    for jugador, info in lista_puntuaciones.items():
        lista_desordenada += [[info["nombre"], info["puntuacion"]]]
    

    #Se ordena la lista por puntaje de manera descendente.
    lista_ordenada = lista_desordenada
    for i in range(len(lista_ordenada)):
        for j in range(0, len(lista_ordenada) - i - 1 ):
            if lista_ordenada[j][1] < lista_ordenada[j+1][1]:
                lista_ordenada[j], lista_ordenada[j + 1] = lista_ordenada [j + 1], lista_ordenada[j]
    
    #Printea en consola el ranking de jugadores linea por linea.
    print(f"\n{verde}------{blanco}RANKING DE PUNTUACIONES{blanco}{verde}------{blanco}\n")
    posicion = 1
    for jugador in lista_ordenada:
        imprimir_linea_por_linea(f"{verde}{posicion}{blanco} - {jugador[0]} --> {verde}{jugador[1]}{blanco} puntos.")
        posicion += 1

def mecanografiar(texto:str) -> None :
    '''
    Funcion que recibe un 'str' como argumento.
    Devuelve en consola el texto como si lo estuviera escribiendo una persona,
    mediante un bucle for con un delay de 0.07s

    '''
    for palabra in texto:
        time.sleep(0.07)
        #end = "" nos asegura que todos los caracteres se escriban en la misma linea.
        #flush = True Nos permite que el texto en consola se imprima en la consola a tiempo real.
        print(palabra, end="", flush=True)

def imprimir_linea_por_linea(texto: str) -> None :
    '''
    Funcion que recibe un 'str' como argumento y lo separa en sus respectivas
    lineas de texto de manera que le de el efecto de pelicula STAR WARS
    '''
    for linea in texto.splitlines():  
        #flush = True Nos permite que el texto en consola se imprima en la consola a tiempo real.
        print(linea, flush=True)  
        time.sleep(0.2)

def habilitar_berserk(contador: int, habilitar: bool) -> None :
    '''
    Recibimos un contador como argumento (Racha de victorias del jugador).
    
    Funcion que aumenta la probabilidad de entrar en modo berserk a medida que
    la racha tambien aumenta, en caso de habilitarse berserk pasa a ser True y
    nos devuelve un mensaje por consola dando aviso por consola de esto mismo.
    '''
    if contador == 3:
        #33.3% de probabilidades (1/3)
        b1 = 1
        b2 = random.randint(1, 3)
    elif habilitar == False and contador == 4:
        #50% de probabilidades (1/2)
        b1 = 1
        b2 = random.randint(1, 2)
    elif habilitar == False and contador >= 5:
        #100% de probabilidades (1/1)
        b1 = 1
        b2 = 1

    #Si b1, b2 son iguales se habilita Vader Berserk
    if b1 == b2:
        habilitar = True
        print(berserk_on)
        #Sonidos
        playsound('audios/vader_berserk.mp3')