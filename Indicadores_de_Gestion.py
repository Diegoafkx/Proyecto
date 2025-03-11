import json

class Indicadores_de_Gestion:
    def __init__(self):
        self.__experimentos = []
        self.__recetas = []
        self.__reactivos = []
        Indicadores_de_Gestion.Obtener_informacion(self)

    def Obtener_informacion(self):
        archivo = open("Recetas.json","r", encoding = "utf-8")
        informacion_del_archivo = archivo.readlines()
        for s in informacion_del_archivo:
            s = json.loads(s)
            self.__recetas.append(s)
        archivo.close()
        archivo = open("Experimento.json","r", encoding = "utf-8")
        informacion_del_archivo = archivo.readlines()
        for s in informacion_del_archivo:
            s = json.loads(s)
            self.__experimentos.append(s)
        archivo.close()
        archivo = open("Reactivos.json","r", encoding = "utf-8")
        informacion_del_archivo = archivo.readlines()
        for s in informacion_del_archivo:
            s = json.loads(s)
            self.__reactivos.append(s)
        archivo.close()

    def Investigador_que_Utiliza_Mas_el_Lab(self):
        pass