# Asigna los valores 180 y 150 a las variables 'gru_altura' y 'minion_altura'.
# Compara si Gru es más alto que el Minion.
# Imprime el resultado usando interpolacion de strings
gru_altura = 180
minion_altura = 150
print(gru_altura > minion_altura)

# Asigna los valores 10 y 12 a las variables 'manzanas_lucas' y 'manzanas_ana'.
# Compara si Lucas tiene menos manzanas que Ana.
# Imprime el resultado.
manzanas_lucas = 10
manzanas_ana = 12
print(manzanas_lucas < manzanas_ana)

# Asigna los valores 500 y 500 a las variables 'tesoro' y 'coste_espada'.
# Compara si el dinero en el cofre del tesoro es suficiente para comprar una espada.
# Imprime el resultado.
tesoro = 500
coste_espada = 500
print(tesoro >= coste_espada)

# Asigna los valores True y False a las variables 'kevin_listo' y 'bob_cansado'.
# Evalúa si Kevin está listo y Bob no está cansado.
# Imprime el resultado.
kevin_listo = True
bob_cansado = False
print(kevin_listo and not bob_cansado)

# Asigna los valores True y False a las variables 'tienes_municion' y 'hay_enemigos'.
# Evalúa si tienes munición o si no hay enemigos cerca.
# Imprime el resultado.
tienes_municion = True
hay_enemigos = False
print(tienes_municion or not hay_enemigos)

# Asigna el valor 100 a la variable 'salud'.
# Asigna el valor False a la variable 'escudo'.
# Evalúa la siguiente expresión: 'salud' es mayor que 50 o no tienes 'escudo'.
# Imprime el resultado.
salud = 100
escudo = False
print(salud > 50 or not escudo)

# Asigna los valores 10, 20 y 30 a las variables 'x', 'y' y 'z', respectivamente.
# Declara una variable con el doble de 'x', calcula e imprime si esta es igual a 'y'
# Luego, compara si 'z' dividido entre 'y' es mayor que 1.
# Compara ambas condiciones entre si e imprime  el resultado.
x = 10
y = 20

doble_x = x * 2
print(doble_x == y)

z = 30
print(doble_x == y and z / y > 1)

# Asigna los valores 7 y 12 a las variables 'bananas' y 'minions', respectivamente.
# Asigna la cadena "Kevin" a la variable 'lider'.
# Evalúa la siguiente expresión: 'bananas' es menor que el doble de 'minions' y
# 'lider' no es igual a "Bob", o no hay suficientes 'bananas' para cada 'minion'.
# Imprime el resultado.
bananas = 7
minions = 12
lider = "Kevin"
print((bananas < 2 * minions and lider != "Bob") or not (bananas >= minions))


# Asigna los valores 12 y 5 a las variables 'a' y 'b'.
# Asigna la cadena "12" a la variable 'c'.
# Evalúa si 'a' es mayor o igual a 'b' y si 'c' es mayor o igual a 'a' en una comparación de tipos diferentes.
# Imprime el resultado.
a = 12
b = 5
c = "12"
# print(b <= a <= c) # Esto tirara error
print(b <= a <= int(c))


# Asigna las cadenas "bob" y "kevin" a las variables 'minion_1' y 'minion_2', respectivamente.
# Luego, evalúa si la longitud de 'minion_1' es mayor o igual a la longitud de 'minion_2',
# o si la longitud de 'minion_2' menos 1 es igual a la longitud de 'minion_1'.
# Imprime el resultado.
minion_1 = "bob"
minion_2 = "kevin"
print(len(minion_1) >= len(minion_2) or len(minion_2) - 1 == len(minion_1))

# Asigna los valores 8, 3 y 12 a las variables 'a', 'b' y 'c'.
# Evalúa la siguiente expresión: 'a' más 'b' es mayor que 'c', y 'c' menos 'b' es mayor o igual a 'a'.
# Imprime el resultado.
a = 8
b = 3
c = 12
print((a + b > c) and (c - b >= a))
