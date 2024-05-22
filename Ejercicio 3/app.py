from datos import *
from usuario import Usuario
from datetime import date, datetime
from libro import Libro

lista_personas = []
lista_libros = [] #Como agregarlos a la lista

while True:
    print("1: Agregar nuevo usuario")
    print("2: Mostrar lista de personas")
    print("3: Buscar usuario")
    print("4: Buscar libro")
    print("5: Ver libros del usuario")
    print("6: Agregar libro")
    print("7: Eliminar libro")
    print("8: Cerrar sesion")
    print("9: Mostrar lista personas desde usuario")
    seleccion = input("Ingrese numero a elegir: ")
    if seleccion == "1":
        nom_us = input("Ingresa el nombre de usuario: ")
        while nom_us == "":
            nom_us = input("Ingresa el nombre de usuario: ")
        email = input("Ingrese email: ")
        apellido = input("Ingrese apellido: ")
        nombre = input("Ingrese nombre: ")
        anio = int(input("Ingrese año de nacimiento: "))
        mes = int(input("Ingrese mes (en numero) de nacimiento: "))
        dia = int(input("Ingrese dia de nacimiento: "))
        fecha_nac = date(anio, mes, dia) # (Esta de ejemplo como para hacer algo) -> Como pasar para que la persona ponga su fecha de nacimiento
        num_doc = input("Ingrese numero de documento: ") #Como elegir desde datos (Tipos de documento)
        contra = input("Ingrese contraseña: ") #Como validar la contraseña desde Usuario.validar_contraseña
        for i,tipodocumento in enumerate(tipos_documento, 1):
            print(f"{i} {tipodocumento}")
        persona = Usuario(nom_us, email, apellido, nombre, fecha_str, num_doc, contra)
        lista_personas.append(persona)
    elif seleccion == "2":
        for persona in lista_personas:
            print(persona)
        indice = input("Ingrese num de tipo doc")
    elif seleccion == "3":
        pass
    elif seleccion == "5":
        for libros in lista_libros:
            print(libros) #Como mostrar los libros
    elif seleccion =="6":
        nom_lib = input("Ingrese nombre del libro: ")
        mes_lanzamiento = date.today() #Como mostrar el mes en el que fue lanzado (tira error)
        autor = input("Ingrese nombre del autor del libro: ")
        libro = Libro(nom_lib, mes_lanzamiento, autor)
        lista_libros.append(libro)