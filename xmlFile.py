import xml.etree.cElementTree as ET
from main import *

class XML_entry():

    def config_System():
        root = 'configXml.xml' #Ruta del archivo

        tree = ET.parse(root) #Parseas el archivo Xml
        empresas = tree.getroot() # Obtener la lista de empresas
        listaEmpresasXml = Lista_enlazada()

        # Iteramos sobre las empresas
        for empresa in empresas:
            id_empresa = empresa.get('id') # Obtenemos el id de empresa
            nombre_empresa = empresa.find('nombre').text # Obtenemos el nombre de empresa
            abreviatura = empresa.find('abreviatura').text # Obtenemos la abreviatura de empresa

            nueva_Empresa = Empresas(id_empresa, nombre_empresa, abreviatura)

            listaEmpresasXml.append_inicio(nueva_Empresa)

            # Iteramos sobre la lista de puntos de atencion
            for puntos_Atencion in empresa.iter('listaPuntosAtencion'):

                # Iteramos sobre el punto de atencion especifico
                for punto_atencion in puntos_Atencion.iter('puntoAtencion'):
                    id_punto = punto_atencion.get('id') # Obtenemos el id de punto de atencion
                    nombre_punto = punto_atencion.find('nombre').text # Obtenemos el nombre 
                    direccion = punto_atencion.find('direccion').text # Obtenemos la direccion

                    nuevo_punto_atencion = Puntos_atencion(id_punto, nombre_punto, direccion)
                    nueva_Empresa.lista_punto_atencion.append_inicio(nuevo_punto_atencion)

                    # Iteramos sobre la lista de escritorios
                    for lista_Escritorios in punto_atencion.iter('listaEscritorios'):

                        # Iteramos sobre el escritorio especifico
                        for escritorio in lista_Escritorios.iter('escritorio'):
                            id_escritorio = escritorio.get('id')
                            identify_escritorio = escritorio.find('identificacion').text
                            encargado_escritorio = escritorio.find('encargado').text

                            nuevo_Escritorio = Escritorios(id_escritorio, identify_escritorio, encargado_escritorio)
                            nuevo_punto_atencion.lista_escritorios.append_inicio(nuevo_Escritorio)
        
        print(listaEmpresasXml.imprimir_lista('nombre'))


XML_entry.config_System()


    #def test_System():
    #    print()