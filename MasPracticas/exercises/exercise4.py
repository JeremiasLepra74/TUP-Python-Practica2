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


###############################################################################


def es_vocal_if_in(letra: str) -> bool:
    """Re-escribir utilizando un sólo IF y el operador IN.

    Restricciónes:
        - Utilizar un único IF.
        - Utilizar dos returns.
        - No utilizar ELSE.
        - No utilizar FOR.
        - No utilizar listas.

    Referencia: https://docs.python.org/3/reference/expressions.html#membership-test-operations # noqa: E501
    """
    letra = letra.lower()
    if letra in "aeiou":
        return True
    return False

"""letra = letra.lower()
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        return True
    else:
        return False
    
    """

# NO MODIFICAR - INICIO
print(es_vocal_if_in("a"))
print(es_vocal_if_in("b"))
print(es_vocal_if_in("A"))
# NO MODIFICAR - FIN


###############################################################################


def es_vocal_in(letra: str) -> bool:
    """Re-escribir como expresión booleana utilizando el operador IN

    Restricciónes:
        - No utilizar IF.
        - Utilizar un único return.
        - No utilizar FOR.
        - No utilizar listas.
    """
    return letra.lower() in "aeiou"
# NO MODIFICAR - INICIO
print(es_vocal_in("a"))
print(es_vocal_in("b"))
print(es_vocal_in("A"))
# NO MODIFICAR - FIN