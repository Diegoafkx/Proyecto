import json

class Indicadores_de_Gestion:
    def __init__(self):
        self.__experimentos = []
        self.__recetas = []
        self.__reactivos = []
        Indicadores_de_Gestion.Obtener_informacion(self)

    def Obtener_informacion(self):
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

        experimento = {}
        for receta in self.__recetas:    
            for experimento in self.__experimentos:

                if (receta.get("id")) == experimento.get("receta_id"):
                    if experimento.get("personas_responsables") == experimento.get(receta.get("nombre")):
                        experimento[receta.get("nombre")] += 1

                    else:
                        experimento[receta.get("nombre")] = 1
                
        experimento_mas_hecho = (max(experimento,key= experimento.get))
        cantidad = (max( experimento.values()))
        experimento_menos_hecho = (min(experimento,key= experimento.get))
        cantidad = (min( experimento.values()))
        
        return(f"El experimento mas realizado es: {experimento_mas_hecho}\nHan sido {cantidad} veces la cantidad que sea a repetido el experimento\nEl experimento menos realzaido es: {experimento_menos_hecho}\nHan sido {cantidad} veces la cantidad que sea a repetido el experimento.")
    
    def Reactivo_con_Mas_Alta_Rotacion(self):
        x = [{"id":1,"nombre":"Waza","rotacion":1},{"id":2,"nombre":"skibidi","rotacion":2},{"id":23,"nombre":"sdkibidi","rotacion":21},{"id":12,"nombre":"sk3ibidi","rotacion":12},{"id":21,"nombre":"skibiddi","rotacion":28},{"id":8,"nombre":"skibi7di","rotacion":82},{"id":9,"nombre":"skib0idi","rotacion":2},{"id":0,"nombre":"skibid0i","rotacion":2}]
        reactivo_rotaciones = {}
        reactivos_con_mayor_rotacion = []
        for s in x:
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
            print("No se a tenido que rotar ningun reactivo.")

    def Veces_que_Falto_un_Reactivo(self):
        reactivo_rotaciones = {}
        reactivos_con_mayor_rotacion = []

        for s in self.__reactivos:
            reactivo_rotaciones[s.get("nombre")] = s.get("veces_que_falto")

        aux = list(reactivo_rotaciones.values())
        aux = sorted(aux, reverse= True)
        counter = 1

        for i in aux:
            for s in reactivo_rotaciones:
                if reactivo_rotaciones.get(s) != 0:
                    if i == reactivo_rotaciones.get(s):
                        reactivos_con_mayor_rotacion.append([s,reactivo_rotaciones[s]])
                        break
                else:
                    break        

        if reactivos_con_mayor_rotacion != []:
            print("Las veces que faltaron un reactivo")
            for s in range(len(reactivos_con_mayor_rotacion)):
                print(f"No se pudo hacer un experimento porque falta en inventario del reactivo {(reactivos_con_mayor_rotacion[s])[0]}, {(reactivos_con_mayor_rotacion[s])[1]} veces.")

        else:
            print("No a ocurrido que un experimento no se haya podido realizar por falta de reactivo.")
