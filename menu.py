from colorama import Fore, Style
from xmlFile import XML_entry
from main import Lista_enlazada
from configInit import *
from simulation import Logica

#Clase Principal
class App():
    def __init__(self):
        aux = True
        
        # Menu principal
        while aux:
            # Creacion del Menu


            print(Style.BRIGHT + Fore.WHITE + '\n-------- Soluciones Guatemaltecas, S.A -----------')
            print(Style.BRIGHT + Fore.YELLOW + '_Bienvenido al sistema:_\n')

            print(Style.BRIGHT + Fore.WHITE + "-------------------- MENU ------------------------\n")
            print(Style.NORMAL + Fore.WHITE +'1. Configuración de Empresas')
            print('2. Selección de empresa y punto de atención')
            print('3. Manejo de puntos de atención')
            print('4. Salir')
            opcion = input(Style.NORMAL + Fore.GREEN +'\nIngrese la operacion que desea realizar: ')

            # Opcion 1, del menu principal
            if opcion == '1':
                print(Style.BRIGHT + Fore.WHITE +'\n------------- Configuración de Empresas ------------------')
                print(Style.NORMAL + Fore.WHITE + "\n1. Limpiar Sistema")
                print("2. Cargar archivo de configuración del sistema")
                print("3. Crear Nueva empresa")
                print("4. Cargar archivo con configuración Inicial para la prueba")
                opcion_1 = input(Style.NORMAL + Fore.GREEN +'\nIngrese la operacion que desea realizar: ' + Style.RESET_ALL + Fore.RESET)

                ## Limpiar el sistema, borrar todo el contenido de las listas 
                if opcion_1 == '1':
                    print('Limpiando el sistema')
                    lista_vacia = Lista_enlazada()
                    config_init = lista_vacia
                    prueba_init = lista_vacia

                    print('Limpieza realizada')

                ## Opcion 2: cargar el archivo de la configuracion inicial
                elif opcion_1 == '2':
                    verified_file = True
                    print(Style.BRIGHT + Fore.WHITE + "\n------- Cargar archivo -------")
                    while verified_file:
                        archivo = input(Style.NORMAL + Fore.GREEN +'\nIngrese el nombre del archivo (nombreArchivo.xml): ')
                        
                        config_init = XML_entry.config_System(archivo)

                        print(Style.BRIGHT + Fore.CYAN + '\n\tArchivo cargado correctamente')

                        add_file = input(Style.NORMAL + Fore.LIGHTMAGENTA_EX +'\n¿Desea agregar otro archivo? (Si o No): '+ Fore.WHITE)

                        if add_file == 'Si' or add_file == 'si':
                            verified_file = True
                        else:
                            verified_file = False
                
                ## Opcion 3: crear una empresa manualmente
                elif opcion_1 == '3':
                    
                    verified_empresa = True
                    while verified_empresa:

                        empresas_listaEnlazada = Lista_enlazada() # Creamos lista enlaxada para la empresa

                        print(Style.BRIGHT + Fore.WHITE + "\n------- Crear Empresa -------")
                        id_empresa = input(Style.NORMAL + Fore.LIGHTCYAN_EX +'\nIngrese un ID de empresa: '+ Fore.WHITE)
                        name_empresa = input(Style.NORMAL + Fore.LIGHTCYAN_EX +'\nIngrese nombre de empresa: '+ Fore.WHITE)
                        abreviatura_empresa = input(Style.NORMAL + Fore.LIGHTCYAN_EX +'\nIngrese la abreviatura del nombre de empresa: '+ Fore.WHITE)
                        
                        print(Fore.LIGHTBLUE_EX + '\n\tPuntos de atencion: ')
                        temp1 = True
                        while temp1:
                            
                            puntos_atencion_listaEnlazada = Lista_enlazada()

                            id_punto = input(Style.NORMAL + Fore.LIGHTCYAN_EX +'\n\tIngrese un ID de punto de atencion: '+ Fore.WHITE)
                            nombre_punto = input(Style.NORMAL + Fore.LIGHTCYAN_EX +'\n\tIngrese el nombre del punto de atencion: '+ Fore.WHITE)
                            direccion_punto = input(Style.NORMAL + Fore.LIGHTCYAN_EX +'\n\tIngrese la direccion del punto de atencion: '+ Fore.WHITE)
                            
                            print('\n\t\tEscritorios:')
                            temp2 = True
                            while temp2:

                                escritorios_listaEnlazada = Lista_enlazada()

                                id_escritorio = input(Style.NORMAL + Fore.LIGHTCYAN_EX +'\n\t\tIngrese un ID para escritorio: '+ Fore.WHITE)
                                identify_escritorio = input(Style.NORMAL + Fore.LIGHTCYAN_EX +'\n\t\tIngrese una identificacion para el escritorio: '+ Fore.WHITE)
                                encargado_escritorio = input(Style.NORMAL + Fore.LIGHTCYAN_EX +'\n\t\tIngrese el encargado del escritorio: '+ Fore.WHITE)

                                new_escritorio = Escritorios(id_escritorio, identify_escritorio, encargado_escritorio)
                                escritorios_listaEnlazada.append_inicio(new_escritorio)
                            
                                add_desk = input(Style.NORMAL + Fore.LIGHTMAGENTA_EX +'\n\t\t¿Desea agregar otro escritorio? (Si o No): '+ Fore.WHITE)
                                if add_desk == 'Si' or add_desk == 'si':
                                    temp2 = True
                                else:
                                    temp2 = False
                            
                            new_punto_atencion = Puntos_atencion(id_punto, nombre_punto, direccion_punto, escritorios_listaEnlazada)
                            puntos_atencion_listaEnlazada.append_inicio(new_punto_atencion)
                            
                            add_punto = input(Style.NORMAL + Fore.LIGHTMAGENTA_EX +'\n\t¿Desea agregar otro punto de atencion? (Si o No): '+ Fore.WHITE)
                            if add_punto == 'Si' or add_punto == 'si':
                                temp1 = True
                            else:
                                temp1 = False
                            
                        print(Fore.LIGHTBLUE_EX + '\n\tTransacciones: ')
                        temp3 = True
                        while temp3:
                            transacciones_listaEnlazada = Lista_enlazada()

                            id_trans = input(Style.NORMAL + Fore.LIGHTCYAN_EX +'\n\tIngrese un ID de transaccion: '+ Fore.WHITE)
                            nombre_trans = input(Style.NORMAL + Fore.LIGHTCYAN_EX +'\n\tIngrese el nombre de la transaccion: '+ Fore.WHITE)
                            tiempo_trans = input(Style.NORMAL + Fore.LIGHTCYAN_EX +'\n\tIngrese el tiempo de atencion de la transaccion: '+ Fore.WHITE)

                            new_transaccion = Transacciones(id_trans, nombre_trans, tiempo_trans)
                            transacciones_listaEnlazada.append_inicio(new_transaccion)

                            add_trans = input(Style.NORMAL + Fore.LIGHTMAGENTA_EX +'\n\t¿Desea agregar otra transaccion? (Si o No): '+ Fore.WHITE)
                            if add_trans == 'Si' or add_trans == 'si':
                                temp3 = True
                            else:
                                temp3 = False

                        new_empresa = Empresas(id_empresa, name_empresa, abreviatura_empresa, puntos_atencion_listaEnlazada, transacciones_listaEnlazada)
                        empresas_listaEnlazada.append_inicio(new_empresa)

                        add_empresa = input(Style.NORMAL + Fore.LIGHTMAGENTA_EX +'\n¿Desea agregar otra empresa? (Si o No): '+ Fore.WHITE)
                        if add_empresa == 'Si' or add_empresa == 'si':
                            verified_empresa = True
                        else:
                            verified_empresa = False
                
                ## Opcion 4: cargar el archivo de la prueba inicial
                elif opcion_1 == '4':
                    verified_file_init = True
                    print(Style.BRIGHT + Fore.WHITE + "\n------- Cargar archivo -------")
                    while verified_file_init:
                        archivo = input(Style.NORMAL + Fore.GREEN +'\nIngrese el nombre del archivo (nombreArchivo.xml): ')
                        
                        prueba_init = XML_entry.test_System(archivo)

                        print(Style.BRIGHT + Fore.CYAN + '\n\tArchivo cargado correctamente')

                        add_file_init = input(Style.NORMAL + Fore.LIGHTMAGENTA_EX +'\n¿Desea agregar otro archivo? (Si o No): '+ Fore.WHITE)

                        if add_file_init == 'Si' or add_file_init == 'si':
                            verified_file_init = True
                        else:
                            verified_file_init = False
                            

            elif opcion == '2':
                print('\n----- Selección de empresa y punto de atención --------')
                print("\na) Seleccione la empresa: ")
                print("b) Seleccione el punto de atención: ")

            elif opcion == '3':
                print('\n---------------- Simulacion atencion al cliente ----------------------- ' + Fore.RESET + Style.RESET_ALL)
                Logica.Asignacion(config_init, prueba_init)
                
            elif opcion == '4':
                print(Style.BRIGHT + Fore.YELLOW + '\n\tLo esperamos pronto' + Fore.RESET + Style.RESET_ALL)
                aux = False
            else:
                print(Style.BRIGHT + Fore.LIGHTRED_EX + '\nNo ha ingresado una opcion correcta')


if __name__ == "__main__":
    App()