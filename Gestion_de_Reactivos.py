from Reactivos import __Reactivos
import json

#Modulo que se encarga de gestionar los reactivos, agregar, editar, eliminar, cambiar la unidad de medicion y ver el estatus de los reactivos
#Heredo todos los atributos y metodos de la clase __Reactivos
#Arreglar codigo utilizar update, remove y en editar y eliminar
class Gestion_de_Reactivos(__Reactivos):
    def __init__(self):
        super().__init__()
        Gestion_de_Reactivos.Lector_de_Datos(self)

    def Analizador_de_Informacion_Reactivo(self,indicador_del_reactivo,accion):
        
        #Este metodo se encarga de asociar los datos de la API que guardamos en el archivo Reactivos.json con los atributos de la clase.
        #Este metodo tambien se encargan de auxiliar a los demas metodos de la clase.
        #El valor que recibe el parametro accion es el que determina cual es el metodo que esta auxiliando.

        conversiones = []
        reactivo_copia = []
        advertensia = []
        self.advise = False
        self.costo = []

        for s in self._reactivos:
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
            
            if accion == 0:
                #Esta accion se encarga de enviar los datos del reactivo que se desea ver.
                if self._id_reactivo == indicador_del_reactivo:
                    return s 

            elif accion == 1:
                if indicador_del_reactivo == self._id_reactivo:
                    print(f"La Cantidad disponible es: {self._inventario_disponible}")
                    self._inventario_disponible = self._inventario_disponible + int(input("Cuanta cantidad que desea sumarles: "))
                    print(f"La cantidad disponible ahora es: {self._inventario_disponible}")
                aux = {"id":self._id_reactivo,"nombre": self._nombre, "descripcion": self._descripcion, "costo": self._costo, "categoria": self._categoria, "inventario_disponible": self._inventario_disponible, "unidad_medida": self._unidad_de_medicion, "fecha_caducidad": self._fecha_de_caducidad, "minimo_sugerido": self._minimo_sugerido, "conversiones_posibles" :self._conversiones_posibles }
                reactivo_copia.append(aux)
            
            elif accion == 2:
                #esta auxilia al metodo Agregar_Editar_o_Eliminar_Reactivo.
                #Esta se encarga de editar un reactivo en especifico.
                if indicador_del_reactivo == self._id_reactivo:
                    Gestion_de_Reactivos.Configurar_Reactivo(self)
                aux = {"id":self._id_reactivo,"nombre": self._nombre, "descripcion": self._descripcion, "costo": self._costo, "categoria": self._categoria, "inventario_disponible": self._inventario_disponible, "unidad_medida": self._unidad_de_medicion, "fecha_caducidad": self._fecha_de_caducidad, "minimo_sugerido": self._minimo_sugerido, "conversiones_posibles" :self._conversiones_posibles }
                reactivo_copia.append(aux)

            elif accion == 3:
                #esta auxilia al metodo Agregar_Editar_o_Eliminar_Reactivo.
                #Esta se encarga de eliminar un reactivo en especifico.
                if indicador_del_reactivo == self._id_reactivo:
                    pass
                else:
                    if indicador_del_reactivo < self._id_reactivo:
                        aux = {"id":self._id_reactivo - 1,"nombre": self._nombre, "descripcion": self._descripcion, "costo": self._costo, "categoria": self._categoria, "inventario_disponible": self._inventario_disponible, "unidad_medida": self._unidad_de_medicion, "fecha_caducidad": self._fecha_de_caducidad, "minimo_sugerido": self._minimo_sugerido, "conversiones_posibles" :self._conversiones_posibles}
                    else:
                        aux = {"id":self._id_reactivo,"nombre": self._nombre, "descripcion": self._descripcion, "costo": self._costo, "categoria": self._categoria, "inventario_disponible": self._inventario_disponible, "unidad_medida": self._unidad_de_medicion, "fecha_caducidad": self._fecha_de_caducidad, "minimo_sugerido": self._minimo_sugerido, "conversiones_posibles" :self._conversiones_posibles}
                    reactivo_copia.append(aux)
                
            elif accion == 4:
                #Esta accion axulia al metodo Estatus_de_los_Reactivos, buscando que reactivos tienen menos de la cantidad minima sugerida.
                if self._inventario_disponible < self._minimo_sugerido:
                    advertensia.append([self._nombre,self._minimo_sugerido,self._inventario_disponible])
                    self.advise = True

            if accion == 5:
                #Esta accion auxilia al metodo Cambiar_la_UnidadMedida, se encarga de cambiar la unidad de medicion de un reactivo en especifico.
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

            if accion == 6:
                for s in indicador_del_reactivo:
                    if self._id_reactivo == s.get("reactivo_id"):
                        while True:
                            if self._unidad_de_medicion == s.get("unidad_medida"):
                                if self._inventario_disponible >= s.get("cantidad_necesaria"):
                                    self.costo.append(s.get("costo"))
                                    self._inventario_disponible = self._inventario_disponible - s.get("cantidad_necesaria")
                                    break
                                else:
                                    print(f"No hay suficiente cantidad en el inventario del reactivo {self._nombre} para realizar el experimento.\nCantidad necesaria: {s.get('cantidad_necesaria')}\nCantidad en el inventario: {self._inventario_disponible}\nPor favor agrega mas cantidad al inventario")
                                    Gestion_de_Reactivos.Agregar_Editar_o_Eliminar_Reactivo(self,2)
                            else:
                                print(f"Es necesario hacer cambios de unidades de medicion para poder realizar el experimento.\nLa unidad de medicion del reactivo {self._nombre} es {self._unidad_de_medicion} y la cantidad necesaria es {s.get("unidad_medida")}\nRealizando cambio de medición")
                                Gestion_de_Reactivos.Cambiar_la_UnidadMedida(self, self._id_reactivo)
                aux = {"id":self._id_reactivo,"nombre": self._nombre, "descripcion": self._descripcion, "costo": self._costo, "categoria": self._categoria, "inventario_disponible": self._inventario_disponible, "unidad_medida": self._unidad_de_medicion, "fecha_caducidad": self._fecha_de_caducidad, "minimo_sugerido": self._minimo_sugerido, "conversiones_posibles" :self._conversiones_posibles }
                reactivo_copia.append(aux)

        if accion == 1 and accion == 2 or accion == 3 or accion == 5 or accion == 6:

            #Ayuda a los metodos Agregar_Editar_o_Eliminar_Reactivo y Cambiar_la_UnidadMedida.
            #Se encarga de guardar los cambios en la lista de reactivos. 
            self._reactivos = reactivo_copia
            Gestion_de_Reactivos.Configurar_json(self)
        
        if accion == 4:
            #Este retorna una lista con los reactivos que tienen menos de la cantidad minima sugerida, para que se imprima en el metodo Estatus_de_los_Reactivos.
            return advertensia
    
    def Agregar_Editar_o_Eliminar_Reactivo(self,auxiliador,indicador_del_reactivo):
        #Este metodo se encarga de agregar, editar o eliminar un reactivo.
        #El parametro indicador_del_reactivo es el id del reactivo que se desea editar o eliminar.
        #El parametro auxiliador es el que determina que accion se va a realizar, esto para que el metodo Analizador_de_Informacion_Reactivo sepa que hacer.
        #Si auxiliador es 1, se agrega un reactivo.
        #Si auxiliador es 2, se edita un reactivo.
        #Si auxiliador es 3, se elimina un reactivo.
        if auxiliador == 1:
            if indicador_del_reactivo != 0:
                for s in self._reactivos:
                    self._id_reactivo = max(s.get("id"))+1
                    break
                self._id_reactivo = self._id_reactivo+ + 1
                Gestion_de_Reactivos.Configurar_Reactivo(self)
                Gestion_de_Reactivos.Configurar_json(self)
                return "se agrego el reactivo exitosamente."
            else:
                Gestion_de_Reactivos.Configurar_Reactivo(self)
                Gestion_de_Reactivos.Configurar_json(self)
                return "se agrego el reactivo exitosamente."

        elif auxiliador == 2 or auxiliador == 3:
            if auxiliador == 2:
                self.reactivo_a_configurar = Gestion_de_Reactivos.Analizador_de_Informacion_Reactivo(self,indicador_del_reactivo,2)
                return "Se a editado el reactivo con exito"
            else:
                self.reactivo_a_configurar = Gestion_de_Reactivos.Analizador_de_Informacion_Reactivo(self,indicador_del_reactivo,3)
                return "Se a eliminado el reactivo con exito"

    def Estatus_de_los_Reactivos(self):
        #Este metodo se encarga de ver el estatus de los reactivos, si hay alguno que tenga menos de la cantidad minima sugerida.
        advertensia = Gestion_de_Reactivos.Analizador_de_Informacion_Reactivo(self,0,False,4, None)
        if self.advise == True:
            print("-------ADVERTENCIA-----")
            for s in advertensia:
                print(f"No hay de la cantidad requerrida en el inventario del reactivo: {s[0]}\nCantidad minima sugerida: {s[1]}\nCantidad en el inventario: {s[2]}")
        
        else:
            print("Todo en orden")

    def Cambiar_la_UnidadMedida(self, indicador_del_reactivo):
        #Este metodo se encarga de cambiar la unidad de medicion de un reactivo en especifico.
        #El parametro indicador_del_reactivo es el id del reactivo que se desea cambiar la unidad de medicion.
        Gestion_de_Reactivos.Analizador_de_Informacion_Reactivo(self,indicador_del_reactivo, 5)
        for i in self._reactivos:
            if i.get("id") == indicador_del_reactivo:
                for s in i: 
                    print(f"{s}: {i.get(s)}")
                print("Se a cambiado la unidad de medicion con exito")
            break

    def Configurar_Reactivo(self):

        #Este metodo se encarga de configurar un reactivo, es decir, pedir los datos necesarios para crear un reactivo.
        #Este metodo se auxilia del metodo Agregar_Editar_o_Eliminar_Reactivo, especificamente a auxiliador 1 y 2, ees decir, agregar y editar.

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

    def Configurar_json(self):

        archivo = open("Reactivos.json","w", encoding = "utf-8")
        for s in self._reactivos:
            aux = json.dumps(s)
            archivo.write(f"{aux}\n")
            archivo.close()
            archivo = open("Reactivos.json","a", encoding = "utf-8")
        archivo.close()

    def Experimento(self,indicador_del_reactivo):
        #Este metodo se encarga de hacer un experimento.
        #Aqui va decir si hay la cantidad necesaria o en su defecto, si es necesario hacer un cambio de unidad de medicion.
        #El parametro indicador_del_reactivo es una lista de los reactivos que se van a utilizar en el experimento.s
        Gestion_de_Reactivos.Analizador_de_Informacion_Reactivo(self,indicador_del_reactivo,6)
        return self.costo

