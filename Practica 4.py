import PySimpleGUI as sg
import json

def ejer1():
    """
        ENUNCIADO:
        Diagrame una interfaz en PySimpleGUI que permita ingresar dos datos: 
        temperatura y humedad, junto con la fecha y hora actual. Al presionar
        Añadir , deberá cargar los valores en una lista (Listbox). Añada un
        botón, que permita guardar esta información en un archivo en formato
        json.
    """
    layout = [
                [sg.Text('Temperatura'),sg.InputText('',key = 'temp')],
                [sg.Text('Humedad'),sg.Input('',key = 'humed')],
                [sg.Button('Añadir'),sg.Button('Salir')],
                [sg.Listbox('',size=(50,20),key='lista')]
             ]
    window = sg.Window('Ejer 1',layout)    
    while True:
        event, values = window.read()
        if event is None or event is 'Salir':
            break
        if event is 'Añadir':
            linea = 'Temperatura: ',values['temp'], 'Humedad: ',values['humed']
            window['lista'].update(values=linea)
            window['lista']



ejer1()