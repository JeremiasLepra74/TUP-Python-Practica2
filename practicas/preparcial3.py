estudiantes = []

def agregar_alumnos():
    global estudiantes
    cant_est = 2
    for i in range(cant_est):
        nombre = input("Nombre: ")
        num_ide = input("Ingrese numero de identificaion estudiantil: ")
        while len(num_ide) > 6 or len(num_ide) < 6:
            print("Numero mayor a 6 caracteres")
            num_ide = input("Ingrese numero de identificaion estudiantil: ")
        for x in estudiantes: #se llama directamente a la lista (Porque ya esta cargada de la primera persona que se usó)
             if num_ide == x["identificador"]:
                while num_ide == x["identificador"]:
                    print("Identificador ya esta usado")
                    num_ide = input("Ingrese numero de identificaion estudiantil: ")
                
        notas = []
        for i in range(3):
            nota = float(input(f"Ingrese la nota {i+1}: "))
            notas.append(nota)
        total = sum(notas)
        prom_alum = total / len(notas)
        if prom_alum >= 7:
             aprueba = "cumple con los estandares"
        if prom_alum < 7:
             aprueba = "no cumple con los estandares"
        dic = {"nombre" : nombre, "identificador" : num_ide, "notas": notas, "totalnotas": total, "promedio" : prom_alum,
               "aprueba" : aprueba}
        estudiantes.append(dic)

def agregar_nota():
    encontrado = 1
    iden = input("Ingrese el numero de identificacion: ")
    while len(iden) > 6 or len(iden) < 6:
            print("Numero mayor a 6 caracteres")
            iden = input("Ingrese numero de identificaion estudiantil: ")
    for i in estudiantes:
        if iden == i["identificador"]:
            nota = float(input("Ingrese la nota del estudiante: "))
            i["notas"] += {nota}
        if iden != i["identificador"]:
             encontrado = 0
    if encontrado == 0:
         print("No encontrado")
        
def most_resumen():
    ordenados = sorted(estudiantes, key=lambda x: x["promedio"], reverse=True)
    for i in ordenados:
        print(f"Nombre: {i['nombre']}")
        print(f"Numero de identificación estudiantil: {i['identificador']}")
        print(f"Calificaciones obtenidas: {i['notas']}")
        print(f"Promedio de calificaciones: {i['promedio']}")
        print(f"Estado: {i['aprueba']}")
        print()

while True:
    print("1- Agregar alumnos")
    print("2- Agregar notas")
    print("3- Mostrar resumen")
    print("4- Salir")
    opt = input("Seleccione item: ")
    if opt == "1":
        agregar_alumnos()
    if opt == "2":
        agregar_nota()
    if opt == "3":
        most_resumen()
        
    if opt == "4":
        break