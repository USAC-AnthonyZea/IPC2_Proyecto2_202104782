class Configuracion_inicial():
    def __init__(self, id, id_empresa, id_punto, escritorios_activos, listado_clientes):
        self.id = id
        self.id_empresa = id_empresa
        self.id_punto = id_punto
        self.escritorios_activos = escritorios_activos
        self.listado_clientes = listado_clientes
        
class Escritorios_activos():
    def __init__(self, id_escritorio):
        self.id_escritorio = id_escritorio

class Clientes():
    def __init__(self, dpi, nombre_cliente, listado_transacciones):
        self.dpi = dpi
        self.nombre_cliente = nombre_cliente
        self.listado_transacciones = listado_transacciones

class Transaccion_cliente():
    def __init__(self, id_transaccion, cantidad):
        self.id_transaccion = id_transaccion
        self.cantidad = cantidad