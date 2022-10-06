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
    
    def imprimir_transaccion(self):
        return f'''
    ID: {self.id_trans}
    Nombre: {self.nombre_trans}
    Tiempo de Atencion: {self.tiempo_trans}
    _______________________________
        '''

class Escritorios():
    def __init__(self, id_escritorio, identificacion, encargado, estado):
        self.id_escritorio = id_escritorio
        self.identificacion = identificacion
        self.encargado = encargado
        self.estado = estado
    
    def imprimir_escritorio(self):
        return f'''{self.id_escritorio} por {self.encargado}'''
        