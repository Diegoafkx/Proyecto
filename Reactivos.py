from Lector_de_APIS import _Lector_de_APIS 
import json

class __Reactivos:
    def __init__(self):
        self._id_reactivo = None
        self._nombre = None
        self._descripcion = None
        self._costo = None
        self._categoria = None
        self._inventario_disponible = None
        self._unidad_de_medicion = None
        self._fecha_de_caducidad = None
        self._minimo_sugerido = None
        self._conversiones_posibles = None
        self._reactivo = []

    def Lector_de_Datos(self):
        api = _Lector_de_APIS("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/refs/heads/main/reactivos.json", 2)
        api.Hacer_Request()
        archivo = open("Reactivos.json","r", encoding = "utf-8")
        informacion_del_archivo = archivo.readlines()
        for s in informacion_del_archivo:
            s = json.loads(s)
            self._reactivo.append(s)
        archivo.close()

