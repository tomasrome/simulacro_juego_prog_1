import json
import time

heroe = {
    "nombre": "Maria",
    "victorias": 0,
    "puntuacion": 321
}

def agregar_jugador_ranking(nombre, puntuacion):

    with open("ranking_puntuaciones.json", mode="r+") as file:
        lista_puntuaciones = json.load(file)

        print(lista_puntuaciones)
        numero_nuevo_jugador = len(lista_puntuaciones)+1
        jugador_nuevo_key = f"jugador_{numero_nuevo_jugador}"
        print(jugador_nuevo_key)
        
        lista_puntuaciones[jugador_nuevo_key] = {
            "nombre": f"{nombre}",
            "puntuacion": puntuacion
        }
        file.seek(0)
        json.dump(lista_puntuaciones, file, indent=4)


def mostrar_ranking_puntuaciones():

    with open("ranking_puntuaciones.json", mode="r") as file:
        lista_puntuaciones = json.load(file)
    
    lista_desordenada = []
    for jugador, info in lista_puntuaciones.items():
        lista_desordenada += [[info["nombre"], info["victorias"]]]
    
    lista_ordenada = lista_desordenada

    for i in range(len(lista_ordenada)):
        for j in range(0, len(lista_ordenada) - i - 1 ):
            if lista_ordenada[j][1] < lista_ordenada[j+1][1]:
                lista_ordenada[j], lista_ordenada[j + 1] = lista_ordenada [j + 1], lista_ordenada[j]
    
    print("\nRANKING DE VICTORIAS\n--------------------")
    posicion = 1
    for jugadores in lista_ordenada:
        print(f"{posicion} - {jugadores[0]} --> {jugadores[1]} victorias.")
        posicion += 1



def mecanografiar(texto):

    for palabra in texto:
        time.sleep(0.1)
        print(palabra, end="", flush=True)



#mostrar_ranking_puntuaciones()