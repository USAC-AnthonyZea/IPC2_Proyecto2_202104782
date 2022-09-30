import xml.etree.cElementTree as ET

def config_System():
    root = 'configXml.xml' #Ruta del archivo

    tree = ET.parse(root) #Parseas el archivo Xml
    empresas = tree.getroot() # Obtener la lista de empresas
    lista = []
    n = 1
    cc = 1
    co = 1

    # Iteramos sobre las empresas
    for empresa in empresas:
        print(f'\nEmpresa {n}:')

        print(empresa.get('id')) # Obtenemos el id de empresa
        print(empresa.find('nombre').text) # Obtenemos el nombre de empresa
        print(empresa.find('abreviatura').text) # Obtenemos la abreviatura de empresa

        #listaPuntosAtencion = Lista_enlazada() # Creamos la lista para los puntos de atencion
        
        # Iteramos sobre la lista de puntos de atencion
        for puntos_Atencion in empresa.iter('listaPuntosAtencion'):

            # Iteramos sobre el punto de atencion especifico
            for punto_atencion in puntos_Atencion.iter('puntoAtencion'):
                print(f'\nPunto de Atencion {co}:')

                print(punto_atencion.get('id')) # Obtenemos el id de punto de atencion
                print(punto_atencion.find('nombre').text) # Obtenemos el nombre 
                print(punto_atencion.find('direccion').text) # Obtenemos la direccion

                co+=1

                #listaEscritorio = Lista_enlazada() # Creamos lista enlazada para los escritorios

                # Iteramos sobre la lista de escritorios
                for lista_Escritorios in punto_atencion.iter('listaEscritorios'):

                    # Iteramos sobre el escritorio especifico
                    for escritorio in lista_Escritorios.iter('escritorio'):
                        print(f'\nEscritorio {cc}:')

                        print(escritorio.get('id'))
                        print(escritorio.find('identificacion').text)
                        print(escritorio.find('encargado').text)
                        cc+=1
        n+=1
                        
        
config_System()