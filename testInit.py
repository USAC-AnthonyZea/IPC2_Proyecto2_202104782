# Creamos clase para la configuracion inicial, respecto a la prueba inicial
class Configuracion_inicial():
    def __init__(self, id, id_empresa, id_punto, escritorios_activos, listado_clientes):
        self.id = id
        self.id_empresa = id_empresa
        self.id_punto = id_punto
        self.escritorios_activos = escritorios_activos
        self.listado_clientes = listado_clientes
        
# Clase para los escritorios activos
class Escritorios_activos():
    def __init__(self, id_escritorio):
        self.id_escritorio = id_escritorio

    def imprimir_escritorios_activos(self):
        return f'''{self.id_escritorio}'''

# Clase para los clientes que estaran dentro de la fila de espera
class Clientes():
    def __init__(self, dpi, nombre_cliente, listado_transacciones):
        self.dpi = dpi
        self.nombre_cliente = nombre_cliente
        self.listado_transacciones = listado_transacciones

    def imprimir_cliente(self):
        return f'''{self.nombre_cliente}'''

    def imprimir_consola(self):
        return f'''----> El cliente {self.nombre_cliente} con DPI: {self.dpi}, esta siendo atendido en el escritorio con ID: '''

# Clase para las transacciones que realizaran cada uno de los clientes
class Transaccion_cliente():
    def __init__(self, id_transaccion, cantidad):
        self.id_transaccion = id_transaccion
        self.cantidad = cantidad

    def imprimir_transaccion_cliente(self):
        return f'''ID de la transaccion: {self.id_transaccion}, Con una cantidad de: {self.cantidad}'''