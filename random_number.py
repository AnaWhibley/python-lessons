import random

def adivina_el_numero():
    print("¡Bienvenido al juego de Adivina el Número!")
    print("Estoy pensando en un número entre 1 y 100.")

    numero_a_adivinar = random.randint(1, 100)
    numero_de_intentos = 0
    adivinado = False

    while not adivinado:
        intento = int(input("Ingresa tu intento: "))
        numero_de_intentos += 1

        # Aquí debes escribir la lógica para comparar el intento con el número a adivinar.
        # Si el intento es menor, imprimir "¡Muy bajo! Inténtalo de nuevo."
        # Si el intento es mayor, imprimir "¡Muy alto! Inténtalo de nuevo."
        # Si el intento es igual al número a adivinar, imprimir "¡Felicidades!
        # Adivinaste el número en X intentos." y terminar el juego.

    print("¡Gracias por jugar!")


if __name__ == "__main__":
    adivina_el_numero()
