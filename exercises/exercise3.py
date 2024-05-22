"""Único return vs múltiples return."""

from typing import Union

def operacion_basica(a: float, b: float, multiplicar: bool) -> Union[float, str]:  # noqa: E501
    """Toma dos números (a, b) y un booleano (multiplicar):
        - Si multiplicar es True: devuelve la multiplicación entre a y b.
        - Si multiplicar es False: devuelve la division entre a y b.
        - Si multiplicar es False y b es cero: devuelve "Operación no válida".

    Restricciones:
        - Utilizar un único return.
        - Utilizar IF con ELIF con ELSE.
        - No utilizar AND ni OR.
    """
    resultado = None
    if multiplicar:
        resultado = a * b
    elif b != 0:
        resultado = a / b
    else:
        resultado = "Operación no válida"
    return resultado

# NO MODIFICAR - INICIO
print(operacion_basica(1, 1, True))
#== 1
print(operacion_basica(1, 1, False))
#== 1
print(operacion_basica(25, 5, True))
#== 125
print(operacion_basica(25, 5, False))
#== 5
print(operacion_basica(0, 5, True))
#== 0
print(operacion_basica(0, 5, False))
#== 0
print(operacion_basica(1, 0, True))
#== 0
print(operacion_basica(1, 0, False))
#== "Operación no válida"
# NO MODIFICAR - FIN



###############################################################################


"""Expresiones Booleanas."""


def es_vocal_if(letra: str) -> bool:
    """Toma un string y devuelve un booleano en base a si letra es una vocal o
    no.

    Restricciónes:
        - Utilizar un if para cada posibilidad.
        - Utilizar la función lower() sólo una vez.
        - No utilizar ELSE.
        - Utilizar 6 returns.

    Referencia: https://docs.python.org/3/library/stdtypes.html#string-methods
    """
    letra = letra.lower()

    if letra == "a":
        return True
    if letra == "e":
        return True
        
    if letra == "i":
        return True
        
    if letra == "o":
        return True
    if letra == "u":
        return True
    return False
# NO MODIFICAR - INICIO
print(es_vocal_if("a"))
print(es_vocal_if ("b"))
print(es_vocal_if ("A"))
print(es_vocal_if ("e"))
print(es_vocal_if("E"))
# NO MODIFICAR - FIN