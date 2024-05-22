"""For, Sum, Reduce."""


def sumatoria_basico(n: int) -> int:
    """Devuelve la suma de los números de 1 a N.

    Restricción: Utilizar un bucle FOR.
    """
    resultado = 0
    for i in range(n+1):
        resultado = resultado + i
    return resultado

# NO MODIFICAR - INICIO
print(sumatoria_basico(1))
#== 1
print(sumatoria_basico(100))
#== 5050
# NO MODIFICAR - FIN


###############################################################################


def sumatoria_sum(n: int) -> int:
    """Re-Escribir utilizando la función sum.

    Restricción: No utilizar bucles (FOR, WHILE, etc)
    Referencia: https://docs.python.org/3/library/functions.html#sum
    """
    return sum(range(n+1))

# NO MODIFICAR - INICIO
print(sumatoria_sum(1))
#== 1
print(sumatoria_sum(100))
#== 5050
# NO MODIFICAR - FIN


###############################################################################


from typing import Iterable  # noqa: E402


from typing import Iterable  # noqa: E402

def multiplicar_basico(numeros: Iterable[float]) -> float:
    """Toma un lista de números y devuelve el producto todos los númereos. Si
    la lista está vacia debe devolver 0.

    Restricciones:
        - No usar bibliotecas auxiliares (Numpy, math, pandas).
        - Utilizar un bucle FOR
        - Utilizar múltiples Return
        - No utilizar ELSE
    """
    suma = numeros[0]
    resultado = 0
    i = 0
    for i in numeros:
        print(i)
        suma = suma * (i+1)
        print(suma)
        print()

    return suma
    # return resultado

    """
    limite = numeros[-1]
    suma = numeros[0]
    resultado = 0
    i = 0
    total = 0
    print(type(numeros))
    print(limite)
    for i in numeros:
        suma = suma * (i+1)
    return suma
    """



# NO MODIFICAR - INICIO
print(multiplicar_basico([1, 2, 3, 4]))
# #== 24
#print(multiplicar_basico([2, 5]))
# #== 10
# print(multiplicar_basico([]))
# #== 0
# print(multiplicar_basico([1, 2, 3, 0, 4, 5]))
# #== 0
