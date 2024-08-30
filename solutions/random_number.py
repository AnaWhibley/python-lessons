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

        if intento < numero_a_adivinar:
            print("¡Muy bajo! Inténtalo de nuevo.")
        elif intento > numero_a_adivinar:
            print("¡Muy alto! Inténtalo de nuevo.")
        else:
            adivinado = True
            print(f"¡Felicidades! Adivinaste el número en {numero_de_intentos} intentos.")

    print("¡Gracias por jugar!")


if __name__ == "__main__":
    adivina_el_numero()
