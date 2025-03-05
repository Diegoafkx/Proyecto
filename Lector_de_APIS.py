import requests
import json

#Esta clase se encarga de leer las APIS y guardarlas en un archivo JSON, dependiendo del inidicador del que se trate
#Si el indicador es 1, se leera la API que contiene las recetas y las pondria en un archivo JSON llamado Recetas.json
#Si el indicador es 2, se leera la API que contiene los reactivos y las pondria en un archivo JSON llamado Reactivos.json
#Si el indicador es 3, se leera la API que contiene los experimentos y las pondria en un archivo JSON llamado Experimentos.json

class _Lector_de_APIS:
    def __init__(self, url,indicador):
        self.indicador = indicador
        self.url = url

    def Hacer_Request(self):
        aux = requests.get(self.url)
        if aux.status_code == 200:
         self.url = aux.json()
        
        if self.indicador == 1:
            archivo = open("Recetas.json","a", encoding = "utf-8")
        
        elif self.indicador == 2:
            archivo = open("Reactivos.json","a", encoding = "utf-8")
        
        elif self.indicador == 3:
            archivo = open("Experimentos.json","a", encoding = "utf-8")

        for s in self.url:
            archivo.write(f"{json.dumps(s)}\n")
        archivo.close() 
           
