import random
from Experimento_y_Recetas import __Experimnto_y_Receta
import json
from Gestion_de_Reactivos import Gestion_de_Reactivos 

class Gestion_de_Experimentos(__Experimnto_y_Receta):
    def __init__(self):
        super().__init__()
        Gestion_de_Experimentos.Lector_de_Datos(self)
        
    def Analizador_de_Informacion_Experimento(self,indicador_de_experimento,accion):
        #Este modulo se encarga de leer la informacion de la lista de experimento y asociarlos a atributos del modulo.
        #Auxilia al metodo de editar, eliminar y mostrar los experimentos existentes
        #El parametro indicador de eexperimento contiene el id de un experimento espeecifico para ciertas acciones 
        #El parametro accion es el que indica cual es el meetodo que va a auxiliar
        experimentos_copia = []
        for s in self._experimentos:    
            self._id_experimento = s.get("id")
            self._receta_id = s.get("receta_id")
            self._personas_responsables = s.get("personas_responsables")
            self._fecha = s.get("fecha")
            self._costo_asociado = s.get("costo_asociado")
            self._resultado = s.get("resultado")

            if accion == 0:
                #Esta accion imprime la informacion de todos los experimentos
                Gestion_de_Experimentos.Analizador_de_Informacion_Experimento(self,self._receta_id,1)
                print(f"Experimento\nNombre de la receta: {self._nombre}\nPersonas Responsables: {self._personas_responsables}\nFecha de Realizacion: {self._fecha}\nCosto: {self._costo_asociado}\nResulatdo: {self._resultado}\n----------------------")

            elif accion == 1:
                #Esta accion imprime la informacion de un expeerimento en especifico
                if indicador_de_experimento == self._id_experimento:
                    Gestion_de_Experimentos.Analizador_de_Informacion_Experimento(self,self._receta_id,1)
                    print(f"Experimento\nNombre de la receta: {self._nombre}\nPersonas Responsables: {self._personas_responsables}\nFecha de Realizacion: {self._fecha}\nCosto: {self._costo_asociado}\nResulatdo: {self._resultado}")
                    break

            elif accion == 2:
                #Esta accion auxilia al metodo Agregar Editar o Eliminar Experimentos
                #Se encarga de ayudar a editar un experimento
                if indicador_de_experimento == self._id_experimento:
                    Gestion_de_Experimentos.Configurar_Experimento(self)
                aux = {"id":self._id_experimento,"receta_id":self._receta_id,"personas_responsables":self._personas_responsables,"fecha":self._fecha ,"costo_asociado":self._costo_asociado ,"resultado":self._resultado}
               
                experimentos_copia.append(aux)
                
            elif accion == 3:
                #Esta accion auxilia al metodo Agregar Editar o Eliminar Experimentos
                #Se encarga de ayudar a eliminar un experimento
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
        #Este metodo se encarga de auxiliar a los modulos de Hacer experimento, tambien se encarga de imprimir la informacion de las recetas.
        #El parametro indicador de receta contiene el ID de una receta para ciertas acciones 
        #El parametro accion es el que indica cual es el meetodo que va a auxiliar
        for s in self._recetas:
            self._id_receta = s.get("id")
            self._nombre = s.get("nombre")
            self._objetivo = s.get("objetivo")
            self._reactivos_utilizados = s.get("reactivos_utilizados")
            self._procedimiento = s.get("procedimiento")
            self._valores_a_medir = s.get("valores_a_medir")
            
            if accion == 1:
                #Esta accion auxilia al modulo Hacer Experimento, haciendo que los atributos relacionados a recetas sean de la receta en especifico que se va a utilizar
                if self._id_receta == indicador_de_receta:
                    break
            
            elif accion == 2:
                #Esta accion imprime una receta en espeecifico
                if self._id_receta == indicador_de_receta:
                    print(f"Receta\nNombre de la receta: {self._nombre}\nObjetivo de la receta: {self._objetivo}\nReactivos utilizados y cantidades:{self._reactivos_utilizados}\nProcedimiento: {self._procedimiento}")
                    break

            elif accion == 3:
                #Esta accion imprime todas las recetas de la lista de recetas
                print(f"Nombre de la receta: {self._nombre}\nObjetivo de la receta: {self._objetivo}\nReactivos utilizados y cantidades:{self._reactivos_utilizados}\nProcedimiento: {self._procedimiento}\n-------------------")

    def Agregar_Editar_o_Eliminar_Experimento(self,accion):
        #Este modulo se encarga de hacer, editar o eliminar un experimento.
        #El parametro accion indica que accion se va a realizar
        if accion == 1:
            #Esta accion se encarga de crear un experimento 
            for s in self._experimentos:    
                self._id_experimento = max(s.get("id")) + 1
                break
            Gestion_de_Experimentos.Hacer_Experimento(self)
            aux = {"id":self._id_experimento,"receta_id":self._receta_id,"personas_responsables":self._personas_responsables,"fecha":self._fecha ,"costo_asociado":self._costo_asociado ,"resultado":self._resultado}
            self._experimentos.append(aux)
            Gestion_de_Experimentos.Configurar_json(self)

        elif accion == 2:
            #Esta accion se encarga de editar un experimento 
            self._id_experimento = int(input("Ingresa el ID del experimento que deseas editar: "))
            Gestion_de_Experimentos.Analizador_de_Informacion_Experimento(self,self._id_experimento,accion)
            Gestion_de_Experimentos.Configurar_json(self)
            return "se edito el experimento exitosamente."
        
        elif accion == 3:
            #Esta accion se encarga de eliminar un experimento 
            self._id_experimento = int(input("Ingresa el ID del experimento que deseas eliminar: "))
            Gestion_de_Experimentos.Analizador_de_Informacion_Experimento(self,self._id_experimento,accion)
            Gestion_de_Experimentos.Configurar_json(self)
            return "se edito el experimento exitosamente."
    
    def Configurar_Experimento(self):
        #Este metodo se encarga ded auxiliar a modulo Agregar Editar o Eliminar, especificamente a editar
        self._id_receta = int(input("Ingresa el ID de la receta que vas a utilizar: "))
        self._personas_responsables = []
        self._personas_responsables.append((input("Ingrese las personas responsables del proyecto: ").split(",")))
        self._fecha = input("Ingresa la fecha: ")
        self._costo_asociado = int(input("Ingresa el costo asociado: "))
        self._resultado = input("Ingresa el resultado: ")

    def Hacer_Experimento(self):
        #Aqui se realiza todo lo relacionado a la creacion del experimento
        #Se hace uso del metodo Experimento del modulo de Gestion de Reactivos
        maximo= []
        minimo = []
        margen_de_resultado = []
        x = []
        self._id_receta = int(input("Ingresa el ID de la receta que vas a utilizar: "))
        self._personas_responsables.append((input("Ingrese las personas responsables del proyecto: ").split(",")))
        self._fecha = input("Ingresa la fecha: ")
        Gestion_de_Experimentos.Analizador_de_Informacion_Recetas(self,self._id_receta,1)
        print(f"Receta: {self._nombre}")
        print(f"Objetivo: {self._objetivo}")
        print(f"Reactivos utilizados: {self._reactivos_utilizados}")
        print(f"Procedimiento: {self._procedimiento}")
        print(f"Valores a medir: {self._valores_a_medir}")
        margen_de_error = random.randint(0.1,22.5)
        costo = Gestion_de_Reactivos.Experimento(self,self._reactivos_utilizados)
        self._costo_asociado = sum(costo)
        
        
        for s in self._valores_a_medir:
            minimo.append(s.get("minimo"))
            maximo.append(s.get("maximo"))

        margen_de_error =random.uniform(0.1,22.5)    
        formula_de_resultado = random.choice(1,2)
        aux = 0 
        for aux in range(len(self._valores_a_medir)):
            if formula_de_resultado == 1:
                margen_de_resultado.append((minimo[aux]+ ((maximo[aux]* margen_de_error)/100)))
            else:    
                margen_de_resultado.append((maximo[aux] - (( maximo[aux]* margen_de_error)/100)))
            
            
        if minimo <= margen_de_resultado or margen_de_resultado <= maximo:
            fallo= False
            resultado = "Dentro del rango esperado"
        else:
            fallo = True
            if minimo > margen_de_resultado:
                resultado = "El resultado fue menor al minimo esperado"
            else:
                resultado = "El resultado fue mayor al maximo esperado"

        if fallo == True:
            self._costo_asociado =+ margen_de_error
        aux = 0 
        for aux in range(len(self._valores_a_medir)):
            x.append({self._valores_a_medir.get('nombre'): {margen_de_resultado}})
        for aux in x:
            valores_x = ', '.join([f"{list(aux.keys())[0]}: {list(aux.values())[0]}" ])
        self._resultado = f"{valores_x}: {margen_de_resultado}. {resultado}"
    
    def Configurar_json(self):
        #Este metodo actualiza la base de datos del inventario con cada accion que cambie algun detalle de algun experimento.
        archivo = open("Experimentos.json","w", encoding = "utf-8")
        for s in self._experimentos:
            aux = json.dumps(s)
            archivo.write(f"{aux}\n")
            archivo.close()
            archivo = open("Experimentos.json","a", encoding = "utf-8")
        archivo.close()