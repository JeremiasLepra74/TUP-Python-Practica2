from abc import ABC, abstractmethod
from datetime import date
class Persona(ABC):
    @classmethod
    
    def __init__(self, nombre, apellido, fecha_nacimiento, edad: int, nro_documento: int) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.edad = edad
        self.nro_documento = nro_documento

    def presentarse(self):
        print(f"Hola, me llamo: {self.nombre} {self.apellido} , naci el dia: {self.fecha_nacimiento} tengo : {self.edad} años, mi documento es: {self.nro_documento}")

class MosPer(Persona):
    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()
    

perinola = Persona("Jeremias", "Carreri", "31-12-04", 19, 46294522)

class Usuario(Persona):

    def __init__(self, user_name:str, email:str, password:str) -> None:
        self.__user_name= user_name
        self.__email = email
        self.__password = password
        self.__fecha_alta = date.today()
        self.__fecha_baja = None
        self.__estado = True
        
    def get_user_name(self) -> str:
        return self.__user_name
    
    def get_email(self) -> str:
        return self.__email
    
    def get_password(self) -> str:
        return self.__password

    def dar_baja(self):
        self.__estado = False
        self.__fecha_baja = date.today()
        
    def validar_credenciales(self, user_name, password):
        return self.__user_name == user_name and self.__password == password
    
    def set_user_name(self, nuevo_usuario) -> str:
        self.__user_name = nuevo_usuario
    
    def set_email(self, nuevo_email) -> str:
        self.__email = nuevo_email
    
    def set_password(self, nueva_password) -> str:
        self.__password = nueva_password
    
    def set_baja(self):
        self.__estado = False
        self.__fecha_baja = date.today()

    def mostrar(self) -> str:
        return "personitas"

