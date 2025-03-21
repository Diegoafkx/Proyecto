from Gestion_de_Experimentos import *
from Gestion_de_Reactivos import *
from Gestion_de_Resultados import *
from Indicadores_de_Gestion import *

class Laboratorio:
    def __init__(self):
        self.__experimentos = Gestion_de_Experimentos()
        self.__reactivos = Gestion_de_Reactivos(1)
        self.__resultados = Gestion_de_Resultados()
        self.__indicador = None

    def Main(self):
        #Este metodo es el main de la aplicacion 
        while True:
            fecha = input("Bienvenido al 'Laboratorio de Quimica Unimet', porfavor ingrese la fecha de hoy (Año-mes-dia)\n----->")
            self.__reactivos.Vencimiento_de_Reactivo(fecha)
            while True:
                print("-----MENU-----")
                self.__reactivos.Estatus_de_los_Reactivos()
                while True:
                    opcion = input("----MENU-----\n1. Ver los reactivos (Aqui podras ver todo lo relacionado a los reactivos)\n2. Ver experimentos (Aqui podras ver todo lo relacionado a los experimentos)\n3. Ver resultados (Aqui podras observar si los resultados estan dentro de los parametros)\n4. Ver estadistas (Aqui veras todo lo relacionado a estadisticas del laboratorio)\n5. Salir\n-------->")
                    if opcion == "1":
                        laboratorio.Reacts(self)
                        
                    elif opcion == "2":
                        laboratorio.Experiments(self)
                        
                    elif opcion == "3":
                        laboratorio.Results(self)
                        
                    elif opcion == "4":
                        laboratorio.Estadistics(self)
                        
                    elif opcion == "5":
                        print("Hasta luego")
                        break
                        
                    else:
                        print(f"ERROR\n{opcion} no es una opciona valida\nPorfavor intentelo otra vez\n-------->")
    
    def Reacts(self):
        #Este metodo se encarga ded todo lo relacionado a los reactivos
        while True:
            opcion = input(f"-----REACTIVOS-----\n----opciones----\n1. Ver un reactivo en especifico\n2. Ver todos los reactivos\n3. Agregar reactivo\n4. Editar informacion de un reactivo\n5. Eliminar un rectivo de la base de datos\n6. Cambiar unidades de un reactivo en especifico\n7. Regresar\n------>")
            if opcion  == "1":
                reactivo = int(input("Ingresa el ID del reactivo que deseas ver\n------>"))
                print(self.__reactivos.Analizador_de_Informacion_Reactivo(reactivo,-1))
            elif opcion == "2":
                print("REACTIVOS:")
                self.__reactivos.Analizador_de_Informacion_Reactivo(0,0)
            elif opcion == "3":
                opcion = input(f"------opciones----\n1. Agregar un nuevo reactivo\n2. Restablecer un reactivo existente\n------------->")
                if opcion == "1":
                    print(self.__reactivos.Agregar_Editar_o_Eliminar_Reactivo(1,0))
                elif opcion == "2":
                    reactivo = int(input("Ingresa el ID del reactivo que deseas reabastecer\n------>"))
                    print(self.__reactivos.Agregar_Editar_o_Eliminar_Reactivo(1,reactivo))
            elif opcion == "4":
                reactivo = int(input("Ingresa el ID del reactivo que deseas editar\n------>"))
                print(self.__reactivos.Agregar_Editar_o_Eliminar_Reactivo(2,reactivo))
            elif opcion == "5":
                reactivo = int(input("Ingresa el ID del reactivo que deseas eliminar\n------>"))
                print(self.__reactivos.Agregar_Editar_o_Eliminar_Reactivo(3,reactivo))
            elif opcion == "6":
                reactivo = int(input("Ingresa el ID del reactivo que deseas cambiar las unidades de medicion\n------>"))
                print(self.__reactivos.Cambiar_la_UnidadMedida(reactivo))
            elif opcion == "7":
                break
            else:
                print(f"ERROR\n{opcion} no es una opciona valida\nPorfavor intentelo otra vez\n-------->")

    def Experiments(self):
        #Este metodo se encarga ded todo lo relacionado a los experimento
        while True:
            opcion = input(f"-----EXPERIMENTOS-----\n----opciones----\n1. Ver un experimento en especifico\n2. Ver todos los experimentos\n3. Ver una recetas en especifico\n4. Ver todas las recetas\n5. Hacer un experimento\n6. Editar informacion de un experimento\n7. Eliminar un experimento de la base de datos\n8. Regresar\n------>")
            if opcion == "1":
                experimento = int(input("Ingrese el ID del experimento que desea ver: "))
                self.__experimentos.Analizador_de_Informacion_Experimento(experimento,1)
            elif opcion == "2":
                self.__experimentos.Analizador_de_Informacion_Experimento(None,2)
            elif opcion == "3":
                receta = int(input("Ingrese el ID del receta que desea ver: "))
                self.__experimentos.Analizador_de_Informacion_Recetas(receta,2)
            elif opcion == "4":
                self.__experimentos.Analizador_de_Informacion_Recetas(None,3)
            elif opcion == "5":
                self.__experimentos.Agregar_Editar_o_Eliminar_Experimento(1)
            elif opcion == "6":
                self.__experimentos.Agregar_Editar_o_Eliminar_Experimento(2)
            elif opcion == "7":
                self.__experimentos.Agregar_Editar_o_Eliminar_Experimento(3)
            elif opcion == "8":
                break
            else:
                print(f"ERROR\n{opcion} no es una opciona valida\nPorfavor intentelo otra vez")

    def Results(self):
        #Este metodo se encarga ded todo lo relacionado a los resultados
        print(f"-----RESULTADOS-----\nA continuacion se veran si los resultados de los experimentos ubicados en la base de datos esta dentro o fuera de los parametros.")
        self.__resultados.Dar_Resultados()

    def Estadistics(self):
        #Este metodo se encarga ded todo lo relacionado a las estadisticas
        self.__indicador = Indicadores_de_Gestion()
        while True:
            opcion = input("-----ESTADISTICAS-----\n----opciones----\n1. Ver los investigadores que mas utilizan el laboratorio\n2. Ver el experimento mayor y menor hecho\n3. Ver los 5 reactivos con mayor rotacion (veces que se reabastecio el reactivo)\n4. Ver los 3 reactivos con mayor perdida\n5. Ver los reactivos que mas se vecen\n6. Ver cuantas veces no se pudo hacer un experimento por falta de reactivos\n7. Regresar\n------>")
            if opcion == "1":
                print(self.__indicador.Investigador_que_Utiliza_Mas_el_Lab())
            elif opcion == "2":
                print(self.__indicador.Experimento_Mas_y_Menos_Hecho())
            elif opcion == "3":
                self.__indicador.Reactivo_con_Mas_Alta_Rotacion()
            elif opcion == "4":
                self.__indicador.Mayor_Perdida()
            elif opcion == "5":
                self.__indicador.Mas_se_Vencen()
            elif opcion == "6":
                self.__indicador.Veces_que_Falto_un_Reactivo()
            elif opcion == "7":
                break
            else:
                print(f"ERROR\n{opcion} no es una opciona valida\nPorfavor intentelo otra vez")

lab =Laboratorio()
lab.Main()