import xml.etree.cElementTree as ET

class XML_entry():

    def config_System():
        root = 'configXml.xml' #Ruta del archivo

        tree = ET.parse(root) #Parseas el archivo Xml
        listaEmpresas = tree.getroot() # Obtener la lista de empresas
    
    def test_System():
        print()