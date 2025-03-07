from Receta import __Receta
from Experimento import __Experimnto

class Gestion_de_Experimentos(__Experimnto,__Receta):
    def __init__(self):
        super().__init__()
        Gestion_de_Experimentos.Lector_de_Datos_E(self)
        Gestion_de_Experimentos.Lector_de_Datos_R(self)

    def Analizador_de_Informacion_Experimento(self,indicador_de_experimento,accion):
        for s in self._experimento:    
            self._id_experimento = s.get("id")
            self._receta_id = s.get("receta_id")
            self._personas_responsables = s.get("personas_responsables")
            self._fecha = s.get("fecha")
            self._costo_asociado = s.get("costo_asociado")
            self._resultado = s.get("resultado")
                
    def Analizador_de_Informacion_Recetas(self):
        for s in self._receta:
            self._id_receta = s.get("id")
            self._nombre = s.get("nombre")
            self._objetivo = s.get("objetivo")
            self._reactivos_utilizados = s.get("reactivos_utilizados")
            self._procedimiento = s.get("procedimiento")
            self._valores_a_medir = s.get("valores_a_medir")
            
    def Agregar_Editar_o_Eliminar_Experimento(self,indicador_de_experimento,accion):
        if accion == 1:
            for s in self._experimento:    
                self._id_experimento = max(s.get("id")) + 1
            

        elif accion == 2:
            pass

        elif accion == 1:
            pass
    
    def Configurar_Experimento(self):
        self._id_receta = int(input("Ingresa el ID de la receta que vas a utilizar: "))
        self._personas_responsables = input("Ingrese las personas responsables del proyecto: ")
        self._fecha = input("Ingresa la fecha: ")
hola = Gestion_de_Experimentos()
print(hola)
