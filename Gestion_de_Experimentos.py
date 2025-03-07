from Receta import __Receta
from Experimento import __Experimnto
import json

class Gestion_de_Experimentos(__Experimnto,__Receta):
    def __init__(self):
        super().__init__()
        Gestion_de_Experimentos.Lector_de_Datos_E(self)
        Gestion_de_Experimentos.Lector_de_Datos_R(self)

    def Analizador_de_Informacion_Experimento(self,indicador_de_experimento,accion):
        for s in self._experimentos:    
            self._id_experimento = s.get("id")
            self._receta_id = s.get("receta_id")
            self._personas_responsables = s.get("personas_responsables")
            self._fecha = s.get("fecha")
            self._costo_asociado = s.get("costo_asociado")
            self._resultado = s.get("resultado")
                
    def Analizador_de_Informacion_Recetas(self,accion):
        self._receta = []
        for s in self._recetas:
            self._id_receta = s.get("id")
            self._nombre = s.get("nombre")
            self._objetivo = s.get("objetivo")
            self._reactivos_utilizados = s.get("reactivos_utilizados")
            self._procedimiento = s.get("procedimiento")
            self._valores_a_medir = s.get("valores_a_medir")
            
    def Agregar_Editar_o_Eliminar_Experimento(self,indicador_de_experimento,accion):
        accion = int(input("Que deseas realizar\n1-Agregar\n2-Editar\3-Eliminar"))
        if accion == 1:
            for s in self._experimento:    
                self._id_experimento = max(s.get("id")) + 1

            archivo = open("Experimentos.json","a", encoding = "utf-8")
            aux = {"id":self._id_experimento,"receta_id":self._receta_id,"personas_responsables":self._personas_responsables,"fecha":self._fecha ,"costo_asociado":self._costo_asociado ,"resultado":self._resultado}
            self._reactivos.append(aux)
            aux = json.dumps(aux)
            archivo.write(f"{aux}\n")
            archivo.close()
            return "se agrego el experimento exitosamente."

        elif accion == 2:
            self._id_experimento = int(input("Ingresa el ID del experimento que deseas editar: "))
            Gestion_de_Experimentos.Configurar_Experimento(self)
            self._experimentos.update({"id":self._id_experimento,"receta_id":self._receta_id,"personas_responsables":self._personas_responsables,"fecha":self._fecha ,"costo_asociado":self._costo_asociado ,"resultado":self._resultado})
        elif accion == 1:
            pass
    
    def Configurar_Experimento(self):
        self._id_receta_buscador = int(input("Ingresa el ID de la receta que vas a utilizar: "))
        self._personas_responsables = input("Ingrese las personas responsables del proyecto: ")
        self._fecha = input("Ingresa la fecha: ")

hola = Gestion_de_Experimentos()
print(hola)
