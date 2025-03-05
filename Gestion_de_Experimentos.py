from Receta import __Receta
from Experimento import __Experimnto

class Gestion_de_Experimentos(__Experimnto,__Receta):
    def __init__(self):
        super().__init__()
        Gestion_de_Experimentos.Lector_de_Datos(self)
        
    def Analizador_de_Informacion_Recetas(self,indicador_de_receta,accion):
        self._id_receta = None
        self._nombre = None
        self._objetivo = None
        self._reactivos_utilizados = []
        self._procedimiento = []
        self._valores_a_medir = []
        self._receta = []
    
    
    def Analizador_de_Informacion_Experimento(self,indicador_de_experimento,accion):
           
