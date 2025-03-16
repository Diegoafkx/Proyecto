import json
import re
class Gestion_de_Resultados:
    def __init__(self):
        self.__experimentos = []
        self.__recetas = []
        self.__resultados = []
        Gestion_de_Resultados.Obtener_informacion(self)

    def Obtener_informacion(self):
        #Este metodo se encarga de leer todos los datos del los archivos json.
        archivo = open("Recetas.json","r", encoding = "utf-8")
        informacion_del_archivo = archivo.readlines()
        for s in informacion_del_archivo:
            s = json.loads(s)
            self.__recetas.append(s)
        archivo.close()
        archivo = open("Experimentos.json","r", encoding = "utf-8")
        informacion_del_archivo = archivo.readlines()
        for s in informacion_del_archivo:
            s = json.loads(s)
            self.__experimentos.append(s)
        archivo.close()
    
    def Dar_Resultados(self,):
        #Este metodo va analizar todos los experimentos y imprimira cada uno diciendo si esta o no dentro de los parametros.
        def Verificador(minimo,maximo,resultado):
            for s in range(len(resultado)):
                aux = resultado[s]
                if aux.isnumeric() == True:
                    aux = int(aux)
                else:
                    aux = float(aux)
                if aux < minimo[s] or aux > maximo[s]:
                    return "El Experimento no esta dentro de los parametros."
                else:
                    return "El Experimento si se encuentra dentro de los parametros"
        
        for bucle in range(len(self.__experimentos)):
            minimo = []
            maximo= []
            self.__id_experimento = self.__experimentos[bucle].get("id")
            self.__receta_id = self.__experimentos[bucle].get("receta_id")
            self.__resultado = self.__experimentos[bucle].get("resultado")

            for s in self.__recetas:
                self.__id_receta = s.get("id")
                if self.__id_receta == self.__receta_id:
                    self.__valores_a_medir = s.get("valores_a_medir")
                    break
                else:
                    pass
            
            self.__resultado= self.__resultado.replace(" ","")
            aux = []

            for parte in self.__resultado.split(".")[0].split(","):
                if ":" in parte or "=" in parte:
                    if ":" in parte:
                        aux.append((parte.split(":"))[1])
                    elif "=" in parte:
                        aux.append((parte.split("="))[1])
                    for mezcla in aux:
                        aux = re.findall(r'\d+', mezcla)
                    
                else:
                    aux = False

            if aux != False:
                self.__resultado = aux
                for s in self.__valores_a_medir:
                    minimo.append(s.get("minimo"))
                    maximo.append(s.get("maximo"))

                for s in range(len(self.__resultado)):
                    self.__resultados.append([self.__id_experimento,Verificador(minimo,maximo,self.__resultado)])
            else:
                self.__resultados.append([self.__id_experimento, self.__resultado.split(".")[0]])
        print("---RESULTADOS---")
        for s in self.__resultados:
            print(f"ID del experimento: {s[0]}, Resultado: {s[1]}\n-------------\n")

            