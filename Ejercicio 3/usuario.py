from datetime import date
from persona import Persona
from datetime import date
from libro import Libro

class Usuario(Persona):

    __list_user_name = [] #atributo de clase

    def __init__(self, user_name:str, email:str, apellido: str, nombre: str, fecha_nacimiento: date, nro_documento: int, password:str, administrator:bool = False) -> None:
        self.__user_name = Usuario.__validar_user_name(user_name)
        self.__password = password
        self.__estado = True #no recibivo el valor por parametro en el constructor, porque lo seteo derecho.
        self.__administrator = administrator
        self.__email = email
        self.__fecha_alta = date.today() #genero la fecha del dia
        self.__fecha_baja = None #Nulo
        self.__libros = [] #lista vacia de libros del usuario, mapeo relación que termina en *
        super().__init__(nombre, apellido, fecha_nacimiento, nro_documento) #llamo al constructor de la clase padre, con sus respectivos argumentos
    
    def get_user_name(self) -> str:
        return self.__user_name
    
    def set_user_name(self, nuevo_usuario) -> str:
        self.__user_name = nuevo_usuario

    def get_password(self) -> str:
        return self.__password
    
    def set_password(self, nueva_password) -> str:
        self.__password = nueva_password

    def get_estado(self) -> str:
        return self.__estado
    
    def set_estado(self, nuevo_estado) -> str:
        self.__estado = nuevo_estado

    def get_email(self) -> str:
        return self.__email
    
    def set_email(self, nuevo_email) -> str:
        self.__email = nuevo_email

    def get_fecha_alta(self) -> date:
        return self.__fecha_alta
    
    def set_fecha_alta(self, nueva_fecha_alta) -> str:
        self.__fecha_alta = nueva_fecha_alta

    def get_fecha_baja(self) -> date:
        return self.__fecha_baja
    
    def set_fecha_baja(self, nueva_fecha_baja) -> str:
        self.__fecha_baja = nueva_fecha_baja
    
    def baja_usuario(self):
        self.__estado = False
        self.__fecha_baja = date.today()    

    #libro:Libro no es una llamada al constructor, es un typehint
    def add_libro(self, libro:Libro): #agrega un obj Libro a la lista __libros que surge de mi relacion con la clase Libro
        self.__libros.append(libro)

    def remove_libro(self, libro:Libro): #remueve el obj Libro de la lista
        self.__libros.remove(libro)

    def leyo_libro(self, isbn:str) -> bool:
        for libro in self.__libros: #recorro toda mi lista de libros
            if libro.get_isbn() == isbn: 
                return True #si el libro encontrado, retorno True
        return False #si no encuentra un libro con el mismo isbn (cod idenficador unico para un libro) en toda mi lista retorno False

    #valida que el user_name y password pasado coincida con lo almacenado en los atributos del objeto
    def validar_credenciales(self, user_name:str, password:str) -> bool:
        return self.__user_name == user_name and self.__password == password

    @classmethod
    def __validar_user_name(cls, user_name:str) -> str:
        if (user_name in Usuario.__list_user_name):
            while user_name in Usuario.__list_user_name or user_name == "":
                user_name = input("Reingrese nombre de usuario: ")
        else: 
            Usuario.__list_user_name.append(user_name)
        print(f"Nombre de usuario de la persona : {user_name}")
        for persona in Usuario.__list_user_name:
            print(persona)
        return user_name


    def __str__(self) -> str:
        return f"Nombre de usuario: {self.__user_name}, email: {self.__email}, apellido : {self._apellido}, nombre : {self._nombre}, contraseña : {self.__password}, numero documento: {self._nro_documento}"
    
    def validar_contraseña() -> str:
        while True:
            contrasena1 = input("Ingrese su contraseña: ")
            contrasena2 = input("Ingrese su contraseña nuevamente: ")

            if contrasena1 != contrasena2:
                print("Las contraseñas no coinciden. Intente nuevamente.")
                continue

            if not (8 <= len(contrasena1) <= 10):
                print("La contraseña debe tener entre 8 y 10 caracteres. Intente nuevamente.")
                continue

            if not re.search(r'\d', contrasena1):
                print("La contraseña debe tener al menos un carácter numérico. Intente nuevamente.")
                continue

            # Si llegamos a este punto, la contraseña es válida
            return contrasena1
    