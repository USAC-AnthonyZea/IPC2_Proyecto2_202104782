# Creamos clase Nodo, para todas las listas
class Nodo():
    def __init__(self, dato, pos) -> None:
        self.dato = dato
        self.pos = pos
        self.siguiente = None

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

    def obtener_primer_nodo(self):
        request = self.raiz
        self.raiz = self.raiz.siguiente
        return request

    def imprimir_lista(self, llave):
        nodo = self.raiz
        print('\nEscritorio', end=' - ')
        while nodo != None:
            print(getattr(nodo.dato, llave), end=' - ')
            nodo = nodo.siguiente
        print('\n')
    
    # Método para verificar si la estructura de datos esta vacia
    def vacio(self):
        return self.raiz == None