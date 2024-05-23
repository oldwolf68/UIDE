import random

def jugar_piedra_papel_tijera():
    opciones = ("piedra", "papel", "tijera")
   
    eleccion_computadora = random.choice(opciones)
    print('La computadora ya eligió')
    
    eleccion_usuario = input("Elige piedra, papel o tijera: ").lower()
    
       
    while eleccion_usuario not in opciones:
        print("Opción inválida. Por favor, elige piedra, papel o tijera.")
        eleccion_usuario = input("Elige piedra, papel o tijera: ").lower()
    
    print('La computadora eligió:', eleccion_computadora, 'y tú elegiste:', eleccion_usuario) 
     
    if eleccion_usuario == eleccion_computadora:
        print("¡Es un empate con la computadora!")
    elif (eleccion_usuario == "piedra" and eleccion_computadora == "tijera") or \
         (eleccion_usuario == "papel" and eleccion_computadora == "piedra") or \
         (eleccion_usuario == "tijera" and eleccion_computadora == "papel"):
        print("¡Ganaste!")
    else:
        print("¡La computadora gana!")

jugar_piedra_papel_tijera()
