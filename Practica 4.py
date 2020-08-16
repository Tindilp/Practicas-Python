import PySimpleGUI as sg
import json
import time
from datetime import datetime

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
#ejer2()

