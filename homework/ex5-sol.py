# Asigna el valor 40 a la variable 'salud'.
# Evalúa si 'salud' es mayor o igual a 80, entre 50 y 79, entre 20 y 49, o menor a 20.
# Según el valor, asigna un estado a la variable 'estado_jugador'.
# Imprime el valor de 'estado_jugador' al final.

salud = 40

if salud >= 80:
    estado_jugador = "Salud al máximo"
elif 50 <= salud < 80:
    estado_jugador = "Salud buena"
elif 20 <= salud < 50:
    estado_jugador = "Salud baja"
else:
    estado_jugador = "Salud crítica"

print(f"Estado del jugador: {estado_jugador}")

# Asigna el valor "espada" a la variable 'arma'.
# Evalúa si 'arma' es "espada", "arco" o "hacha".
# Según el valor, asigna una potencia a la variable 'potencia'.
# Imprime el valor de 'potencia' al final.

arma = "espada"

if arma == "espada":
    potencia = "alta"
elif arma == "arco":
    potencia = "media"
elif arma == "hacha":
    potencia = "muy alta"
else:
    potencia = "desconocida"

print(f"El arma seleccionada es {arma} con potencia {potencia}.")

# Asigna el valor "difícil" a la variable 'modo'.
# Evalúa si 'modo' es "fácil", "normal" o "difícil".
# Según el valor, asigna una cantidad de enemigos a la variable 'enemigos'.
# Imprime el valor de 'enemigos' al final.

modo = "difícil"

if modo == "fácil":
    enemigos = 10
elif modo == "normal":
    enemigos = 20
elif modo == "difícil":
    enemigos = 30
else:
    enemigos = 0

print(f"Modo de juego seleccionado: {modo}. Número de enemigos: {enemigos}.")

# Asigna el valor "dragón" a la variable 'monstruo'.
# Evalúa si 'monstruo' es "dragón", "ogro" o "troll".
# Según el valor, asigna una dificultad a la variable 'dificultad'.
# Imprime el valor de 'dificultad' al final.

monstruo = "dragón"

if monstruo == "dragón":
    dificultad = "Extrema"
elif monstruo == "ogro":
    dificultad = "Alta"
elif monstruo == "troll":
    dificultad = "Media"
else:
    dificultad = "Desconocida"

print(f"Te enfrentarás a un {monstruo} con dificultad {dificultad}.")

# Asigna el valor "hechicero" a la variable 'amigo'.
# Evalúa si 'amigo' es "hechicero", "caballero", "elfo" o "enano".
# Según el valor, asigna un bono a la variable 'bono'.
# Imprime el valor de 'bono' al final.

amigo = "hechicero"

if amigo == "hechicero":
    bono = "Bono de magia"
elif amigo == "caballero":
    bono = "Bono de defensa"
elif amigo == "elfo":
    bono = "Bono de agilidad"
else:
    bono = "Sin bono"

print(f"Tu compañero es un {amigo} y obtienes {bono}.")
