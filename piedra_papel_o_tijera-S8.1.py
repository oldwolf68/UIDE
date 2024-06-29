import random
from getpass import getpass  # Importación del módulo getpass

def jugar_piedra_papel_tijera():
    opciones = {1: "piedra", 2: "papel", 3: "tijera"}  # Diccionario para mapear números a opciones

    # Validación del número de partidas
    while True:
        try:  # Intenta ejecutar el bloque de código que podría generar una excepción
            num_partidas = int(input("¿Cuántas partidas deseas jugar? "))
            if num_partidas > 0:
                break  # Interrumpe el bucle cuando se cumple la condición
            else:
                print("Por favor, ingresa un número entero positivo.")
        except ValueError:  # Si el usuario ingresa un caracter o cadena de caracteres, el bucle se repite porque falla la conversión a entero
            print("Entrada inválida. Por favor, ingresa un número entero.")
   
    modo_juego = input("¿Deseas jugar contra la computadora o contra otro usuario? (Escribe 'computadora' o 'usuario'): ").lower()

    victorias_usuario1 = 0  # Se inicializa la variable victorias_usuario1 (contador)
    victorias_usuario2 = 0  # Se inicializa la variable victorias_usuario2 (contador)
    empates = 0  # Se inicializa la variable empates (contador)

    for partida in range(num_partidas):  # Bucle for cuya variable 'partida' se va incrementando hasta llegar al valor de num_partidas-1
        print(f"\nPartida {partida + 1}")  # f-string de Python permite formatear una cadena de caracteres incluyendo expresiones dinámicas que se evalúan en tiempo de ejecución.
        
        if modo_juego == 'computadora':  # Verifica si el modo de juego es contra la computadora
            eleccion_computadora = random.choice(list(opciones.values()))  # La computadora elige de manera aleatoria entre los valores de la variable opciones
            print('La computadora ya eligió')  # Informa al usuario que la computadora ya ha hecho su elección
            
            eleccion_usuario = int(input("Elige 1 para piedra, 2 para papel, o 3 para tijera: "))
            while eleccion_usuario not in opciones:
                print("Opción inválida. Por favor, elige 1 para piedra, 2 para papel, o 3 para tijera.")
                eleccion_usuario = int(input("Elige 1 para piedra, 2 para papel, o 3 para tijera: "))
            
            eleccion_usuario = opciones[eleccion_usuario]
            print('La computadora eligió:', eleccion_computadora, 'y tú elegiste:', eleccion_usuario) 
            
            if eleccion_usuario == eleccion_computadora:  # Determina si hay empate
                empates += 1  # Incrementa en 1 el valor de la variable 'empates'
                print("¡Es un empate con la computadora!")
            elif (eleccion_usuario == "piedra" and eleccion_computadora == "tijera") or \
                 (eleccion_usuario == "papel" and eleccion_computadora == "piedra") or \
                 (eleccion_usuario == "tijera" and eleccion_computadora == "papel"):  # Verifica si el usuario ha ganado
                print("¡Ganaste!")
                victorias_usuario1 += 1  # Incrementa en 1 el valor de la variable 'victorias_usuario1'
            else:  # La computadora gana
                print("¡La computadora gana!")
                victorias_usuario2 += 1  # Incrementa en 1 el valor de la variable 'victorias_usuario2'
        elif modo_juego == 'usuario':  # Verifica si el modo de juego es contra otro usuario
            eleccion_usuario1 = int(getpass("Usuario 1, elige 1 para piedra, 2 para papel, o 3 para tijera (no se mostrará): "))
            while eleccion_usuario1 not in opciones:
                print("Opción inválida. Por favor, elige 1 para piedra, 2 para papel, o 3 para tijera.")
                eleccion_usuario1 = int(getpass("Usuario 1, elige 1 para piedra, 2 para papel, o 3 para tijera (no se mostrará): "))
            
            eleccion_usuario2 = int(input("Usuario 2, elige 1 para piedra, 2 para papel, o 3 para tijera: "))
            while eleccion_usuario2 not in opciones:
                print("Opción inválida. Por favor, elige 1 para piedra, 2 para papel, o 3 para tijera.")
                eleccion_usuario2 = int(input("Usuario 2, elige 1 para piedra, 2 para papel, o 3 para tijera: "))

            eleccion_usuario1 = opciones[eleccion_usuario1]
            eleccion_usuario2 = opciones[eleccion_usuario2]
            print('Usuario 1 eligió:', eleccion_usuario1, 'y Usuario 2 eligió:', eleccion_usuario2) 
            
            if eleccion_usuario1 == eleccion_usuario2:  # Determina si hay empate
                empates += 1  # Incrementa en 1 el valor de la variable 'empates'
                print("¡Es un empate!")
            elif (eleccion_usuario1 == "piedra" and eleccion_usuario2 == "tijera") or \
                 (eleccion_usuario1 == "papel" and eleccion_usuario2 == "piedra") or \
                 (eleccion_usuario1 == "tijera" and eleccion_usuario2 == "papel"):  # Verifica si el Usuario 1 ha ganado
                print("¡Usuario 1 gana!")
                victorias_usuario1 += 1  # Incrementa en 1 el valor de la variable 'victorias_usuario1'
            else:  # El Usuario 2 gana
                print("¡Usuario 2 gana!")
                victorias_usuario2 += 1  # Incrementa en 1 el valor de la variable 'victorias_usuario2'
        else:  # Modo de juego inválido
            print("Modo de juego inválido. Saliendo del juego.")
            return  # Termina la función y sale del juego

    print("\nResultados finales:")
    print("Empates:", empates)
    
    if modo_juego == 'computadora':  # Imprime los resultados finales si el juego fue contra la computadora
        print("Victorias del usuario:", victorias_usuario1)
        print("Victorias de la computadora:", victorias_usuario2)
        
        if victorias_usuario1 > victorias_usuario2:  # Determina el ganador del juego
            print("¡Eres el ganador del juego!")    
        elif victorias_usuario2 > victorias_usuario1:
            print("¡La computadora es la ganadora del juego!")
        else:
            print("¡El juego ha terminado en empate!")
    else:  # Imprime los resultados finales si el juego fue contra otro usuario
        print("Victorias del Usuario 1:", victorias_usuario1)
        print("Victorias del Usuario 2:", victorias_usuario2)
        
        if victorias_usuario1 > victorias_usuario2:  # Determina el ganador del juego
            print("¡Usuario 1 es el ganador del juego!")    
        elif victorias_usuario2 > victorias_usuario1:
            print("¡Usuario 2 es el ganador del juego!")
        else:
            print("¡El juego ha terminado en empate!")

jugar_piedra_papel_tijera()  # Llama a la función para iniciar el juego