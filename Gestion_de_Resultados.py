import json

class Gestion_de_Resultados:
    def __init__(self):
        self.__experimentos = []
        self.__recetas = []
        self.__resultados = []
        Gestion_de_Resultados.Obtener_informacion(self)

    def Obtener_informacion(self):
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
    
    def Dar_Resultados(self,indicador_de_experimento):
        def Verificador(minimo,maximo,resultado):
            for s in range(len(resultado)):
                if resultado[s] < minimo or resultado > maximo:
                    return "El Experimento no esta dentro de los parametros."
                else:
                    return "El Experimento si se encuentra dentro de los parametros"

        for bucle in range(len(self.__experimentos)):
            minimo = []
            maximo= []
            for s in self.__experimentos:
                self.__id_experimento = s.get("id")
                if self.__id_experimento == indicador_de_experimento:
                    self.__receta_id = s.get("receta_id")
                    self.__resultado = s.get("resultado")

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
                aux.append((parte.split(":"))[1])
            self.__resultado = aux
            for s in self.__valores_a_medir:
                minimo.append(s.get("minimo"))
                maximo.append(s.get("maximo"))

            for s in range(len(self.__resultado)):
                if str(self.__resultado[s]).isnumeric() == False:
                    pass
                else:
                    self.__resultados.append([self.__id_experimento,Verificador(minimo,maximo,self.__resultado)])
        print("---RESULTADOS---")
        for s in self.__resultados:
            print(f"ID del experimento: {s[0]}, Resultado: {s[1]}")

            