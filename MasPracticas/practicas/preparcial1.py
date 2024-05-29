empleados = []
ya_hecho = True
cant_cursos = 0
def registrar_empleados():
    while ya_hecho:
        for i in range(2):
            nombre = input("Ingrese nombre: ")
            legajo = input("Ingrese legajo: ")
            mismoleg = False
            for i in empleados:
                if legajo == i["legajo"]:
                      print("Legajo ya usado")
                      legajo = input("Reingrese legajo: ")
                      mismoleg = True
                if legajo != i["legajo"]:
                           mismoleg = False
            while len(legajo) != 5 or mismoleg:
                legajo = input("Ingrese legajo: ")
            antigueda = int(input("Ingrese antiguedad (en meses): "))
            curs_real = int(input("Ingrese la cantida de cursos realizados desde que esta en la empresa: "))
            dic = {"cursos" : [], "nombre" : nombre, "legajo" : legajo, "antiguedad": antigueda, "Cantidad de cursos: ": curs_real}
            empleados.append(dic)
        return empleados

def agregar_curso():
    com_legajo = input("Ingrese legajo a buscar ")
    encontrado = 0
    for i in empleados:
          if com_legajo == i["legajo"]:
               print("El legajo es el indicado ")
               curso = input("Ingrese curso hecho: ")
               i["cursos"] += {curso}
            #    i["Cantidad de cursos: "] += 1
               
               encontrado = 1
               break
    if encontrado == 0:
        print("Legajo no encontrado")

def mostrar_cursos():
     num_persona = 0
     for i in empleados:
            num_persona = num_persona + 1
            print(num_persona)
            print(i["nombre"], "- Legajo: ", i["legajo"], "- Antiguedad: ", i["antiguedad"])
            print("Cursos: ", i["cursos"])
            print("Cantidad de cursos: ", i["Cantidad de cursos: "])
            if (i["antiguedad"] / i["Cantidad de cursos: "]) > 6:
                 print("NO cumple con el estandar")
            if (i["antiguedad"] / i["Cantidad de cursos: "]) <= 6:
                 print("Cumple con el estandar")
            
while True:
    print("1 - Registrar empleados")
    print("2 - Agregar nuevo curso")
    print("3 - Mostrar resumen")
    print("4 - Salir")
    opt = input("Ingrese una opcion del menu: ")
    if opt == '1':
        if ya_hecho == False:
                print("Ya ha cargado datos")
        while ya_hecho:
            registrar_empleados()
            ya_hecho = False
    elif opt == '2':
        agregar_curso()
    elif opt == '3':
        mostrar_cursos()
    elif opt == '4':
        break
print("Gracias por utilizar nuestro sistema.")