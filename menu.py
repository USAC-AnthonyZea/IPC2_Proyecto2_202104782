from colorama import Fore, Style

class App():
    def __init__(self):

        # Creacion del Menu
        print(Style.BRIGHT + Fore.WHITE + '\n-------- Soluciones Guatemaltecas, S.A -----------')
        print(Style.BRIGHT + Fore.YELLOW + '_Bienvenido al sistema:_\n')

        print(Style.BRIGHT + Fore.WHITE + "-------------------- MENU ------------------------\n")
        print(Style.NORMAL + Fore.WHITE +'1. Configuración de Empresas')
        print('2. Selección de empresa y punto de atención')
        print('3. Manejo de puntos de atención')
        print('4. Salir')
        opcion = input(Style.NORMAL + Fore.GREEN +'\nIngrese la operacion que desea realizar: ')

        if opcion == '1':
            print(Style.BRIGHT + Fore.WHITE +'\n------------- Configuración de Empresas ------------------')
            print(Style.NORMAL + Fore.WHITE + "\n1. Limpiar Sistema")
            print("2. Cargar archivo de configuración del sistema")
            print("3. Crear Nueva empresa")
            print("4. Cargar archivo con configuración Inicial para la prueba")
            opcion_1 = input(Style.NORMAL + Fore.GREEN +'\nIngrese la operacion que desea realizar: ')

            if opcion_1 == '2':
                print()
        
        elif opcion == '2':
            print('\n----- Selección de empresa y punto de atención --------')
            print("\na) Seleccione la empresa: ")
            print("b) Seleccione el punto de atención: ")

        elif opcion == '3':
            print('\n---------------- Manejo de puntos de atención -----------------------')
            print("\n1. Ver estado del punto de atencion")
            print("2. Activar o Desactivar escritorio de servicio (1 ó 0, respectivamente)")
            print("3. Atender Cliente")
            print("4. Solicitud de Atención")
        else:
            print(Style.BRIGHT + Fore.LIGHTRED_EX + '\nNo ha ingresado una opcion correcta')


if __name__ == "__main__":
    App()