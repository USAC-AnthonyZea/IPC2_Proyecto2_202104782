import os

class Graphviz():

    def graficar(lista_cola_clientes, lista_pila_desk):

        #Estructura de graphviz al inicio
        estruct_inicio = '''graph  grafi{
rankdir=TB;
labelloc="t";
label="Atencion al cliente";
node[shape="circle"
fixedsize=true
width=0.8
height=0.8
];

    subgraph cluster_1 {
        node [shape = plaintext fillcolor="gold:brown" style="radial" gradientangle=180];
        style="filled";
        color="aquamarine";
        label="Clientes";

        subgraph cluster_b{
            node [style=filled shape="rectangle"];
            style="filled";
            color="gray";
            label="En espera";
        '''

        verified_cliente = True
        # Verificamos que se hayan atendido a todos los clientes

        while verified_cliente:
            file_dot = open('Simulate\graph.txt', 'w') # Abrimos archivo para escribir graphviz

            for i in range(lista_cola_clientes.size): # Iteramos en la lista de clientes

                obj_clase_cliente = lista_cola_clientes.get_Valor(i)
                nombre_cliente = obj_clase_cliente.nombre_cliente
                estruct_inicio += f'"{nombre_cliente}";\n'

            estruct_inicio += '''\n}
            '''

            for i in range(lista_pila_desk.size): # Iteramos en la lista de escritorios activos
                
                obj_desk_activo = lista_pila_desk.get_Valor(i) # Obtenemos el objeto del escritorio
                estado_desk_activo = obj_desk_activo.estado # Obtenemos el estado, para ver si es activo o inactivo

                for j in range(lista_cola_clientes.size): # Iteramos en la lista de clientes

                    #lista_cola_clientes.imprimir_lista('nombre_cliente')
                    
                    if estado_desk_activo == True: # Validamos que sea un escritorio activo
                        
                        # Agregamos un subgrafo
                        estruct_inicio += f'''
                        subgraph cluster_{i+1} 
                        '''
                        
                        # Para agregar los escritorios activos
                        estruct_inicio += '''{
                            node [style=filled shape="circle"];
                            style="filled";
                            color="wheat";
                            label="Escritorio";
                        '''

                        lista_cola_clientes.imprimir_lista('nombre_cliente')

                        obj_cliente = lista_cola_clientes.obtener_primer_nodo()
                        estruct_inicio += f'"{obj_cliente.dato.imprimir_cliente()}";'
                        estruct_inicio += '}'

                        estruct_inicio += '''\n
                            }
                        }'''
                        file_dot.write(estruct_inicio)
                        file_dot.close()
                        os.system(f'dot.exe -Tpng Simulate\graph.txt -o Simulate\Estado{j}.png')
                        break

                if lista_cola_clientes.vacio():
                    print('\n\tla simulacion ha terminado')
                    verified_cliente = False
                    break


        



        