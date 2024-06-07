class Precio():
    precio_hora = float(1500)
    @classmethod
    def calcularimporte(cls, cant_hora : int) -> float:
        return float(cant_hora * cls.precio_hora)