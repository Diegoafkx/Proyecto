import json

class Indicadores_de_Gestion:
    def __init__(self):
        self.__experimentos = []
        self.__recetas = []
        self.__reactivos = []
        Indicadores_de_Gestion.Obtener_informacion(self)

    def Obtener_informacion(self):
        #Este metodo se encarga de leer todos los datos de la base de datos y meterlos en listas especificas
        archivo = open("Recetas.json","r", encoding = "utf-8")
        informacion_del_archivo = archivo.readlines()
        for s in informacion_del_archivo:
            s = json.loads(s)
            self.__recetas.append(s)
        archivo.close()
        archivo = open("Experimentos.json","r", encoding = "utf-8")
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
        #Este metodo buscara y imprimira los Investigadores que mas han hecho uso del laboratorio
        personas = {}
        for s in self.__experimentos:
            for persona in s.get("personas_responsables"):
                if persona in personas:
                    personas[persona] += 1

                else:
                    personas[persona] = 1

        persona_que_mas_utilizo = (max(personas,key= personas.get))
        cantidad = (max( personas.values()))
        return(f"La persona que mas a utilizado los laboratorios es {persona_que_mas_utilizo} al ahber hecho uso del laboratorio {cantidad} veces.")

    def Experimento_Mas_y_Menos_Hecho(self):
        #Este metodo se encarga de buscar y imprimir los experimentos mas y menos realizados
        experimento1 = {}
        for receta in self.__recetas:    
            for experimento in self.__experimentos:

                if (receta.get("id")) == experimento.get("receta_id"):
                    if receta.get("nombre") in experimento1:
                        experimento1[receta.get("nombre")] += 1
                        break

                    else:
                        experimento1[receta.get("nombre")] = 1
                
        experimento_mas_hecho = (max(experimento1,key= experimento1.get))
        cantidad_mas_hecho = (max( experimento1.values()))
        experimento_menos_hecho = (min(experimento1,key= experimento1.get))
        cantidad_menos_hecho = (min( experimento1.values()))
        
        return(f"El experimento mas realizado es: {experimento_mas_hecho}\nHan sido {cantidad_mas_hecho} veces la cantidad que sea a repetido el experimento\nEl experimento menos realzaido es: {experimento_menos_hecho}\nHan sido {cantidad_menos_hecho} veces la cantidad que sea a repetido el experimento.")
    
    def Reactivo_con_Mas_Alta_Rotacion(self):
        #Este metodo se encarga de buscar y imprimir los 5 reactivos con mas alta rotacion
        
        reactivo_rotaciones = {}
        reactivos_con_mayor_rotacion = []
        for s in self.__reactivos:
            reactivo_rotaciones[s.get("nombre")] = s.get("rotacion")
        aux = list(reactivo_rotaciones.values())
        aux = sorted(aux, reverse= True)
        counter = 1
        for i in aux:
            for s in reactivo_rotaciones:
                if reactivo_rotaciones.get(s) != 0:
                    if i == reactivo_rotaciones.get(s):
                        reactivos_con_mayor_rotacion.append([s,reactivo_rotaciones[s]])
                        counter += 1
                        break
                
                else:
                    pass
            if counter > 5:
                break
        if reactivos_con_mayor_rotacion != []:
            print("Los 5 reactivos con mayor rotacion son:")
            for s in range(len(reactivos_con_mayor_rotacion)):
                print(f"{s+1}.{(reactivos_con_mayor_rotacion[s])[0]} se a rotado {(reactivos_con_mayor_rotacion[s])[1]}")
        else:
            print("No se a rotado ningun reactivo aun.")

    def Veces_que_Falto_un_Reactivo(self):
        #Este metodo se encarga de imprimir todas las veces que un eexperimento no se pudo realizar por falta de reactivo, con el nombre del reactivo y cuantas veces fuero.
        contador = 0 
        for s in self.__reactivos:
            if s.get("veces_que_falto") > 0:
                print(f"En {s.get("veces_que_falto")} experimentos el reactivo: {s.get("nombre")} hizo falta ")
            else:
                contador+= 1
        if contador == len(self.__reactivos):
            print("Aun no se a llegado a no poder realizar un experimento porr falta de reactivo.")

    def Mayor_Perdida(self):
        #Este metodo se encarga de imprimir los 3 reactivos que mas se han perdido cuadno un experimento fracasa.
        reactivo_desperdicio = {}
        reactivos_con_mayor_desperdicio = []
        for s in self.__reactivos:
            reactivo_desperdicio[s.get("nombre")] = s.get("veces_que_se_desperdicio")
        aux = list(reactivo_desperdicio.values())
        aux = sorted(aux, reverse= True)
        counter = 1
        for i in aux:
            for s in reactivo_desperdicio:
                if reactivo_desperdicio.get(s) != 0:
                    if i == reactivo_desperdicio.get(s):
                        reactivos_con_mayor_desperdicio.append([s,reactivo_desperdicio[s]])
                        counter += 1
                        break
                
                else:
                    pass
            if counter > 3:
                break
        if reactivos_con_mayor_desperdicio != []:
            print("Los 3 reactivos con mayor desperdicio son:")
            for s in range(len(reactivos_con_mayor_desperdicio)):
                print(f"{s+1}.{(reactivos_con_mayor_desperdicio[s])[0]} se a desperdiciado {(reactivos_con_mayor_desperdicio[s])[1]} veces.")
        else:
            print("No se a desperdiciado ningun reactivo aun.")

    def Mas_se_Vencen(self):
        #Este metodo se encarga de imprimir los 3 experimentos que mas se han caducado. 
        reactivo_caduco = {}
        reactivos_con_mayor_caducacion = []
        for s in self.__reactivos:
            reactivo_caduco[s.get("nombre")] = s.get("veces_que_caduco")
        aux = list(reactivo_caduco.values())
        aux = sorted(aux, reverse= True)
        counter = 1
        for i in aux:
            for s in reactivo_caduco:
                if reactivo_caduco.get(s) != 0:
                    if i == reactivo_caduco.get(s):
                        reactivos_con_mayor_caducacion.append([s,reactivo_caduco[s]])
                        counter += 1
                        break
                
                else:
                    pass
            if counter > 3:
                break
        if reactivos_con_mayor_caducacion != []:
            print("Los 3 reactivos con mayor caducacion son:")
            for s in range(len(reactivos_con_mayor_caducacion)):
                print(f"{s+1}.{(reactivos_con_mayor_caducacion[s])[0]} se a caducado {(reactivos_con_mayor_caducacion[s])[1]} veces.")
        else:
            print("No se a caducado ningun reactivo aun.")