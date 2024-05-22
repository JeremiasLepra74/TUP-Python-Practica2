# Ejercicio 561: Crear una función lambda para filtrar los números pares de una lista.

numeros = list(range(1, 11))
#numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(map(lambda x: x % 2 == 0, numeros))
print(pares)

print()

pares = list(filter(lambda n: n % 2 == 0, numeros))
print(pares)
# Ejercicio 563: Crear una función lambda para generar números cuadrados.

numeros = list(range(1, 11))
print(numeros)

print()

cuadrados = list(map(lambda n: n ** 2, numeros))
print(cuadrados)
# Ejercicio 570: Crear una función lambda para convertir a mayúscula varias cadenas.

lenguajes = ['Python', 'JavaScript', 'Java', 'PHP', 'C++', 'Perl']
print(lenguajes)

print()

resultado = list(map(lambda c: c.upper(), lenguajes))
print(resultado)
# Ejercicio 572: Crear una función lambda para obtener las palabras con longitud mayor a 5.

lenguajes = ['Python', 'PHP', 'C', 'C++', 'Java', 'JavaScript', 'C#']
print(lenguajes)

print()

resultado = list(filter(lambda l: len(l) > 5, lenguajes))
print(resultado)
for e in resultado:
    print(e)