# Creamos clase Nodo, para todas las listas
class Nodo():
    def __init__(self, dato = None, siguiente = None):
        self.dato = dato
        self.siguiente = siguiente

# Creamos clase para empresas
class Empresas():

    def __init__(self, id, nombre, abreviatura):
        self.id = id
        self.nombre = nombre
        self.abreviatura = abreviatura
        self.lista_punto_atencion = Lista_enlazada()
        self.lista_transacciones = Lista_enlazada()

# Creamos clase para puntos de atencion
class Puntos_atencion():
    def __init__(self, id_punto, nombre_punto, direccion_punto):
        self.id_punto = id_punto
        self.nombre_punto = nombre_punto
        self.direccion = direccion_punto
        self.lista_escritorios = Lista_enlazada()

# Creamos clara para trasnacciones
class Transacciones():
    def __init__(self, id_trans, nombre_trans, tiempo_trans):
        self.id_trans = id_trans
        self.nombre_trans = nombre_trans
        self.tiempo_trans = tiempo_trans

class Escritorios():
    def __init__(self, id_escritorio, identificacion, encargado):
        self.id_escritorio = id_escritorio
        self.identificacion = identificacion
        self.encargado = encargado
        
# ---------------- Aqui viene todo el TDA (Linked List) -------------------- #
class Lista_enlazada():

    def __init__(self) -> None:
        self.raiz = None # Definimos la cabeza
    
    # Metodo para agregar datos al inicio
    def append_inicio(self, dato_):
        self.raiz = Nodo(dato = dato_, siguiente = self.raiz)

    # Metodo para agregar datos al final
    def append_final(self, dato_):
        if not self.raiz:
            self.raiz = Nodo(dato = dato_)
            return
        actual = self.raiz
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = Nodo(dato = dato_)

    # Método para imprimir la lista de nodos
    def imprimir_lista(self, llave):
        nodo = self.raiz
        while nodo != None:
            print(getattr(nodo.dato, llave), " => ")
            nodo = nodo.siguiente