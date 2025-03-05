from Lector_de_APIS import _Lector_de_APIS 
import json

#Este modulo se encarga de activar el modulo de Lector_de_APIS, enviando el url y el indicador correspondiente.
#Luego lee el archivo JSON que se genero y guarda la informacion en una lista que le heredara a la clase Gestion_de_Experimentos.

class __Receta:
    def __init__(self):
        self._id_receta = None
        self._nombre = None
        self._objetivo = None
        self._reactivos_utilizados = []
        self._procedimiento = []
        self._valores_a_medir = []
        self._receta = []

    def Lector_de_Datos(self):
        api = _Lector_de_APIS("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/refs/heads/main/recetas.json", 1)
        api.Hacer_Request()
        archivo = open("Recetas.json","r", encoding = "utf-8")
        informacion_del_archivo = archivo.readlines()
        for s in informacion_del_archivo:
            s = json.loads(s)
            self._receta.append(s)
        archivo.close()
