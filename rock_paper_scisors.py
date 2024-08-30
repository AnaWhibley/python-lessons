import random

def jugar_una_ronda():
    opciones = ["piedra", "papel", "tijeras"]
    eleccion_computadora = random.choice(opciones)

    print("¡Vamos a jugar Piedra, Papel, Tijeras!")
    eleccion_jugador = input("Ingresa tu elección (piedra, papel o tijeras): ").lower()

    if eleccion_jugador not in opciones:
        print("¡Elección inválida! Por favor elige piedra, papel o tijeras.")
        return None

    print(f"La computadora eligió: {eleccion_computadora}")

    # Aquí debes escribir la lógica para determinar el ganador:
    # 1. Si la elección del jugador es igual a la de la computadora, imprimir "¡Es un empate!"
    # 2. Si la elección del jugador gana contra la de la computadora, imprimir "¡Tú ganas!"
    # 3. En caso contrario, imprimir "¡Tú pierdes!"

def piedra_papel_tijeras():
    while True:
        jugar_una_ronda()
        jugar_otra_vez = input("¿Quieres jugar otra vez? (sí/no): ").lower()
        if jugar_otra_vez != "sí":
            print("¡Gracias por jugar!")
            break

if __name__ == "__main__":
    piedra_papel_tijeras()
