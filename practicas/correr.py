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
    
    
    # return resultado



# NO MODIFICAR - INICIO
print(multiplicar_basico([1, 2, 3, 4]))
# #== 24
print(multiplicar_basico([2, 5]))
# #== 10
# print(multiplicar_basico([]))
# #== 0
# print(multiplicar_basico([1, 2, 3, 0, 4, 5]))
# #== 0
# NO MODIFICAR - FIN
