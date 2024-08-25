# 1. Guarda en una variable el nombre de un amigo (amigo). Escribe un programa que imprima las cadenas:
# "Hey" y "Como estas [amigo]?" en dos líneas diferentes
# Tip: Usa una sola declaración print() y el carácter \n para separar las líneas
amigo="Adrián"
print("Hey\nComo estas" ,amigo,"?")
print(f"Hey\nComo estas {amigo}?")

# interpolacion de strings
resultado = 4
print(f"Mi resultado es igual a {3 * 2 + resultado}")

# Ejercicio 2: Operaciones Aritméticas Básicas
# Instrucciones: Realiza las siguientes operaciones aritméticas e imprime los resultados:
# 1. Suma los números 5 y 3
# 2. Resta 9 menos 4
# 3. Multiplica 7 por 2
# 4. Divide 20 entre 5
print(5+3)
print(9-4)
print(7*2)
print(20/5)
# Ejercicio 3: Asignación de Variables
# Instrucciones: Asigna los valores 10 y 3.5 a las variables 'a' y 'b', respectivamente.
# Luego, imprime la suma, resta, multiplicación y división de 'a' y 'b'.
a=10
b=3
print(a+b,a-b,a*b,a/b)
# Ejercicio 4: Tipo de Datos
# Instrucciones: ¿De qué tipo son los datos que has impreso arriba, 'int', 'float', o 'string'?
# Respuesta en un comentario:


# Ejercicio 5: División Entera y Módulo
# Instrucciones: Asigna el valor 27 a la variable 'x' y 4 a la variable 'y'.
# Imprime el resultado de la división entera y del módulo de 'x' entre 'y'.
x=27
y=4
print("Division entera [x//y] es igual a ", x//y)
print("Modulo [x%y] es igual a ", x%y )


# Ejercicio 6: Exponenciación
# Instrucciones: Calcula el resultado de elevar 3 al cubo (3^3) e imprímelo.
numero = 3
print(3**3)
print(numero**numero)

# Ejercicio 7: Suma de Variables
# Instrucciones: Asigna 7 a la variable 'p' y 12 a la variable 'q'. Imprime la suma de 'p' y 'q'.
p=7
q=12
print(p+q)

# Ejercicio 8: Operaciones Combinadas
# Instrucciones: Realiza la siguiente operación combinada: (10 + 5) * 2 - 8, e imprime el resultado.
print((10+5)*2-8)