

from estadia import *
from datetime import *
from datos import *

estadia = Estadia() #no importa estadia

def mostrar_menu():
    print("1. Ingresar estadía")
    print("2. Finalizar estadía")
    print("3. Salir")

while True:
     mostrar_menu()
     opcion = input("Seleccione una opción: ")
     
     if opcion == '1':
          nro_patente = input("Ingrese el número de patente: ")
          estadia.registrar_entrada(nro_patente) 
     elif opcion == '2':
          nro_patente = input("Ingrese el número de patente: ")
          estadia.registrar_salida(nro_patente)
     elif opcion == '3':
          break
     else:
          print("Opción no válida. Por favor, intente nuevamente.")

 """

from datetime import datetime, timedelta

class Precio:
    precio_por_hora = 10.0  # Precio fijo por hora

class Estadia:
    def __init__(self, nro_patente):
        self.nro_patente = nro_patente
        self.fecha = datetime.now().date()
        self.hora_entrada = datetime.now()
        self.hora_salida = None
        self.estado = 'ACTIVO'
        self.pagado = False

    def finalizar_estadia(self):
        self.hora_salida = datetime.now()
        duracion = self.hora_salida - self.hora_entrada
        horas, resto = divmod(duracion.total_seconds(), 3600)
        if resto >= 1800:
            horas += 1
        importe = horas * Precio.precio_por_hora
        self.estado = 'PAGADO'
        self.pagado = True
        return importe

    def __str__(self):
        hora_salida_str = self.hora_salida.strftime('%H:%M') if self.hora_salida else 'N/A'
        return (f"fecha: {self.fecha.strftime('%d/%m/%Y')}\n"
                f"patente: {self.nro_patente}\n"
                f"hora entrada: {self.hora_entrada.strftime('%H:%M')}\n"
                f"hora salida: {hora_salida_str}\n"
                f"pagado: {self.pagado}")

class Garaje:
    def __init__(self):
        self.estadias = {}

    def ingresar_estadia(self, nro_patente):
        if nro_patente in self.estadias:
            print(f"Error: El vehículo con patente {nro_patente} ya está en el garaje.")
            return
        self.estadias[nro_patente] = Estadia(nro_patente)
        print(f"Vehículo con patente {nro_patente} ingresado correctamente.")

    def finalizar_estadia(self, nro_patente):
        if nro_patente not in self.estadias:
            print(f"Error: No se encontró vehículo con patente {nro_patente}.")
            return
        estadia = self.estadias[nro_patente]
        if estadia.estado == 'PAGADO':
            print(f"Error: La estadía del vehículo con patente {nro_patente} ya fue pagada.")
            return
        importe = estadia.finalizar_estadia()
        print(f"Importe a abonar: ${importe:.2f}")
        print(estadia)

def mostrar_menu():
    print("1. Ingresar estadía")
    print("2. Finalizar estadía")
    print("3. Salir")

def main():
    garaje = Garaje()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            nro_patente = input("Ingrese el número de patente: ")
            garaje.ingresar_estadia(nro_patente)
        elif opcion == '2':
            nro_patente = input("Ingrese el número de patente: ")
            garaje.finalizar_estadia(nro_patente)
        elif opcion == '3':
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")

if __name__ == "__main__":
    main()

    """ 