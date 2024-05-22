from usuario import Usuario

class Persona(Usuario):
    def __init__(self, user_name: str, email: str, password: str) -> None:
        super().__init__(user_name, email, password)

    def printear(self) -> str:
        return super().mostrar()

obj = Persona("Jere", "mias@gmail.com", "ashei")
print(obj.get_email())
print(obj)

    
    