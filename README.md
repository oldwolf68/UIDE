Proyecto: Piedra, Papel o Tijera

Descripción:

Este programa desarrollado en Python recrea el clásico juego de Piedra, Papel o Tijera. 
Permite jugar al juego "Piedra, Papel o Tijera" contra la computadora o contra otro usuario.
Utiliza entradas numéricas para las opciones de juego (1 para piedra, 2 para papel, 3 para tijera).
Valida la entrada del usuario para asegurando que se ingresen números enteros positivos para el número de partidas que se elige jugar.
Oculta la elección del Usuario 1 cuando se juega contra otro usuario.
Lleva un conteo de victorias y empates, y muestra los resultados finales al terminar todas las partidas.

Principales Funcionalidades:
Importaciones:
import random: Importa el módulo random, que se utiliza para generar elecciones aleatorias para la computadora.
from getpass import getpass: Importa la función getpass, que se utiliza para ocultar la entrada del Usuario 1 cuando se juega contra otro usuario.

Función principal: jugar_piedra_papel_tijera
Esta función es la que contiene toda la lógica del juego.

Mapeo de opciones:
opciones = {1: "piedra", 2: "papel", 3: "tijera"}
Se utiliza un diccionario para mapear las opciones de números (1, 2, 3) a las jugadas correspondientes ("piedra", "papel", "tijera").

Validación del número de partidas:
while True:
    try:
        num_partidas = int(input("¿Cuántas partidas deseas jugar? "))
        if num_partidas > 0:
            break
        else:
            print("Por favor, ingresa un número entero positivo.")
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número entero.")
Este bloque de código asegura que el usuario ingrese un número entero positivo para el número de partidas. Si el usuario ingresa un valor no entero o negativo, se le pedirá que lo intente de nuevo.
        
Selección del modo de juego:
modo_juego = input("¿Deseas jugar contra la computadora o contra otro usuario? (Escribe 'computadora' o 'usuario'): ").lower()
El usuario elige si quiere jugar contra la computadora o contra otro usuario.

Bucle de partidas:
for partida in range(num_partidas):
    print(f"\nPartida {partida + 1}")
Este bucle se repite el número de veces que el usuario especificó, jugando las partidas una por una.

Lógica para el modo "computadora":
En el modo contra la computadora, esta elige una opción aleatoria. El usuario ingresa su elección como un número (1, 2, 3). Se compara la elección del usuario con la de la computadora y se determinan los resultados de la partida.

Lógica para el modo "usuario":
En el modo de juego entre usuarios, ambos jugadores ingresan su elección como un número (1, 2, 3). Las entradas del Usuario 1 se ocultan usando getpass. Se comparan las elecciones y se determinan los resultados de la partida.

Resultados finales:
Se imprime los resultados finales del juego, mostrando el número de empates, victorias del usuario y victorias de la computadora o del otro usuario. También declara el ganador del juego basado en el número de victorias.

El proyecto final está disponible en el siguiente enlace: [piedra_papel_o_tijera-S8.1]. 
Todas las líneas de código están comentadas para facilitar la comprensión de su lógica y estructura.

Saludos,
\Oldwolf68






