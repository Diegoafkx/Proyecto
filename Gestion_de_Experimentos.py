import random
from Experimento_y_Recetas import __Experimnto_y_Receta
import json

class Gestion_de_Experimentos(__Experimnto_y_Receta):
    def __init__(self):
        super().__init__()
        Gestion_de_Experimentos.Lector_de_Datos(self)
        
    def Analizador_de_Informacion_Experimento(self,indicador_de_experimento,accion):
        experimentos_copia = []
        for s in self._experimentos:    
            self._id_experimento = s.get("id")
            self._receta_id = s.get("receta_id")
            self._personas_responsables = s.get("personas_responsables")
            self._fecha = s.get("fecha")
            self._costo_asociado = s.get("costo_asociado")
            self._resultado = s.get("resultado")

            if accion == 1:
                if indicador_de_experimento == self._id_experimento:
                    return s

            elif accion == 2:
                if indicador_de_experimento == self._id_experimento:
                    Gestion_de_Experimentos.Configurar_Experimento(self)
                aux = {"id":self._id_experimento,"receta_id":self._receta_id,"personas_responsables":self._personas_responsables,"fecha":self._fecha ,"costo_asociado":self._costo_asociado ,"resultado":self._resultado}
               
                experimentos_copia.append(aux)
                
            elif accion == 3:
                if indicador_de_experimento == self._id_experimento:
                    pass
                else:
                    if indicador_de_experimento < self._id_experimento:
                        aux = {"id":self._id_experimento -1,"receta_id":self._receta_id,"personas_responsables":self._personas_responsables,"fecha":self._fecha ,"costo_asociado":self._costo_asociado ,"resultado":self._resultado}
                    else:
                        aux = {"id":self._id_experimento,"receta_id":self._receta_id,"personas_responsables":self._personas_responsables,"fecha":self._fecha ,"costo_asociado":self._costo_asociado ,"resultado":self._resultado}
                    experimentos_copia.append(aux)

        if accion == 2 or accion == 3:
            self._experimentos = experimentos_copia
                
    def Analizador_de_Informacion_Recetas(self,indicador_de_receta,accion):
        for s in self._recetas:
            self._id_receta = s.get("id")
            self._nombre = s.get("nombre")
            self._objetivo = s.get("objetivo")
            self._reactivos_utilizados = s.get("reactivos_utilizados")
            self._procedimiento = s.get("procedimiento")
            self._valores_a_medir = s.get("valores_a_medir")
            
            
            if accion == 1:
                if self._id_receta == indicador_de_receta:
                    return s
            
            elif accion == 2:
                if self._id_receta == self._receta_id:
                    return s
            
    def Agregar_Editar_o_Eliminar_Experimento(self,):
        accion = int(input("Que deseas realizar\n1-Agregar\n2-Editar\3-Eliminar"))
        if accion == 1:
            for s in self._experimentos:    
                self._id_experimento = max(s.get("id")) + 1
            

        elif accion == 2:
            self._id_experimento = int(input("Ingresa el ID del experimento que deseas editar: "))
            Gestion_de_Experimentos.Analizador_de_Informacion_Experimento(self,self._id_experimento,accion)
            Gestion_de_Experimentos.Configurar_json(self)
            return "se edito el experimento exitosamente."
        
        elif accion == 3:
            self._id_experimento = int(input("Ingresa el ID del experimento que deseas eliminar: "))
            Gestion_de_Experimentos.Analizador_de_Informacion_Experimento(self,self._id_experimento,accion)
            Gestion_de_Experimentos.Configurar_json(self)
            return "se edito el experimento exitosamente."
    
    def Configurar_Experimento(self):
        self._id_receta_buscador = int(input("Ingresa el ID de la receta que vas a utilizar: "))
        self._personas_responsables = []
        self._personas_responsables.append((input("Ingrese las personas responsables del proyecto: ").split(",")))
        self._fecha = input("Ingresa la fecha: ")
        self._costo_asociado = int(input("Ingresa el costo asociado: "))
        self._resultado = input("Ingresa el resultado: ")

    def Configurar_json(self):
        archivo = open("Experimentos.json","w", encoding = "utf-8")
        for s in self._experimentos:
            aux = json.dumps(s)
            archivo.write(f"{aux}\n")
            archivo.close()
            archivo = open("Experimentos.json","a", encoding = "utf-8")
        archivo.close()

    def Hacer_Experimento(self):
        self._id_receta = int(input("Ingresa el ID de la receta que vas a utilizar: "))
        self._receta = Gestion_de_Experimentos.Analizador_de_Informacion_Recetas(self,self._id_receta,1)
        print(f"Receta: {self._receta}")
        print(f"Objetivo: {self._receta.get('objetivo')}")
        print(f"Reactivos utilizados: {self._receta.get('reactivos_utilizados')}")
        print(f"Procedimiento: {self._receta.get('procedimiento')}")
        print(f"Valores a medir: {self._receta.get('valores_a_medir')}")
        self._personas_responsables = []
        self._personas_responsables.append((input("Ingrese las personas responsables del proyecto: ").split(",")))
        

hola = Gestion_de_Experimentos()
print(hola)
while True:
    hola.Agregar_Editar_o_Eliminar_Experimento()
