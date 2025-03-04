from Lector_de_APIS import _Lector_de_APIS 
import json

class __Experimnto(_Lector_de_APIS):
    def __init__(self):
        self._id_experimento = None
        self._receta_id = None  
        self._personas_responsables = None
        self._fecha = None
        self._costo_asociado = None
        self._resultado = None
        self._experimento = []

    def Lector_de_Datos(self):
        api = _Lector_de_APIS("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/refs/heads/main/experimentos.json", 3)
        api.Hacer_Request()
        archivo = open("Experimentos.json","r", encoding = "utf-8")
        informacion_del_archivo = archivo.readlines()
        for s in informacion_del_archivo:
            s = json.loads(s)
            self._experimento.append(s)
        archivo.close()
