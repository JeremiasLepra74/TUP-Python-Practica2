cliente = []

def reg_cliente():
    global cliente
    compras = []
    nombre = input("Ingrese el nombre: ")
    num_client = input("Ingrese numero de cliente: ")
    for i in cliente:
        if num_client == i["numcliente"]:
            print("Numero de cliente duplicado")
            while num_client == i["numcliente"]:
                num_client = input("Ingrese numero de cliente: ")
    dic = {"nombre" : nombre, "numcliente" : num_client, "compras" : compras}
    cliente.append(dic)


def reg_compra():
    encontrado = 0
    comp_client = input("Ingrese numero de cliente: ")
    for i in cliente:
        if comp_client == i["numcliente"]:
            nueva_comp = input("Ingrese producto : ")
            i["compras"] += {nueva_comp}
            encontrado = 1
            break
    if encontrado == 0:
        print("No se encontro el numero de cliente")

def mos_compra():
    ordenados = sorted(cliente, key=lambda x: len(x["compras"]), reverse=True)
    for i in ordenados:
        print("Nombre : ", i["nombre"])
        print("Compras: ", i["compras"])
        print("Numero de compras: ", len(i["compras"]))
    
while True:
    print("1- Registrar cliente")
    print("2- Agregar compra")
    print("3- Mostrar resumen")
    print("4- Salir")
    opt = input("Ingrese opcion : ")
    if opt == "1":
        reg_cliente()
    if opt == "2":
        reg_compra()
    if opt == "3":
        mos_compra()
    if opt == "4":
        break