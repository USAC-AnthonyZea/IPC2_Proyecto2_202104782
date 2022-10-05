import xml.etree.cElementTree as ET
from testInit import *
from configInit import *
from main import *

class XML_entry():

    def config_System(archivo):
        
        tree = ET.parse(archivo) #Parseas el archivo Xml
        empresas = tree.getroot() # Obtener la lista de empresas

        empresas_listaEnlazada = Lista_enlazada()

        # Iteramos sobre las empresas
        for empresa in empresas:
            id_empresa = empresa.get('id') # Obtenemos el id de empresa
            nombre_empresa = empresa.find('nombre').text # Obtenemos el nombre de empresa
            abreviatura = empresa.find('abreviatura').text # Obtenemos la abreviatura de empresa

            puntos_de_atencion_listaEnlazada = Lista_enlazada() # Creamos lista enlazada para los puntos de atencion
            transacciones_listaEnlazada = Lista_enlazada()

            # Iteramos sobre la lista de puntos de atencion
            for puntos_Atencion in empresa.iter('listaPuntosAtencion'):

                # Iteramos sobre el punto de atencion especifico
                for punto_atencion in puntos_Atencion.iter('puntoAtencion'):

                    id_punto = punto_atencion.get('id') # Obtenemos el id de punto de atencion
                    nombre_punto = punto_atencion.find('nombre').text # Obtenemos el nombre 
                    direccion = punto_atencion.find('direccion').text # Obtenemos la direccion
                    
                    escritorios_listaEnlazada = Lista_enlazada() # Creamos lista enlazada para los escritorios

                    # Iteramos sobre la lista de escritorios
                    for lista_Escritorios in punto_atencion.iter('listaEscritorios'):

                        # Iteramos sobre el escritorio especifico
                        for escritorio in lista_Escritorios.iter('escritorio'):
                            
                            id_escritorio = escritorio.get('id') # Obtenemos id de escritorio
                            identify_escritorio = escritorio.find('identificacion').text # Obtenemos identificaion de escritorio
                            encargado_escritorio = escritorio.find('encargado').text # Obtenemos al encargado del escritorio

                            nuevo_Escritorio = Escritorios(id_escritorio, identify_escritorio, encargado_escritorio, False) # Objeto de la clase Escritorios
                            escritorios_listaEnlazada.append_inicio(nuevo_Escritorio) #Lo añadimos a la lista elazada
                    
                    nuevo_punto_atencion = Puntos_atencion(id_punto, nombre_punto, direccion, escritorios_listaEnlazada) # Objeto de la clase Punto de atencion
                    puntos_de_atencion_listaEnlazada.append_inicio(nuevo_punto_atencion) # Lo añadimos a la lista de puntos de atencion

            # Iteramos para obtener las transacciones
            for transacciones in empresa.iter('listaTransacciones'):
                for transaccion in transacciones.iter('transaccion'):
                    id_trans = transaccion.get('id') # Obtenemos el id de transaccion
                    nombre_trans = transaccion.find('nombre').text # Obtenemos el nombre de la transaccion
                    tiempo_trans = transaccion.find('tiempoAtencion').text # Obtenemos el tiempo de atencion


                    nueva_transaccion = Transacciones(id_trans, nombre_trans, tiempo_trans) # Objeto de la clase Transaccion
                    transacciones_listaEnlazada.append_inicio(nueva_transaccion) # Lo añadimos a la lista enlazada
            
            nueva_empresa = Empresas(id_empresa, nombre_empresa, abreviatura, puntos_de_atencion_listaEnlazada, transacciones_listaEnlazada) # Objeto de la clase Transaccion
            empresas_listaEnlazada.append_inicio(nueva_empresa) # Lo añadimos a la lista enlazada
  

            return empresas_listaEnlazada

        # Imprimimos valores del primer archivo
        for i in range(empresas_listaEnlazada.size): # Iteramos en el tamaño de la lista de empresas
            empresa = empresas_listaEnlazada.get_Valor(i) #Obtenemos el nodo 'i', el cual es un objeto de la clase empresa
            # Imprimimos las empresas
            print(f'''
    Empresa: {i + 1}
    {empresa.imprimir_empresa()}
            ''')

            # Iteramos para los puntos de atencion
            for j in range(empresa.lista_puntos_atencion.size): # Iteramos en el tamaño de la lista de puntos de atencion
                point_atencion = empresa.lista_puntos_atencion.get_Valor(j) # Obtenemos el nodo 'j', el cual es un objeto de la clase Puntos de atencion
                # Imprimimos los puntos de atencion
                print(f'''
        Punto de atencion: {j + 1}
        {point_atencion.imprimir_punto_atencion()}
                ''')

                # Iteramos para los escritorios
                for k in range(point_atencion.lista_escritorios.size): # Iteramos en el tamaño de la lista de escritorios
                    desk = point_atencion.lista_escritorios.get_Valor(k) # Obtenemos el nodo 'k', el cual es un objeto de la clase Escritorios
                    # Imprimimos los escritorios
                    print(f'''
            Escritorio: {k + 1}
            {desk.imprimir_escritorio()}
                    ''')
            for l in range(empresa.lista_transacciones.size):
                transaction = empresa.lista_transacciones.get_Valor(l) # Obtenemos el nodo 'j', el cual es un objeto de la clase Puntos de atencion
                # Imprimimos los puntos de atencion
                print(f'''
        Transaccion: {l + 1}
        {transaction.imprimir_punto_atencion()}
                ''')
            

    def test_System(archivo):

        tree = ET.parse(archivo) #Parseas el archivo Xml
        configuraciones_iniciales = tree.getroot() # Obtener la lista de la configuracion inicial

        config_inicial_listaEnlazada = Lista_enlazada()

        for config_inicial in configuraciones_iniciales:
            id_config = config_inicial.get('id') # Obtenemos el id de la configuracion
            id_empresa = config_inicial.get('idEmpresa') # Obtenemos el id de empresa inicial
            id_punto = config_inicial.get('idPunto')

            escritorios_activos_listaEnlaxada = Lista_enlazada()
            clientes_listaEnlazada = Lista_enlazada()

            for escritorios_activados in config_inicial.iter('escritoriosActivos'):
                for desk_activo in escritorios_activados.iter('escritorio'):

                    id_escritorio = desk_activo.get('idEscritorio')

                    new_escritorio = Escritorios_activos(id_escritorio)
                    escritorios_activos_listaEnlaxada.append_inicio(new_escritorio)

            for listado_clientes in config_inicial.iter('listadoClientes'):
                for cliente in listado_clientes.iter('cliente'):

                    dpi = cliente.get('dpi')
                    nombre_cliente = cliente.find('nombre').text

                    transacciones_listaEnlazada = Lista_enlazada()

                    for listado_transacciones in cliente.iter('listadoTransacciones'):
                        for transaccion in listado_transacciones.iter('transaccion'):
                            id_transaccion = transaccion.get('idTransaccion')
                            cantidad = transaccion.get('cantidad')

                            new_transaccion = Transaccion_cliente(id_transaccion, cantidad)
                            transacciones_listaEnlazada.append_inicio(new_transaccion)
                            
                    new_cliente = Clientes(dpi, nombre_cliente, transacciones_listaEnlazada)
                    clientes_listaEnlazada.append_inicio(new_cliente)

            new_configInicial = Configuracion_inicial(id_config, id_empresa, id_punto, escritorios_activos_listaEnlaxada, clientes_listaEnlazada)
            config_inicial_listaEnlazada.append_inicio(new_configInicial)

            return config_inicial_listaEnlazada

    
#XML_entry.config_System()
#XML_entry.test_System()