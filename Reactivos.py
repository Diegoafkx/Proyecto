from Lector_de_APIS import _Lector_de_APIS 
import json

#Este modulo se encarga de activar el modulo de Lector_de_APIS, enviando el url y el indicador correspondiente.
#Luego lee el archivo JSON que se genero y guarda la informacion en una lista que le heredara a la clase Gestion_de_Reactivos.

class __Reactivos:
    def __init__(self):
        self._id_reactivo = None
        self._nombre = None
        self._descripcion = None
        self._costo = None
        self._categoria = None
        self._inventario_disponible = None
        self._unidad_de_medicion = None
        self._fecha_de_caducidad = None
        self._minimo_sugerido = None
        self._conversiones_posibles = None
        self._rotacion = None
        self._veces_que_falto = None
        self._desperdicio = None
        self._caduco = None
        self._reactivos = []
        
    def Guardar_Datos(self):
        #Este metodo se utiliza para mandar a sacar la informacion del url
        
        api = _Lector_de_APIS("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/refs/heads/main/reactivos.json", 2)
        api.Hacer_Request()
       
    def Lector_de_Datos(self):
        archivo = open("Reactivos.json","r", encoding = "utf-8")
        informacion_del_archivo = archivo.readlines()
        for s in informacion_del_archivo:
            s = json.loads(s)
            self._reactivos.append(s)
        archivo.close()

    def Agregar_Contadores(self):
        
        #Este metodo se encarga de asociar los datos de la API que guardamos en el archivo Reactivos.json con los atributos de la clase.
        #Aqui actualizaremos los datos agregandole los contadores de cuantas veces fueron rotados, se agotaron, cuantas veces hizo falta para hacer un experimento y cuantas veces se desperdicio el reactivos. 
        reactivos_copia=[]
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
            self._rotacion = 0
            self._veces_que_falto = 0
            self._desperdicio = 0
            self._caduco = 0

            aux = {"id":self._id_reactivo,"nombre": self._nombre, "descripcion": self._descripcion, "costo": self._costo, "categoria": self._categoria, "inventario_disponible": self._inventario_disponible, "unidad_medida": self._unidad_de_medicion, "fecha_caducidad": self._fecha_de_caducidad, "minimo_sugerido": self._minimo_sugerido, "conversiones_posibles" :self._conversiones_posibles, "rotacion": self._rotacion,"veces_que_falto": self._veces_que_falto,"veces_que_se_desperdicio":self._desperdicio,"veces_que_caduco":self._caduco}
            reactivos_copia.append(aux)
        self._reactivos = reactivos_copia
   
    def Configurar_json(self):
        #Este metodo actualiza la base de datos del inventario con cada accion que cambie algun detalle de algun reactivo.
        archivo = open("Reactivos.json","w", encoding = "utf-8")
        for s in self._reactivos:
            aux = json.dumps(s)
            archivo.write(f"{aux}\n")
            archivo.close()
            archivo = open("Reactivos.json","a", encoding = "utf-8")
        archivo.close()