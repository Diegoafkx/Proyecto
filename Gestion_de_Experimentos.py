from Receta import __Receta
from Experimento import __Experimnto

class Gestion_de_Experimentos(__Experimnto,__Receta):
    def __init__(self):
        super().__init__()
        Gestion_de_Experimentos.Lector_de_Datos(self)