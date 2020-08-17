import PySimpleGUI as sg
import json
import csv
import time
from datetime import datetime
from pattern.es import conjugate
from pattern.es import INFINITIVE
from pattern.es import parse,split
import random


def ejer1():
    """
    ENUNCIADO:
    Diagrame una interfaz en PySimpleGUI que permita ingresar dos datos: 
    temperatura y humedad, junto con la fecha y hora actual. Al presionar
    Añadir , deberá cargar los valores en una lista (Listbox). Añada un
    botón, que permita guardar esta información en un archivo en formato
    json.
    """
    info_clima = {}
    layout = [
                [sg.Text('Temperatura'),sg.InputText('',key = 'temp')],
                [sg.Text('Humedad'),sg.Input('',key = 'humed')],
                [sg.Button('Añadir'),sg.Button('Guardar'),sg.Button('Salir')],
                [sg.Listbox('',size=(60,20),key='lista')]
             ]
    window = sg.Window('Ejer 1',layout) 
    now = datetime.now()   
    while True:
        now = datetime.now()
        event, values = window.read()
        if event is None or event is 'Salir':
            break
        if event is 'Añadir':
            fec_y_hora = '{}/{}/{}, {}:{}'.format(now.day,now.month,now.year, now.hour,now.minute)
            linea = 'Temperatura: ',values['temp'], 'Humedad: ',values['humed'], 'Fecha y hora:' , fec_y_hora
            window['lista'].update(values=linea)
        if event is 'Guardar':
            info_clima['fec_y_hora']=fec_y_hora,{'Temperatura':values['temp'],'Humedad':values['humed']}
            with open('ejer1.json','a+') as file:
                json.dump(info_clima,file,indent=4)
 

def ejer2():
    """
    ENUNCIADO:
    Registrar los jugadores del Ejercicio 3 de la Práctica 3 en un archivo
    utilizando cualquiera de las librerías dadas en la teoría (Pickle, JSON,
    CSV). Implementar una función denominada modificoDatos, la cual solicita 
    (mediante una interfaz generada con PySimpleGUI) los datos de un jugador, 
    si este existe en el archivo, modifica dichos datos en el mismo. Si no 
    existe el jugador, lo agrega.
    """
    def  limpiar_pantalla(window,datos):
        with open('infoJugadores.txt','w') as arch:             
                    json.dump(datos, arch,indent=4)
        sg.popup('Cambios Realizados')
        window['name'].Update('')  
        window['points'].Update('')  
        window['lvl'].Update('')  
        window['time'].Update('')  

    def modificoDatos():
        layout = [
                    [sg.Text('Bienvenido al prgrama de registro de jugadores')],
                    [sg.Text('Ingrese el nombre:'),sg.Input(key='name')],
                    [sg.Text('Ingrese el puntaje:'),sg.Input(key='points')],
                    [sg.Text('Ingrese el nivel:'),sg.Input(key='lvl')],
                    [sg.Text('Ingrese el tiempo:'),sg.Input(key='time')],
                    [sg.Button('Modificar/Guardar'),sg.Button('Salir')]
                ]
        window = sg.Window('Ejer 2',layout) 
        with open('infoJugadores.txt','r') as arch:             
            datos=json.load(arch)
        while True:
            event, values = window.read()
            if event is None or event is 'Salir':
                break
            if event is 'Modificar/Guardar':
                if values['name'] in datos.keys():
                    sg.popup('El jugador existe, se van a realizar los cambios')
                    jugador = datos[values['name']]
                    try:
                        jugador['points'] = int(values['points'])
                    except ValueError:
                        sg.popup('Se ingresaron datos invalidos en "Puntos", este campo no sufrirar cambios')
                    try:    
                        jugador['lvl'] = int(values['lvl'])
                    except ValueError:
                        sg.popup('Se ingresaron datos invalidos en "Nivel", este campo no sufrirar cambios')
                    try:    
                        jugador['time'] = int(values['time'])
                    except ValueError:
                        sg.popup('Se ingresaron datos invalidos en "Tiempo", este campo no sufrirar cambios')   
                    limpiar_pantalla(window,datos)
                elif values['name'].strip() == '':
                        sg.popup('No se ingreso ningun nombre')   
                else:
                    sg.popup('El jugador no existe, se cargaran sus datos')
                    try:
                        juga_nuevo = {'lvl': int(values['lvl']), 'points': int(values['points']), 'time': int(values['time'])}
                        datos.setdefault(values['name'],juga_nuevo)    
                        limpiar_pantalla(window,datos)
                    except ValueError:
                        sg.popup('Faltan ingresar datos para el jugador nuevo o hay datos invalidos')
                    
  
                
    '''=========== inicio del ejercicio aca ============'''  

    jugadores = {
                'fede': { 'lvl': 3, 'points': 4, 'time': 200 },
                'belen': { 'lvl': 5, 'points': 10, 'time': 400 },
                'juan': { 'lvl': 15, 'points': 110, 'time': 400 },
                'pedro': { 'lvl': 5, 'points': 3, 'time': 400 }
                 }
    with open('infoJugadores.txt','w') as arch:             
        json.dump(jugadores, arch,indent=4)
    modificoDatos()        
 
 
