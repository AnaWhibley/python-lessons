# Ejercicio 1
# Asigna el valor 5 a la variable 'x'.
# Evalúa si 'x' es mayor que 0.
# Si lo es, imprime "x es positivo".
# Si no, imprime "x es negativo o cero".
x=5
xEsPositivo = x > 0
if xEsPositivo:
    y = 7
    print("x es positivo, e y es igual a " + str(y))
else:
    print("x es negativo")

# Ejercicio 2
# Asigna el valor 8 a la variable 'edad'.
# Evalúa si 'edad' es mayor o igual a 18.
# Si lo es, imprime "Eres mayor de edad".
# Si no, imprime "Eres menor de edad"
edad=8
if edad>=18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")


# Ejercicio 3
# Asigna los valores 15 y 10 a las variables 'a' y 'b'.
# Compara si 'a' es mayor que 'b'.
# Imprime el resultado con el mensaje "a es mayor que b" o "a no es mayor que b".
a=15
b=10
if a==b:
    print("a es mayor que b")
else:
    print("a es menor que b")

# print("a es mayor que b") if a==b else print("a es menor que b") # operador ternario

# Ejercicio 4
# Asigna el valor 20 a la variable 'temperatura'.
# Evalúa si la 'temperatura' es mayor que 30, mayor que 20, o menor o igual a 20.
# Imprime "Hace calor", "Está templado", o "Hace frío" según la condición.
temperatura=20
if temperatura>30:
    print("Hace calor")
elif temperatura>20:
    print("Está templado")
else:
    print("Hace frío")

# Ejercicio 5
# Asigna el valor 7 a la variable 'nota'.
# Evalúa si 'nota' es mayor o igual a 9, mayor o igual a 7, mayor o igual a 5, o menor a 5.
# Imprime "Sobresaliente", "Notable", "Aprobado", o "Suspendido" según la condición.
nota=10
alumno = 'Pepe'
if nota == 10:
    if alumno == 'Alex':
        print('Lo hiciste genial Alex')
    else:
        print(f'Lo hiciste genial {alumno}')
elif nota>=9:
    print('Sobresaliente')
elif nota>=7:
    print("Notable")
elif nota>=5:
    print("Aprobado")
else:
    print("Suspendido")


# Ejercicio 6
# Asigna el valor "mago" a la variable 'personaje'.
# Evalúa si 'personaje' es igual a "mago", "guerrero" o "arquero". => 'magia' | 'defensa' | 'arco'
# Según el valor, asigna una habilidad a la variable 'habilidad'.
# Imprime el valor de 'habilidad' al final.
personaje="animal"
if personaje == "mago":
    habilidad="magia"
elif personaje=='guerrero':
    habilidad='defensa'
elif personaje=="arquero":
    habilidad="arco"
else:
    habilidad = 'ninguna habilidad concreta'
    
print(f"El personaje es de {habilidad}")