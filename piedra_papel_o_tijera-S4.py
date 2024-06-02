import random   #Importacion del modulo random

def jugar_piedra_papel_tijera():    #Se define la funcion jugar_piedra_papel_tijera
    opciones = ("piedra", "papel", "tijera")    #Se declara la variable opciones con multiples valores (tupla)

    num_partidas = int(input("¿Cuántas partidas deseas jugar? "))   #La variable num_partidas almacena el numero de partidas ingresadas por el usuario
    victorias_usuario = 0
    victorias_computadora = 0   #Se inicializan las variables (contadores)
    empates = 0

    for partida in range(num_partidas): #Bucle for cuya variable 'partida' se va incrementado hasta llegar a num_partidas-1
        print(f"\nPartida {partida + 1}")   #f-string de Python permite formatear una cadena de caracteres incluyendo expresiones dinamicas
                                            # que se evaluan en tiempo de ejecucion.
        eleccion_computadora = random.choice(opciones)
        print('La computadora ya eligió')
        
        eleccion_usuario = input("Elige piedra, papel o tijera: ").lower()
        
        while eleccion_usuario not in opciones:
            print("Opción inválida. Por favor, elige piedra, papel o tijera.")
            eleccion_usuario = input("Elige piedra, papel o tijera: ").lower()
        
        print('La computadora eligió:', eleccion_computadora, 'y tú elegiste:', eleccion_usuario) 
        
        if eleccion_usuario == eleccion_computadora:
            empates +=1
            print("¡Es un empate con la computadora!")
        elif (eleccion_usuario == "piedra" and eleccion_computadora == "tijera") or \
             (eleccion_usuario == "papel" and eleccion_computadora == "piedra") or \
             (eleccion_usuario == "tijera" and eleccion_computadora == "papel"):
            print("¡Ganaste!")
            victorias_usuario += 1
        else:
            print("¡La computadora gana!")
            victorias_computadora += 1

    print("\nResultados finales:")
    print("Empates:", empates)
    print("Victorias del usuario:", victorias_usuario)
    print("Victorias de la computadora:", victorias_computadora)
    
    if victorias_usuario > victorias_computadora:
        print("¡Eres el ganador del juego!")
    elif victorias_computadora > victorias_usuario:
        print("¡La computadora es la ganadora del juego!")
    else:
        print("¡El juego ha terminado en empate!")

jugar_piedra_papel_tijera()