def ejer3():
    """
    ENUNCIADO:
    Leer un texto desde un archivo y generar uno nuevo (denominado verbos.
    json) que contenga una estructura con todos los verbos convertidos a 
    infinitivo junto con la cantidad de apariciones de cada uno.
    """
    #GENRERO EL ARCHIVO PARA USAR
    with open('ejer3.txt','w') as arch:
        json.dump('Hola, Como andas trolo vamos a corre soy yo o sos vos corre',arch)
  

    #ABRO EL ARCHIVO Y GUARDO LOS DATOS
    with open('ejer3.txt','r') as archi:
        datos = json.load(archi)
   
    #datos=['hola, lucas perro gato']
    #PRIMERO OBTENGO LOS DATOS DE CADA PALABRA Y LUEGO DIVIDO LA FRASE
    s=parse(datos).split()

    #CREO UNA LISTA PARA GUARDAR LOS VERBOS EN INFINITIVO
    listaInfinitivos=[]
    for pal in s[0]:
        print(pal)
        if pal[1]=='VB':
            listaInfinitivos.append(conjugate(pal[0],INFINITIVE))

    #CREO OTRA LISTA PARA CONTAR LAS OCURRENCIAS DE CADA VERBO
    recuenciaPalab=[]
    for pal in listaInfinitivos:
        recuenciaPalab.append(listaInfinitivos.count(pal))

    #PRIMERO UNO LAS LISTAS CON EL ZIP, ME QUEDARA CADA PALABRA CON SU CANTIDAD
    #CORRESPONDIENTE DE OCURRENCIAS, AL FINAL(CON EL SET) LO TRANSFORMO EN UN CONJUNTO PARA
    #ELIMININAR LAS REPETICIONES
    conjuntoFinal=(set(list(zip(listaInfinitivos,recuenciaPalab))))

    
    #TRANSFORMO EL CONJUNTO FINAL EN UN DICCIONARIO PARA PODER EXPORTARLO AL ARCHIVO JSON
    dic={}
    for elem in conjuntoFinal:
        palabra=elem[0]
        cantidad=elem[1]
        dic.setdefault(palabra,cantidad)

    #EXPORTO EL ARCHIVO
    with open('verbos.json','w') as archivoFinal:
        json.dump(dic,archivoFinal,indent=4)
 

