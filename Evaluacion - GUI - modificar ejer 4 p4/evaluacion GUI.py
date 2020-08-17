import csv
import PySimpleGUI as sg
import json

def ejer4():
    """
    4-
    ENUNCIADO:
    En base al ejercicio 5 de la Práctica 3, diagramar una interfaz en 
    PySimpleGUI que permita seleccionar dos archivos (utilizando el widget
    FileBrowse). Uno de ellos contendrá colores y el otro coordenadas. Ambos
    archivos se encuentran en texto plano, donde cada elemento se ubica en una
    línea. Utilizando el widget Graph, dibuje en cada coordenada, un punto
    (con DrawPoint) del color asociado (correspondiente a la misma línea de 
    ambos archivos). Para realizar las pruebas, genere ambos archivos. Para
    generar el de colores, investigue los disponibles en el ejemplo de colores
    en Github.
    """
    layout = [[sg.Text('Seleccione los archivos de Txt')],
              [sg.Text('Source for colores', size=(15, 1)), sg.InputText(), sg.FileBrowse(key='COLORES')],
              [sg.Text('Source for coordenadas', size=(15, 1)), sg.InputText(), sg.FileBrowse(key='COORDENADAS')],
              [sg.Button('Cargar archivos'), sg.Cancel(),sg.Button('Ordenar',disabled=True)],     
              [sg.Graph(canvas_size=(200,200), graph_bottom_left=(0, 0), graph_top_right=(150, 150), background_color='white', enable_events=True, key='graph'),sg.Listbox('-',size=(20,10),key='list')],
              [sg.Button('Guardar',visible=False)]
             ]
    window = sg.Window('Ejer4y5',layout)
    while True:
        event, values = window.read()
        if event is 'Cancel' or event is None:
            break
        if event is 'Cargar archivos':   
            try:
                c = open(values[0],'r')
                x = open(values[1],'r')
                colores = c.read().split()
                coordenadas = x.read().split()
                lista=[]
                # este if es para obteber la lista de menos elementos para 
                # iterar sobre esa lista, sino en caso de que iteremos sobre
                # la lista con mas elementos, al querer juntar ambos datos es
                # posible que de error por encontrar un inice fuera de rango al
                # recorrer la lista de menor tamaño
                if len(colores) > len(coordenadas):
                    cantidad_a_recorrer = len(coordenadas)
                else:
                    cantidad_a_recorrer = len(colores)   
                for i in range(cantidad_a_recorrer):
                    tupla = (colores[i],coordenadas[i])
                    lista.append(tupla)
                for i in lista: 
                    print(i)
                    coords=i[1].split(',')
                    window['graph'].draw_point((int(coords[0]),int(coords[1])), 30, color=i[0])
                window['Guardar'].update(visible=True)  
                window['Ordenar'].update(disabled=False)
            except FileNotFoundError:
                sg.popup('No se cargaron los archivos')
        if event is 'Guardar':  
            colores.sort(reverse=True)
            try: 
                with open('colores.txt','w') as file:
                    for color in colores:
                        file.writelines(color)
                        file.writelines('\n')
                sg.popup('archivo guardado')        
            except FileNotFoundError:   
                sg.popup('No se encontro el archivo') 
        if event is 'Ordenar':
            window['list'].Update(values=colores)        


ejer4()