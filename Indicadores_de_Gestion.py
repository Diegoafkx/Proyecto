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
        archivo = open("Experimento.json","r", encoding = "utf-8")
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
        pass