def ejer4y5():
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
    5-
    ENUNCIADO:    
    En base al ejercicio anterior, guarde en un nuevo archivo las coordenadas
    y los colores (ya asociados) al presionar un botón "Guardar". ¿Cómo haría
    para almacenar la estructura completa en un archivo de texto plano?
    Implementarlo teniendo en cuenta la separación de las coordenadas y los 
    colores.
    """
    layout = [[sg.Text('Seleccione los archivos de Txt')],
              [sg.Text('Source for colores', size=(15, 1)), sg.InputText(), sg.FileBrowse(key='COLORES')],
              [sg.Text('Source for coordenadas', size=(15, 1)), sg.InputText(), sg.FileBrowse(key='COORDENADAS')],
              [sg.Button('Cargar'), sg.Cancel()],     
              [sg.Graph(canvas_size=(200,200), graph_bottom_left=(0, 0), graph_top_right=(150, 150), background_color='white', enable_events=True, key='graph')],
              [sg.Button('Guardar colores',visible=False)]
             ]
    window = sg.Window('Ejer4y5',layout)
    while True:
        event, values = window.read()
        if event is 'Cancel' or event is None:
            break
        if event is 'Cargar':   
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
                window['Guardar colores'].update(visible=True)    
            except FileNotFoundError:
                sg.popup('No se cargaron los archivos')
        # ejercicio 5
        if event is 'Guardar colores':    
            fieldnames = ['Coord X','Coord Y','Color']
            with open('coord.csv','w',newline = "") as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()    
                for i in lista:
                    coords = i[1].split(',')
                    writer.writerow({'Coord X': int(coords[0]),'Coord Y':int(coords[1]), 'Color': i[0]})


def ejer6():
    """
    6-
    ENUNCIADO:
    En base a los ejercicios anteriores, genere una ventana en la que se permita
    seleccionar un color de una lista (InputCombo, cargada desde el archivo de
    colores) y los valores de x e y de las coordenadas (con dos Slider). Al 
    presionar Añadir, deberá cargar los valores en una lista (Listbox). Añada un
    botón, que permita guardar la lista de colores/coordenadas en un archivo en 
    formato json.
    """
    layout1 = [[sg.Text('Seleccione los archivos de Txt')],
              [sg.Text('Source for colores', size=(15, 1)), sg.InputText(), sg.FileBrowse(key='COLORES')],
              [sg.Text('Source for coordenadas', size=(15, 1)), sg.InputText(), sg.FileBrowse(key='COORDENADAS')],
              [sg.Button('Cargar'), sg.Cancel()]]
    layout2 = [[sg.Text('SELECCIONE UN COLOR')],
              [sg.InputCombo('colores', size=(20, 1),key='_LIST_')],
              [sg.Text('SELECCIONE UNA COORDENADA DE X')],
              [sg.T('0',key='_LEFTX_'), sg.Slider((1,100), key='_SLIDERX_', orientation='h', enable_events=True, disable_number_display=True), sg.T('0', key='_RIGHTX_')],
              [sg.Text('SELECCIONE UNA COORDENADA DE Y')],
              [sg.T('0',key='_LEFTY_'), sg.Slider((1,100), key='_SLIDERY_', orientation='h', enable_events=True, disable_number_display=True), sg.T('0', key='_RIGHTY_')],
              [sg.Button('AÑADIR'),sg.Button('SALIR')],
              [sg.Text('VALORES AÑADIDOS')],
              [sg.Listbox('' , size=(50,10), key='-VALORES-', enable_events=True)],
              [sg.Button('GUARDAR VALORES')]
             ]
    layout = [
             [sg.Column(layout2,key = 'lay2', visible=False)],
             [sg.Column(layout1,key = 'lay1')]
             ]
    window = sg.Window('Ejer6',layout)
    choices = []
    while True:
        event, values = window.read()
        window['_LEFTX_'].update(values['_SLIDERX_'])  
        window['_RIGHTX_'].update(values['_SLIDERX_'])  
        window['_LEFTY_'].update(values['_SLIDERY_'])  
        window['_RIGHTY_'].update(values['_SLIDERY_'])  
        if event is 'Cancel' or event is None or event is 'SALIR':
            break
        if event is 'Cargar':   
            try:
                c = open(values[0],'r')
                x = open(values[1],'r')
                colores = c.read().split()
                coordenadas = x.read().split()
                window['lay1'].Update(visible=False)
                window['lay2'].Update(visible=True)
                window['_LIST_'].Update(values=colores)
            except FileNotFoundError:
                sg.popup('No se cargaron los archivos')
        if event is 'AÑADIR':
            col = values['_LIST_']
            x = int(values['_SLIDERX_'])
            y = int(values['_SLIDERY_'])
            cord = (x,y)
            choices.append({'Color':col,'Coordenadas X':cord[0],'Coordenadas Y':cord[1]})
            window['-VALORES-'].update(choices)
        if event == 'GUARDAR VALORES':
            with open('ejer6.json','w') as f:
                json.dump(choices,f,indent=4)      


'''
    Ejer 1 Practica 4
'''
#ejer1()

'''
    Ejer 2 Practica 4
'''
#ejer2()

'''
    Ejer 3 Practica 4
'''
#ejer3()
'''
    Ejer 4y5 Practica 4
'''
#ejer4y5()
'''
    Ejer 6 Practica 4
'''
ejer6()
