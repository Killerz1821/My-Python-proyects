import random

victorias_usuario = 0
victorias_bot = 0

opciones = ["piedra", "papel", "tijeras"]

while True:
    User_input = input("Escribe Piedra/Papel/Tijeras o Q para salir ").lower()
    if User_input == "q":
        break

    if User_input not in opciones:
        continue

    random_number = random.randint(0, 2 )
    # piedra = 0, papel = 1, tijeras = 2
    eleccion_bot = opciones[random_number]
    print("el bot eligio", eleccion_bot + ".")

    if User_input == "piedra" and eleccion_bot == "tijeras":
        print("Ganaste!")
        victorias_usuario += 1 

    elif User_input == "papel" and eleccion_bot == "piedra":
        print("Ganaste!")
        victorias_usuario += 1 

    elif User_input == "tijeras" and eleccion_bot == "papel":
        print("Ganaste!")
        victorias_usuario += 1 

    elif User_input == "piedra" and eleccion_bot == "papel":
        print("Perdiste!")
        victorias_bot += 1 

    elif User_input == "papel" and eleccion_bot == "tijeras":
        print("Perdiste!")
        victorias_bot += 1 

    elif User_input == "tijeras" and eleccion_bot == "piedra":
        print("Perdiste!")
        victorias_bot += 1 

    elif User_input == eleccion_bot:
        print("empate")

print("ganaste", victorias_usuario, "veces")
print("el bot gano", victorias_bot, "veces")
print("Adios!")