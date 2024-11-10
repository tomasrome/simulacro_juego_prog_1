from funciones import *
from juego import jugar
from mensajes import como_jugar, texto_bienvenida, mensaje_menu
from playsound import playsound

imprimir_linea_por_linea(texto_bienvenida)

continuar = True


'''

Se inicializa un bucle while en continuar = True (No cerrará hasta que se actualice a False)
Podemos seleccionar entre 4 opciones del 1 al 4. Caso omiso se devolverá un mensaje de error y nos pedirá elegir una opción válida.

Opción 1: Llama a la función jugar(). Se inicia el juego.
Opción 2: Se llamará a la función como_jugar() en la cual se nos dará una explicación del juego, puntaje y probabilidades.
Opción 3: Llama a la función mostrar_ranking_puntuaciones(). Nos muestra el ranking de todos los jugadores, extraídos de un documento .json
Opción 4: Nos devuelve un mensaje de cierre de juego y actualiza la variable continuar = False para terminar con el bucle del menú.
Caso omiso: Mensaje de error en caso de ingresar una opción inválida.

'''

while continuar:
    opcion = input(mensaje_menu)

    match opcion:
        case "1":
            playsound('audios/menu.mp3')
            jugar()
            mecanografiar(f"Juego terminado.")
        case "2":
            playsound('audios/menu.mp3')
            imprimir_linea_por_linea(como_jugar)
        case "3":
            playsound('audios/menu.mp3')
            mostrar_ranking_puntuaciones()
        case "4":
            playsound('audios/menu.mp3')
            mecanografiar("Saliendo del programa...\n¡Gracias por jugar!")
            continuar = False
        case _:
            opcion = input("Opción invalida. Vuelva a ingresar: ")