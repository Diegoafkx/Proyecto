from Reactivos import __Reactivos
import json
class Gestion_de_Reactivos(__Reactivos):
    def __init__(self):
        super().__init__()
        Gestion_de_Reactivos.Lector_de_Datos(self)

    def Analizador_de_Informacion_Reactivo(self,indicador_del_reactivo,accion):
        conversiones = []
        ya_paso = True
        fist_time = True
        reactivo_copia = []
        advertensia = []
        self.advise = False
        for s in self._reactivo:
            self._id_reactivo = s.get("id")
            self._nombre = s.get("nombre")
            self._descripcion = s.get("descripcion")
            self._costo = s.get("costo")
            self._categoria = s.get("categoria")
            self._inventario_disponible = s.get("inventario_disponible")
            self._unidad_de_medicion = s.get("unidad_medida")
            self._fecha_de_caducidad = s.get("fecha_caducidad")
            self._minimo_sugerido = s.get("minimo_sugerido")
            self._conversiones_posibles = s.get("conversiones_posibles")
            
            if accion == 1:
                if self._id_reactivo == indicador_del_reactivo:
                    return s    
            
            elif accion == 2:
                    
                if indicador_del_reactivo == self._id_reactivo:
                    Gestion_de_Reactivos.Configurar_Reactivo(self)
                aux = {"id":self._id_reactivo,"nombre": self._nombre, "descripcion": self._descripcion, "costo": self._costo, "categoria": self._categoria, "inventario_disponible": self._inventario_disponible, "unidad_medida": self._unidad_de_medicion, "fecha_caducidad": self._fecha_de_caducidad, "minimo_sugerido": self._minimo_sugerido, "conversiones_posibles" :self._conversiones_posibles }
                reactivo_copia.append(aux)
                aux = json.dumps(aux)
                if fist_time == True:
                    archivo = open("Reactivos.json","w", encoding = "utf-8")
                    archivo.write(f"{aux}\n")
                    fist_time = False
                else:
                    archivo = open("Reactivos.json","a", encoding = "utf-8")
                    archivo.write(f"{aux}\n")

            elif accion == 3:
                if indicador_del_reactivo == self._id_reactivo:
                    ya_paso = False
                elif indicador_del_reactivo != self._id_reactivo and ya_paso == True:
                    aux = {"id":self._id_reactivo,"nombre": self._nombre, "descripcion": self._descripcion, "costo": self._costo, "categoria": self._categoria, "inventario_disponible": self._inventario_disponible, "unidad_medida": self._unidad_de_medicion, "fecha_caducidad": self._fecha_de_caducidad, "minimo_sugerido": self._minimo_sugerido, "conversiones_posibles" :self._conversiones_posibles }
                    reactivo_copia.append(aux)
                    aux = json.dumps(aux)
                    if fist_time == True:
                        archivo = open("Reactivos.json","w", encoding = "utf-8")
                        archivo.write(f"{aux}\n")
                        fist_time = False
                    else:
                        archivo = open("Reactivos.json","a", encoding = "utf-8")
                        archivo.write(f"{aux}\n")
                elif indicador_del_reactivo != self._id_reactivo and ya_paso == False:
                    aux = {"id":self._id_reactivo - 1,"nombre": self._nombre, "descripcion": self._descripcion, "costo": self._costo, "categoria": self._categoria, "inventario_disponible": self._inventario_disponible, "unidad_medida": self._unidad_de_medicion, "fecha_caducidad": self._fecha_de_caducidad, "minimo_sugerido": self._minimo_sugerido, "conversiones_posibles" :self._conversiones_posibles }
                    reactivo_copia.append(aux)
                    aux = json.dumps(aux)
                    if fist_time == True:
                        archivo = open("Reactivos.json","w", encoding = "utf-8")
                        archivo.write(f"{aux}\n")
                        fist_time = False
                    else:
                        archivo = open("Reactivos.json","a", encoding = "utf-8")
                        archivo.write(f"{aux}\n")
                
            elif accion == 4:
                if self._inventario_disponible < self._minimo_sugerido:
                    advertensia.append([self._nombre,self._minimo_sugerido,self._inventario_disponible])
                    self.advise = True

            if accion == 5:

                if indicador_del_reactivo == self._id_reactivo:
                    if len(self._conversiones_posibles)+1 > 1:
                        mas_de_una_conversion = True
                        print("Estas son las conversiones posibles\n")
                        n = 1
                        for s in self._conversiones_posibles:
                            print(f"conversion: {n}")
                            print(f"Unidad: {s.get('unidad')}\nFactor: {s.get('factor')}\n-------------------")
                            n+=1

                        option = int(input("Escribe el numero de la conversion que deseas cambiar: ")) 
                        for s in range(len(self._conversiones_posibles)):
                            if s+1 == option:
                                conversion = self._conversiones_posibles[s]

                            else:
                                conversiones.append(self._conversiones_posibles[s])

                    else:
                        mas_de_una_conversion = False
                        conversion = self._conversiones_posibles
                    
                    
                    self._inventario_disponible = self._inventario_disponible * conversion.get("factor")
                    self._minimo_sugerido = self._minimo_sugerido * conversion.get("factor")
                    factor = 1/conversion.get("factor")
                    x = conversion.get("unidad")
                    unidad = self._unidad_de_medicion
                    self._unidad_de_medicion = x

                    if mas_de_una_conversion == True:
                        self._conversiones_posibles= conversiones
                        self._conversiones_posibles.append({"unidad": unidad, "factor": factor})
                    
                    

                aux = {"id":self._id_reactivo,"nombre": self._nombre, "descripcion": self._descripcion, "costo": self._costo, "categoria": self._categoria, "inventario_disponible": self._inventario_disponible, "unidad_medida": self._unidad_de_medicion, "fecha_caducidad": self._fecha_de_caducidad, "minimo_sugerido": self._minimo_sugerido, "conversiones_posibles" :self._conversiones_posibles }
                reactivo_copia.append(aux)
                aux = json.dumps(aux)
                if fist_time == True:
                    archivo = open("Reactivos.json","w", encoding = "utf-8")
                    archivo.write(f"{aux}\n")
                    fist_time = False
                else:
                    archivo = open("Reactivos.json","a", encoding = "utf-8")
                    archivo.write(f"{aux}\n")
                    

        if accion == 2 or accion == 3 or accion == 5:
            self._reactivo = []
            self._reactivo = reactivo_copia
            archivo.close()
        
        elif accion == 4:
            return advertensia
    
    def Agregar_Editar_o_Eliminar_Reactivo(self, indicador_del_reactivo, auxiliador):
        
        if auxiliador == 1:
            for s in self._reactivo:
                self._id_reactivo = max(s.get("id"))+1
                break
            self._id_reactivo = self._id_reactivo+ + 1
            Gestion_de_Reactivos.Configurar_Reactivo(self)
            archivo = open("Reactivos.json","a", encoding = "utf-8")
            aux = {"id":self._id_reactivo,"nombre": self._nombre, "descripcion": self._descripcion, "costo": self._costo, "categoria": self._categoria, "inventario_disponible": self._inventario_disponible, "unidad_medida": self._unidad_de_medicion, "fecha_caducidad": self._fecha_de_caducidad, "minimo_sugerido": self._minimo_sugerido, "conversiones_posibles" :self._conversiones_posibles }
            self._reactivo.append(aux)
            aux = json.dumps(aux)
            archivo.write(f"{aux}\n")
            archivo.close()
            return "se agrego el reactivo exitosamente."

        elif auxiliador == 2 or auxiliador == 3:
            if auxiliador == 2:
                self.reactivo_a_configurar = Gestion_de_Reactivos.Analizador_de_Informacion_Reactivo(self,indicador_del_reactivo,2)
                return "Se a editado el reactivo con exito"
            else:
                self.reactivo_a_configurar = Gestion_de_Reactivos.Analizador_de_Informacion_Reactivo(self,indicador_del_reactivo,3)
                return "Se a eliminado el reactivo con exito"

    def Estatus_de_los_Reactivos(self):
        advertensia = Gestion_de_Reactivos.Analizador_de_Informacion_Reactivo(self,0,False,4)
        if self.advise == True:
            print("-------ADVERTENCIA-----")
            for s in advertensia:
                print(f"No hay de la cantidad requerrida en el inventario del reactivo: {s[0]}\nCantidad minima sugerida: {s[1]}\nCantidad en el inventario: {s[2]}")
        
        else:
            print("Todo en orden")

    def Cambiar_la_UnidadMedida(self,indicador_del_reactivo):
        Gestion_de_Reactivos.Analizador_de_Informacion_Reactivo(self,indicador_del_reactivo, 5)
        for i in self._reactivo:
            if i.get("id") == indicador_del_reactivo:
                for s in i: 
                    print(f"{s}: {i.get(s)}")
                print("Se a cambiado la unidad de medicion con exito")
            break

    def Configurar_Reactivo(self):
        self._nombre = input("Escribe el nombre del reactivo: ")
        self._descripcion = input("Escribe la descripcion del reactivo: ")
        self._costo = float(input("Escribe el costo del reactivo: "))
        self._categoria = input("Escribe la categoria del reactivo: ")
        self._inventario_disponible = int(input("Escribe el inventario disponible: "))
        self._unidad_de_medicion = input("Escribe la unidad de medicion del reactivo: ")
        self._fecha_de_caducidad = input("Escribe la fecha de caducidad del reactivo: ")
        self._minimo_sugerido = int(input("Escribe la cantidad minima sugerrida del reactivo: "))
        self._conversiones_posibles = []
        while True:
            unidad = input("Escribe la unidad de conversion: ")
            factor = float(input("Escribe el factor: "))
            self._conversiones_posibles.append({"unidad": unidad, "factor": factor})

            option = input("Estos son todas las converrsiones posibles?\n(1-si/2-no)\n-------->?")
            if option == "1":
                break

hola = Gestion_de_Reactivos()
reactivos = hola.Analizador_de_Informacion_Reactivo(1,1)
print(reactivos)
for s in reactivos:
    print(f"{s}: {reactivos.get(s)}")
#agregar es la opcion 1, editar es la opcion 2 y eliminar la opcion 3
"print(hola.Agregar_Editar_o_Eliminar_Reactivo(1,1,3))"
"""print(hola.Agregar_Editar_o_Eliminar_Reactivo(1,2,2))
print(hola.Agregar_Editar_o_Eliminar_Reactivo(2,3,3))"""
"hola.Estatus_de_los_Reactivos()"
hola.Cambiar_la_UnidadMedida(1)
hola.Cambiar_la_UnidadMedida(1)
