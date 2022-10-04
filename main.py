# Creamos clase Nodo, para todas las listas
class Nodo():
    def __init__(self, dato, pos) -> None:
        self.dato = dato
        self.pos = pos
        self.siguiente = None

# Creamos clase para empresas
class Empresas():

    def __init__(self, id, nombre, abreviatura, lista_puntos_atencion, lista_transacciones):
        self.id = id
        self.nombre = nombre
        self.abreviatura = abreviatura
        self.lista_puntos_atencion = lista_puntos_atencion
        self.lista_transacciones = lista_transacciones

    def imprimir_empresa(self):

         return f'''
        ID: {self.id}
        Empresa: {self.nombre}
        Abreviatura: {self.abreviatura}
        _______________________________
            '''

# Creamos clase para puntos de atencion
class Puntos_atencion():
    def __init__(self, id_punto, nombre_punto, direccion_punto, lista_escritorios):
        self.id_punto = id_punto
        self.nombre_punto = nombre_punto
        self.direccion = direccion_punto
        self.lista_escritorios = lista_escritorios

    def imprimir_punto_atencion(self):
        return f'''
    ID: {self.id_punto}
    Punto de Atencion: {self.nombre_punto}
    Direccion: {self.direccion}
    _______________________________
        '''

# Creamos clara para trasnacciones
class Transacciones():
    def __init__(self, id_trans, nombre_trans, tiempo_trans):
        self.id_trans = id_trans
        self.nombre_trans = nombre_trans
        self.tiempo_trans = tiempo_trans
    
    def imprimir_punto_atencion(self):
        return f'''
    ID: {self.id_trans}
    Nombre: {self.nombre_trans}
    Tiempo de Atencion: {self.tiempo_trans}
    _______________________________
        '''

class Escritorios():
    def __init__(self, id_escritorio, identificacion, encargado):
        self.id_escritorio = id_escritorio
        self.identificacion = identificacion
        self.encargado = encargado
    
    def imprimir_escritorio(self):
        return f'''
    ID: {self.id_escritorio}
    Identificacion: {self.identificacion}
    Encargado: {self.encargado}
    _______________________________
        '''
        
# ---------------- Aqui viene todo el TDA (Linked List) -------------------- #
class Lista_enlazada():

    def __init__(self) -> None:
        self.raiz = None
        self.size = 0
    
    # Metodo para agregar datos al inicio
    def append_inicio(self, dato):
        if self.raiz == None:
            self.raiz = Nodo(dato, self.size)
        else:
            aux = self.raiz
            while aux.siguiente != None:
                aux = aux.siguiente
            aux.siguiente = Nodo(dato, self.size)
            
        self.size += 1

    # Metodo para agregar datos al final
    def append_final(self, dato):
        if not self.raiz:
            self.raiz = Nodo(dato = dato)
            return
        actual = self.raiz
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = Nodo(dato = dato)

    def get_Valor(self, indice):
        aux = self.raiz
        while aux is not None:
            if aux.pos == indice:
                return aux.dato
            aux = aux.siguiente
        return None