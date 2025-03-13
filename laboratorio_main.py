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
        while True:
            print("-----MENU-----")
            opcion = input("1. Ver los reactivos (Aqui podras ver todo lo relacionado a los reactivos)\n2. Ver experimentos (Aqui podras ver todo lo relacionado a los experimentos)\n3. Ver resultados (Aqui podras observar si los resultados estan dentro de los parametros)\n4. Ver estadistas (Aqui veras todo lo relacionado a estadisticas del laboratorio)\n-------->")
            
            while True:
                if opcion == "1":
                    laboratorio.Reacts(self)
                    break
                elif opcion == "2":
                    laboratorio.Experiments(self)
                    break
                elif opcion == "3":
                    laboratorio.Results(self)
                    break
                elif opcion == "4":
                    laboratorio.Estadistics(self)
                    break
                else:
                    opcion = input(f"ERROR\n{opcion} no es una opciona valida\nPorfavor intentelo otra vez\n-------->")
    
    def Reacts(self):
        opcion = input(f"-----REACTIVOS-----\n----opciones----\n1. Ver un reactivo en especifico\n2. Ver todos los reactivos\n3. Agregar reactivo\n4. Editar informacion de un reactivo\n5. Eliminar un rectivo de la base de datos\n6. Cambiar unidades de un reactivo en especifico\n------>")
        if opcion  == "1":
            reactivo = int(input("Ingresa el ID del reactivo que deseas ver\n------>"))
            print(self.__reactivos.Analizador_de_Informacion_Reactivo(reactivo,-1))
        elif opcion == "2":
            print("REACTIVOS:")
            self.__reactivos.Analizador_de_Informacion_Reactivo(0,0)
        elif opcion == "3":
            opcion = input(f"------opciones----\n1. Agregar un nuevo reactivo\n2. Restablecer un reactivo existente\n------------->")
            if opcion == "1":
                print(self.__experimentos.Agregar_Editar_o_Eliminar_Experimento(1,0))
            elif opcion == "2":
                reactivo = int(input("Ingresa el ID del reactivo que deseas reabastecer\n------>"))
                print(self.__experimentos.Agregar_Editar_o_Eliminar_Experimento(1,reactivo))
        elif opcion == "4":
            reactivo = int(input("Ingresa el ID del reactivo que deseas editar\n------>"))
            print(self.__experimentos.Agregar_Editar_o_Eliminar_Experimento(2,reactivo))
        elif opcion == "5":
            reactivo = int(input("Ingresa el ID del reactivo que deseas eliminar\n------>"))
            print(self.__experimentos.Agregar_Editar_o_Eliminar_Experimento(3,reactivo))
        elif opcion == "6":
            reactivo = int(input("Ingresa el ID del reactivo que deseas cambiar las unidades de medicion\n------>"))
            print(self.__reactivos.Cambiar_la_UnidadMedida(reactivo))
            
    def Experiments(self):
        opcion = input(f"-----EXPERIMENTOS-----\n----opciones----\n1. Ver un experimento en especifico\n2. Ver todos los experimnetos\n3. Ver una recetas en especifico\n4. Ver todas las recetas\n5. Hacer un experimento\n6. Editar informacion de un experimento\n7. Eliminar un experimento de la base de datos\n------>")

    def Results(self):
        opcion = input(f"-----RESULTADOS-----\nA continuacion se veran si los resultados de los experimentos ubicados en la base de datos esta dentro o fuera de los parametros.")

    def Estadistics(self):
        opcion = input("-----ESTADISTICAS-----\n----opciones----\n1. Ver los investigadores que mas utilizan el laboratorio\n2. Ver el experimento mayor y menor hecho\n3. Ver los 5 reactivos con mayor rotacion (veces que se reabastecio el reactivo)\n4. Ver los 3 reactivos con mayor perdida\n5. Ver los reactivos que mas se vecen\n6. Ver cuantas veces no se pudo hacer un experimento por falta de reactivos\n7. Ver grafica con todas las estadisticas\n------>")

lab =laboratorio()
lab.Main()