import requests
import json

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
           

           
