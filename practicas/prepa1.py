empleados = []
cant_empl = 2
def reg_emple():
    for i in range(cant_empl):
        cursos = []
        nombre = input("Ingrese nombre : ")
        legajo = input("Ingrese legajo : ")
        while len(legajo) != 5:
            print("Menos o mas de 5 caracteres")
            legajo = input("Ingrese antiguedad (en meses): ")
        for i in empleados:
            if legajo == i["legajo"]:
                print("legajo ya usado")
                while legajo == i["legajo"] or len(legajo) != 5:
                    legajo = input("Ingrese legajo de vuelta: ")
        antiguedad = int(input("Ingrese antiguedad (en meses): "))
        dic = {"nombre" : nombre, "legajo" : legajo, "antiguedad" : antiguedad, "cursos" : cursos}
        empleados.append(dic)

def reg_cursos():
    leg = input("Ingrese legajo de empleado: ")
    encontrado = 0
    for i in empleados:
        if leg == i["legajo"]:
            curso = input("Ingrese curso realizado: ")
            i["cursos"] += {curso}
            encontrado = 1
    if encontrado == 0:
        print("legajo no encontrado")

def most_emplead():
    ordenados = sorted(empleados, key=lambda x : len(x["cursos"]), reverse=True)
    numero_empl = 0
    for i in ordenados:
        numero_empl = numero_empl + 1
        print(numero_empl)
        print("Nombre: ", i["nombre"])
        print("Legajo: ", i["legajo"])
        print("Antiguedad: ", i["antiguedad"], " meses")
        print("Cantidad de cursos: ", len(i["cursos"]))
        print("Cursos: ", i["cursos"])
        print("")
        if (i["antiguedad"] / len(i["cursos"]) > 6):
            print("No cumple")
        if (i["antiguedad"] / len(i["cursos"]) <= 6):
            print("Si cumple")
        
    
while True:
    print("1- Registrar empleado")
    print("2- Registrar curso")
    print("3- Mostrar empleados")
    print("4- Salir")
    opt = input("Ingrese opcion: ")
    if opt == "1":
        reg_emple()
    if opt == "2":
        reg_cursos()
    if opt == "3":
        most_emplead()
    if opt == "4":
        break
