from Gestion_de_Experimentos import *
from Gestion_de_Reactivos import *
from Gestion_de_Resultados import *
from Indicadores_de_Gestion import *

class laboratorio:
    def __init__(self):
        self.__experimentos = Gestion_de_Experimentos()
        self.__reactivos = Gestion_de_Reactivos()
        self.__resultados = Gestion_de_Resultados()
        self.__indicador = Indicadores_de_Gestion()

    def Main(self):
        fecha = input("Bienvenido al 'Laboratorio de Quimica Unimet', porfavor ingrese la fecha de hoy\n----->")
        print("-----MENU-----")
        opcion = input("1. Ver los reactivos (Aqui podras ver todo lo relacionado a los reactivos)\n2. Ver experimentos (Aqui podras ver todo lo relacionado a los experimentos)\n3. Ver resultados (Aqui podras observar si los resultados estan dentro de los parametros)\n4. Ver estadistas (Aqui veras todo lo relacionado a estadisticas del laboratorio)\n-------->")
           
        while True:
            if opcion == "1":
                print("Reactivos")
                break
            elif opcion == "2":
                print("Experimento")
                break
            elif opcion == "3":
                print("Resultados")
                break
            elif opcion == "4":
                print("Estadisticas")
                break
            else:
                opcion = input(f"ERROR\n{opcion} no es una opciona valida\nPorfavor intentelo otra vez\n-------->")


lab =laboratorio()
lab.Main()