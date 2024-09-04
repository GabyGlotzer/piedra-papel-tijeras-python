
nombre1 = input("Nombre jugador #1?: ")
nombre2 = input("Nombre jugador #2?: ")

texto1 = "Hola " + nombre1 + "! Elegí: Piedra, papel o tijeras? (o FIN)"
texto2 = "Hola " + nombre2 + "! Elegí: Piedra, papel o tijeras?"


jugador1 = ""
jugador2 = ""


while jugador1 != "fin" and jugador2 != "fin":

    while jugador1 not in("piedra","papel","tijeras","fin"):
        jugador1 = input(texto1)
        jugador1 = jugador1.lower()
    
    if jugador1 == "fin":
        break

    while jugador2 not in("piedra","papel","tijeras","fin"):
        jugador2 = input(texto2)
        jugador2 = jugador2.lower()

    if jugador2 == "fin":
        break

    condicion1 = jugador1 == "piedra" and jugador2 == "tijeras"
    condicion2 = jugador1 == "papel" and jugador2 == "piedra"
    condicion3 = jugador1 == jugador1 == "tijeras" and jugador2 == "papel"

    if jugador1 == jugador2:
        print("Empate!!!")
    elif condicion1 or condicion2 or condicion3:
        print("Ganó ", nombre1)
    else:
        print("Ganó ", nombre2) 

    jugador1 = ""
    jugador2 = ""

