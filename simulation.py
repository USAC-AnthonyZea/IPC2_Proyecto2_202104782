from main import *

class Logica():

    def Asignacion(lista_config, lista_prueba):

        n_t = 0
        n_f = 0

        # Iteramos en la lista de configuraciones
        for i in range(lista_prueba.size):
            obj_prueba = lista_prueba.get_Valor(i) # Obtenemos el objeto de la primera prueba inicial
            id_empresa_prueba = obj_prueba.id_empresa # Obtenemos el id de la empresa a la cual se le hara la simulacion
            id_punto_prueba = obj_prueba.id_punto # Obtenemos el punto de atencion donde estan los escritorios

            # Iteramos en la lista de empresas
            for k in range(lista_config.size):
                obj_empresa = lista_config.get_Valor(k) # Obtenemos el objeto de la clase empresa 
                id_empresa_config = obj_empresa.id # Obtenemos el id de la empresa

                if id_empresa_config == id_empresa_prueba: # Evaluamos que el id de empresa sea igual al de la configuracion

                    # Si es verdadero
                    for l in range(obj_empresa.lista_puntos_atencion.size): # Iteramos en los puntos de atencion

                        obj_puntos_config = obj_empresa.lista_puntos_atencion.get_Valor(l) # Obtenemos el objeto de puntos de atencion
                        id_punto_config = obj_puntos_config.id_punto # Obtenemos el id, del punto de atencion

                        if id_punto_config == id_punto_prueba: # Verificamos que el id de punto inicial sea igual al de la prueba

                            for m in range(obj_puntos_config.lista_escritorios.size):
                                obj_desk_config = obj_puntos_config.lista_escritorios.get_Valor(m)
                                id_desk_config = obj_desk_config.id_escritorio

                                for j in range(obj_prueba.escritorios_activos.size):
                                    obj_desk_prueba = obj_prueba.escritorios_activos.get_Valor(j)
                                    id_desk_prueba = obj_desk_prueba.id_escritorio
                                
                                    if id_desk_config == id_desk_prueba:
                                        obj_desk_config.estado = True
                                        n_t += 1
                                    else:
                                        n_f += 1

                                print(obj_desk_config.imprimir_escritorio())

        lista_cola_clientes = Lista_enlazada() # Creamos una cola para los clientes
        
        # Iteramos en la lista de configuraciones
        for i in range(lista_prueba.size):
            obj_prueba = lista_prueba.get_Valor(i) # Obtenemos el objeto de la primera prueba inicial
            id_empresa_prueba = obj_prueba.id_empresa # Obtenemos el id de la empresa a la cual se le hara la simulacion
            id_punto_prueba = obj_prueba.id_punto # Obtenemos el punto de atencion donde estan los escritorios

            # Iteramos en la lista de empresas
            for k in range(lista_config.size):
                obj_empresa = lista_config.get_Valor(k) # Obtenemos el objeto de la clase empresa 
                id_empresa_config = obj_empresa.id # Obtenemos el id de la empresa

                if id_empresa_config == id_empresa_prueba: # Evaluamos que el id de empresa sea igual al de la configuracion

                    # Si es verdadero
                    for l in range(obj_empresa.lista_puntos_atencion.size): # Iteramos en los puntos de atencion

                        obj_puntos_config = obj_empresa.lista_puntos_atencion.get_Valor(l) # Obtenemos el objeto de puntos de atencion
                        id_punto_config = obj_puntos_config.id_punto # Obtenemos el id, del punto de atencion

                        if id_punto_config == id_punto_prueba: # Verificamos que el id de punto inicial sea igual al de la prueba
                            
                            for j in range(obj_prueba.listado_clientes.size):

                                new_cliente = obj_prueba.listado_clientes.get_Valor(j)
                                lista_cola_clientes.append_inicio(new_cliente)

        
        print('Clientes en Cola:')
        for i in range(lista_cola_clientes.size):
            
            lista_cola_clientes.imprimir_lista('nombre_cliente')

            obj_cliente = lista_cola_clientes.obtener_primer_nodo()

            print(f'{obj_cliente.dato.imprimir_cliente()}')

            if lista_cola_clientes.vacio():
                print('\n\tla simulacion ha terminado')

            #lista_cola_clientes.imprimir_lista('nombre_cliente')


