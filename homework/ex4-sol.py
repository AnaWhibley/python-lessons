# Ejercicio 1: ¿Es Mario más alto que Bowser?
# Instrucciones: Asigna los valores 180 y 200 a las variables 'mario' y 'bowser', respectivamente.
# Almacena en una variable 'esMarioMasAlto' la comparación de si 'mario' es mayor que 'bowser'
# y almacena en otra variable 'sonIguales' si 'mario' es igual a 'bowser'.
# Imprime los resultados en las strings proporcionadas.
mario = 180
bowser = 200
esMarioMasAlto = mario > bowser
sonIguales = mario == bowser
print(f"¿Mario es más alto que Bowser? {esMarioMasAlto}")
print(f"¿Mario y Bowser tienen la misma altura? {sonIguales}")

# Ejercicio 2: Comparación de Nombres de Personajes
# Instrucciones: Asigna las cadenas "link" y "zelda" a las variables 'personaje1' y 'personaje2', respectivamente.
# Almacena en una variable 'mismosNombres' si 'personaje1' es igual a 'personaje2'.
# Almacena en otra variable 'esPersonaje1Mayor' si 'personaje1' es mayor que 'personaje2' en el orden alfabético.
# Imprime los resultados en las strings proporcionadas.
personaje1 = "link"
personaje2 = "zelda"
mismosNombres = personaje1 == personaje2
esPersonaje1Mayor = personaje1 > personaje2
print(f"¿Link y Zelda tienen el mismo nombre? {mismosNombres}")
print(f"¿El nombre 'Link' es mayor que 'Zelda'? {esPersonaje1Mayor}")

# Ejercicio 3: Poderes en Fortnite
# Instrucciones: Asigna los valores 5 y 8 a las variables 'arma' y 'enemigos', respectivamente.
# Almacena en una variable 'condicion1' si 'arma' es menor que 'enemigos' y 'arma' es mayor que 0.
# Almacena en otra variable 'condicion2' si 'arma' es mayor que 'enemigos' o 'enemigos' es igual a 8.
# Imprime los resultados en las strings proporcionadas.
arma = 5
enemigos = 8
condicion1 = arma < enemigos and arma > 0
condicion2 = arma > enemigos or enemigos == 8
print(f"¿El arma tiene menos balas que los enemigos y es mayor que 0? {condicion1}")
print(f"¿El arma tiene más balas que los enemigos o hay exactamente 8 enemigos? {condicion2}")

# Ejercicio 4: Uso de 'not' en la Batalla
# Instrucciones: Asigna el valor True a la variable 'jefeDerrotado'.
# Almacena en una variable 'noDerrotado' el valor de 'not jefeDerrotado'.
# Almacena en otra variable 'confusion' el valor de 'jefeDerrotado and not jefeDerrotado'.
# Imprime los resultados en las strings proporcionadas.
jefeDerrotado = True
noDerrotado = not jefeDerrotado
confusion = jefeDerrotado and not jefeDerrotado
print(f"¿El jefe no está derrotado? {noDerrotado}")
print(f"¿El jefe está derrotado y no derrotado al mismo tiempo? {confusion}")

# Ejercicio 5: La Prueba del Juego
# Instrucciones: Asigna los valores 10, 20 y 30 a las variables 'puntos', 'nivel' y 'nivelMax', respectivamente.
# Almacena en una variable 'condicion' si 'puntos' es menor que 'nivel' y 'nivelMax' es mayor que 'nivel'.
# Imprime el resultado en la string proporcionada.
puntos = 10
nivel = 20
nivelMax = 30
condicion = puntos < nivel and nivelMax > nivel
print(f"¿10 puntos es menor que el nivel 20 y el nivel máximo es mayor que el nivel 20? {condicion}")

# Ejercicio 6: Comparación de Equipos
# Instrucciones: Asigna las cadenas "armor" y "ARMOR" a las variables 'equipo1' y 'equipo2', respectivamente.
# Almacena en una variable 'mismosEquipos' si 'equipo1' es igual a 'equipo2'.
# Almacena en otra variable 'longitudMayor' si la longitud de 'equipo1' es mayor que la longitud de 'equipo2'.
# Imprime los resultados en las strings proporcionadas.
equipo1 = "armor"
equipo2 = "ARMOR"
mismosEquipos = equipo1 == equipo2
longitudMayor = len(equipo1) > len(equipo2)
print(f"¿'armor' es igual a 'ARMOR'? {mismosEquipos}")
print(f"¿La longitud de 'armor' es mayor que la de 'ARMOR'? {longitudMayor}")

# Ejercicio 7: Condiciones de Jugador en un RPG
# Instrucciones: Asigna los valores 0 y 5 a las variables 'mana' y 'nivelMagia', respectivamente.
# Almacena en una variable 'manaSuficiente' si 'not (mana + nivelMagia > 5)'.
# Almacena en otra variable 'manaDoble' si 'mana * 2 == 0'.
# Imprime los resultados en las strings proporcionadas.
mana = 0
nivelMagia = 5
manaSuficiente = not (mana + nivelMagia > 5)
manaDoble = mana * 2 == 0
print(f"¿La suma de mana y nivel de magia no supera 5? {manaSuficiente}")
print(f"¿El doble de mana es 0? {manaDoble}")

# Ejercicio 8: Evaluación de Estrategias
# Instrucciones: Asigna los valores 3, 6 y 9 a las variables 'estrategia1', 'estrategia2' y 'estrategia3', respectivamente.
# Almacena en una variable 'estrategiaCompuesta' si 'estrategia1' es menor que 'estrategia2' o 'estrategia2' es mayor que 'estrategia3' y 'estrategia3' es igual a 9.
# Imprime el resultado en la string proporcionada.
estrategia1 = 3
estrategia2 = 6
estrategia3 = 9
estrategiaCompuesta = estrategia1 < estrategia2 or (estrategia2 > estrategia3 and estrategia3 == 9)
print(f"¿3 es menor que 6 o 6 es mayor que 9 y 9 es igual a 9? {estrategiaCompuesta}")

# Ejercicio 9: Booleanos en el Juego
# Instrucciones: Asigna los valores True y False a las variables 'nivelCompleto' y 'enemigosDerrotados'.
# Almacena en una variable 'todoListo' el valor de 'nivelCompleto and enemigosDerrotados'.
# Almacena en otra variable 'alMenosUno' el valor de 'nivelCompleto or enemigosDerrotados'.
# Imprime los resultados en las strings proporcionadas.
nivelCompleto = True
enemigosDerrotados = False
todoListo = nivelCompleto and enemigosDerrotados
alMenosUno = nivelCompleto or enemigosDerrotados
print(f"¿Nivel completo y enemigos derrotados? {todoListo}")
print(f"¿Nivel completo o enemigos derrotados? {alMenosUno}")

# Ejercicio 10: Comparación de Puntos en un Juego
# Instrucciones: Asigna los valores 7 y 14 a las variables 'puntos1' y 'puntos2', respectivamente.
# Almacena en una variable 'puntosCondicion' si 'puntos1' es menor que 'puntos2' y el cuadrado de 'puntos2' es mayor que 100.
# Imprime el resultado en la string proporcionada.
puntos1 = 7
puntos2 = 14
puntosCondicion = puntos1 < puntos2 and puntos2 ** 2 > 100
print(f"¿7 puntos es menor que 14 y el cuadrado de 14 es mayor que 100? {puntosCondicion}")
