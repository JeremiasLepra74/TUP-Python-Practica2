from datetime import date, time, datetime
from precio import Precio

class Estadia():
    lista_patentes = [
    ]
    def __init__(self, fecha : date, nro_patente: str, hora_entrada: time, hora_salida: time) -> None:
        self.__fecha = datetime.now().date()
        self.__nro_patente = nro_patente
        self.__hora_entrada = datetime.now()
        self.__hora_salida = hora_salida
        self.__pagado = False
        self.__estado = "activo"

    @property
    def fecha(self) -> str:
        return self.__fecha  
    
    @fecha.setter
    def fecha(self, new_fecha:str):
        self.__fecha = new_fecha
        
    @property
    def nro_patente(self) -> str:
        return self.__nro_patente
    
    @nro_patente.setter
    def nro_patente(self, new_nro_patente:str):
        self.__nro_patente= new_nro_patente

    @property
    def hora_entrada(self) -> str:
        return self.__hora_entrada
    
    @hora_entrada.setter
    def hora_entrada(self, new_hora_entrada:str):
        self.__hora_entrada = new_hora_entrada

    @property
    def hora_salida(self) -> str:
        return self.__hora_salida
    
    @hora_salida.setter
    def hora_salida(self, new_hora_salida:str):
        self.__hora_salida = new_hora_salida

    @property
    def cant_horas(self) -> str:
        dif_min = self.__hora_salida.minute - self.__hora_entrada.minute
        if (dif_min > 30):
            return (self.__hora_salida.hour - self.__hora_entrada.hour) + 1
        return self.__hora_salida.hour - self.__hora_entrada.hour
    
    @property    
    def estado(self) -> str:
        return self.__estado
    
    @estado.setter
    def estado(self, new_estado:str):
        self.__estado = new_estado
        
    @property    
    def pagado(self) -> str:
        return self.__pagado
    
    @pagado.setter
    def pagado(self, new_pagado:str):
        self.__pagado = new_pagado
    
    #registrar entrada
    def registrar_entrada(self, nro_patente):
        if nro_patente in Estadia.lista_patentes:
            print(f"Error: La patente {nro_patente} ya está registrada.")
        else:
            Estadia.lista_patentes.append(nro_patente)
            self.__nro_patente = nro_patente
            print(f"Patente {nro_patente} registrada correctamente.")

    #Hacer funcion de registrar salida y dentro de este mismo archivo importar precio
    def registrar_salida(self) -> float:
        self.__pagado = True
        self.__hora_salida = datetime.now().time()
        return Precio.calcularimporte(self.cant_horas)
    
    def  __str__(self) -> str:
        return f"""fecha: {datetime.now}
        patente: {self.__nro_patente}
        hora entrada: {self.__hora_entrada}
        hora salida: {self.__hora_salida}
        pagado: {self.__pagado}
        """