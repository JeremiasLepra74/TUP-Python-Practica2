from llamar import validar_numero_documento
medicos = []
num_med = 1
def registrar_medico():
    global medicos
    titulos_realizados = []
    nombre = input("Nombre y apellido: ")
    dni = input("Ingrese su dni: ")
    while validar_numero_documento(medicos, dni) or ((len(dni) < 7) or len(dni) > 8):
        if ((len(dni) < 7) or len(dni) > 8):
            print("Cantidad de numeros incorrecto")
        if validar_numero_documento(medicos, dni):
            print("El dni ingresado ya existe")
        dni = input("Ingrese el numero de documento: ")
    dic = {"nombre": nombre, "dni" : dni, "titulos" : titulos_realizados}
    medicos.append(dic)
    return medicos
        

def agregar_titulo():
    num_doc = input("Ingrese dni a buscar: ")
    encontrado = 0
    for i in medicos:
        if num_doc == i["dni"]:
            titulo = input("Ingrese titulo: ")
            i["titulos"] += {titulo}
            encontrado = 1
    if encontrado == 0:
        print("Dni no encontrado")

def mostrar_med():
    ordenado = sorted(medicos, key=lambda x: len(x["titulos"]), reverse=True)
    med = 0
    for i in ordenado:
          med = med + 1
          print(med)
          print(i["nombre"], "- Nro Doc: ", i["dni"])
          print("Cursos realizados: ", i["titulos"])
          print("Cantidad cursos realizados: ", len(i["titulos"]))
          print("")
    
while True:
    print("1- Registrar medicos")
    print("2- Agregar titulo")
    print("3- Mostrar resumen")
    print("4- Salir")
    opt = input("Ingrese una opcion: ")
    if opt == "1":
        registrar_medico()
    if opt == "2":
        agregar_titulo()
    if opt == "3":
        mostrar_med()
    if opt == "4":
         break
    


""" if dni == i["dni"]:
            print("Dni ya registrado")
            break
    if dni != i["dni"]:
             """