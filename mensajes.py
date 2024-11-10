rojo = "\033[3;31m"
verde = "\033[3;32m"
azul = "\033[3;34m"
amarillo = "\033[3;33m"
blanco = "\033[0;37m"
subrayado = "\033[4;37m"


texto_bienvenida = f"""
{rojo}──────────────────────────────────────────────────{blanco}
    {verde}¡Bienvenido, guerrero!{blanco}
    
    Te enfrentas a {rojo}Darth Vader{blanco}. Solo los valientes 
    sobreviven. La batalla será dura... ¿Estás listo?
    
    {verde}¡Que la Fuerza te acompañe!{blanco}
{rojo}──────────────────────────────────────────────────{blanco}
"""



mensaje_menu = f'''{azul}
*********** MENÚ PRINCIPAL ***********                                   

{azul}1.{blanco} Jugar: Duelo de Piedra, Papel o Tijeras.
{azul}2.{blanco} Cómo jugar.
{azul}3.{blanco} Ver tu nivel de la Fuerza - Ranking de puntuaciones.
{azul}4.{blanco} Salir de la Galaxia

Elige una opción (1-4): {blanco}'''



como_jugar = f'''
{subrayado}COMO JUGAR:{blanco}

{verde}Maestro Yoda{blanco}: 

"El destino de la galaxia, en este duelo final se decidirá. Piedra, Papel o Tijeras jugarás, Padawan, y frente a {rojo}Darth Vader{blanco} te enfrentarás. Ni sables ni ejércitos, solo estrategia e intuición usarás, pues un combate de ingenio será.

{subrayado}Reglas del duelo, simples son:{blanco}

- Cada victoria, {verde}10{blanco} puntos ganarás. Pero un poder oculto en la racha encontrarás:
  - 2 victorias consecutivas obtienes, y un multiplicador de {verde}1.25{blanco} tendrás. Así, tu habilidad crecerá.
  - 3 victorias seguidas alcanzas, un multiplicador de {verde}1.5{blanco} recibirás, y… {rojo}Berserk{blanco} podrías despertar en Vader.
  - 4 victorias logras, y un multiplicador de {verde}1.75{blanco} a tu favor tendrás.
  - 5 victorias seguidas alcanzas, un multiplicador de {verde}2{blanco} serás digno de recibir. Un maestro, en la Fuerza te habrás vuelto.

Pero ten cuidado. Si Darth Vader acumula {rojo}3{blanco} derrotas seguidas, una posibilidad de 1 en 3 existe de que entre en modo {rojo}Berserk{blanco}. Si en la racha de {verde}3{blanco} victorias el {rojo}Berserk{blanco} no se activa, con cada victoria adicional, las probabilidades aumentarán. En {rojo}Berserk{blanco}, su furia oscura en un solo y devastador ataque concentrará, y el duelo de inmediato terminará.

Mas en la derrota, consecuencias también hay. Si dos veces seguidas pierdes, {rojo}10{blanco} puntos restados serán.

Así que juega con astucia y precisión, joven aprendiz. En este duelo final, el destino de ambos se decidirá. La Fuerza contigo que esté."
'''



vader_pierde = f'''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣴⣶⣯⠪⣕⢶⣦⣔⢄⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣼⣿⣿⣿⣿⣧⡙⣧⢹⣿⣷⣇⠀⠀⠀⠀
⠀⠀⠀⣸⣿⣿⣿⣿⡟⠛⢿⣾⢿⡟⠟⢛⡄⠀⠀⠀
⠀⠀⠀⣿⣿⣿⣿⢟⣯⢖⣒⣚⣭⠀⣣⣈⡨⣢⠀⠀   {rojo}¡Maldicion!{blanco}
⠀⠀⠀⣿⣿⣿⢏⡛⠱⢿⣧⣿⢿⡂⠻⠭⠿⣴⠀⠀    {rojo}Esta vez ganaste.{blanco}
⠀⠀⣰⣿⣿⡟⢼⣿⡶⡄⣴⣶⣶⠇⠀⢶⣶⡎⡗⠀    {rojo}Pero pronto te arrepentiras{blanco}
⠀⢠⣿⣿⣿⢇⣷⣭⣃⠈⠙⠁⣠⢟⡟⡷⡙⢸⣷⠃    {rojo}de haberme desafiado!{blanco}
⢀⣿⣿⠿⢟⣸⣷⠶⠯⠍⠀⡫⢬⣬⣤⣥⡅⣊⣿⣼
⡜⣫⣴⣿⣿⣿⠁⢰⣿⣿⣿⣿⣞⠿⢛⣵⣾⡿⠛⠁
⠙⠿⠿⠿⣿⣿⣼⣬⣿⣿⣿⣿⣿⣷⠟⠉⠁⠀⠀⠀'''




vader_gana = f'''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣴⣶⣯⠪⣕⢶⣦⣔⢄⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣼⣿⣿⣿⣿⣧⡙⣧⢹⣿⣷⣇⠀⠀⠀⠀
⠀⠀⠀⣸⣿⣿⣿⣿⡟⠛⢿⣾⢿⡟⠟⢛⡄⠀⠀⠀
⠀⠀⠀⣿⣿⣿⣿⢟⣯⢖⣒⣚⣭⠀⣣⣈⡨⣢⠀⠀   {rojo}¿Pensaste que podrías vencer al poder del {blanco}
⠀⠀⠀⣿⣿⣿⢏⡛⠱⢿⣧⣿⢿⡂⠻⠭⠿⣴⠀⠀   {rojo}Lado Oscuro? Tu derrota era inevitable{blanco}
⠀⠀⣰⣿⣿⡟⢼⣿⡶⡄⣴⣶⣶⠇⠀⢶⣶⡎⡗⠀    
⠀⢠⣿⣿⣿⢇⣷⣭⣃⠈⠙⠁⣠⢟⡟⡷⡙⢸⣷⠃
⢀⣿⣿⠿⢟⣸⣷⠶⠯⠍⠀⡫⢬⣬⣤⣥⡅⣊⣿⣼
⡜⣫⣴⣿⣿⣿⠁⢰⣿⣿⣿⣿⣞⠿⢛⣵⣾⡿⠛⠁
⠙⠿⠿⠿⣿⣿⣼⣬⣿⣿⣿⣿⣿⣷⠟⠉⠁⠀⠀⠀
'''



berserk_on = f'''
                      |_:_|
                     /(_Y_)\.
.                   ( \/M\/ )
 '.               _.'-/'-'\-'._ 
   ':           _/.--'[[[[]'--.\_
     ':        /_'  : |::"| :  '.\  {rojo}¡Ya basta! No permitiré una derrota más.{blanco}
       ':     //   ./ |oUU| \.'  :\ {rojo}¡Este es el poder absoluto del Lado {blanco}
         ':  _:'..' \_|___|_/ :   :| {rojo}Oscuro! Prepárate para enfrentar{blanco}
           ':.  .'  |_[___]_|  :.':\ {rojo}un final doloroso e inevitable.{blanco}
            [::\ |  :  | |  :   ; : \.
             '-'   \/'.| |.' \  .;.' |
             |\_    \  '-'   :       |
             |  \    \ .:    :   |   |
             |   \    | '.   :    \  |
             /       \   :. .;       |
            /     |   |  :__/     :  \|\.
           |  |   |    \:   | \   |   ||
          /    \  : :  |:   /  |__|   /|
         |     : : :_/_|  /'._\  '--|_\|
          /___.-/_|-'   \  \.
                         '-' '''

