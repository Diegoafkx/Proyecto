from Lector_de_APIS import _Lector_de_APIS 
import json

#Este modulo se encarga de activar el modulo de Lector_de_APIS, enviando el url y el indicador correspondiente.
#Luego lee el archivo JSON que se genero y guarda la informacion en una lista que le heredara a la clase Gestion_de_Experimentos.

class __Experimnto:
    def __init__(self):
        self._id_experimento = None
        self._receta_id = None  
        self._personas_responsables = None
        self._fecha = None
        self._costo_asociado = None
        self._resultado = None
        self._experimentos = []

    def Lector_de_Datos(self):
        api = _Lector_de_APIS("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/refs/heads/main/experimentos.json", 3)
        api.Hacer_Request()
        archivo = open("Experimentos.json","r", encoding = "utf-8")
        informacion_del_archivo = archivo.readlines()
        for s in informacion_del_archivo:
            s = json.loads(s)
            self._experimento.append(s)
        archivo.close()
