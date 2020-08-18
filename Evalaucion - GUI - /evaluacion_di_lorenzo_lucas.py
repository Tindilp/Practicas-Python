import PySimpleGUI as sg
import json
import time
from datetime import datetime

"""
Diagrame una interfaz en PySimpleGUI que permita realizar el alta de datos: 
número de aula (numérico), temperatura y humedad, junto con la fecha y hora
actual. La fecha y hora actual se debe añadir desde el código en forma 
automática y no en un campo de input. Realizar las siguientes acciones: 

Añada a la interfaz un botón que permita guardar esta información en un archivo
existente en formato json ordenado de menor a mayor por temperatura.
Se debe agregar la información a los datos que contiene el archivo.

Se debe capturaruna excepción si no existe el archivo (FileNotFoundError).
Al producirse esta situación se debe mostrar un mensaje con la excepción 
capturada en una ventana popup de PySimpleGUI, dando la posibilidad de poder generarlo.

El nombre del archivo que se guarda deberá llamarse “datos_aulas.json” y 
deberá guardarse de forma que permita acceder a través del número de aula 
directamente a los datos correspondientes. Cada número de aula podrá tener
solo una instancia de datos asociado.
"""

def limpiar_pantalla(window,datos):
    with open('datos_aulas.json','w') as arch:             
            json.dump(datos, arch,indent=4)
    sg.popup('Cambios Realizados')
    window['aula'].Update('')  
    window['temp'].Update('')  
    window['humed'].Update('')  


layout = [
            [sg.Text('Nro de Aula'),sg.InputText('',key = 'aula')],
            [sg.Text('Temperatura'),sg.InputText('',key = 'temp')],
            [sg.Text('Humedad'),sg.Input('',key = 'humed')],
            [sg.Button('Añadir'),sg.Button('Salir')],
]

window = sg.Window('examen',layout)
now = datetime.now() 
dic={}  
ok = True
try:
    with open('datos_aulas.json','r') as file:
        datos=json.load(file)     
except FileNotFoundError:
    valor = sg.popup_yes_no('El archivo no existe, desea crearlo?')
    if valor == 'Yes':
        with open('datos_aulas.json','w') as file:
            json.dump(dic,file)
            datos={}
        ok = True    
    else:
        sg.popup('Salio del programa')
        ok = False            

while True and ok:
    now = datetime.now()
    event, values = window.read()

    if event is None or event is 'Salir':
        break
    if event is 'Añadir':
        fec_y_hora = '{}/{}/{}, {}:{}'.format(now.day,now.month,now.year, now.hour,now.minute)
        try:
            num_aula = int(values['aula']) 
            if values['aula'] in datos.keys():
                sg.popup('El aula existe, se van a realizar los cambios')
                aula = num_aula
                aula['temp'] = values['temp']
                aula['humedad'] = values['humed']
                aula['fecha'] = fec_y_hora
                limpiar_pantalla(window,datos)  
            else:
                sg.popup('El aula no existe, se cargaran sus datos')
                try:
                    aula_nueva = {'temp: ':values['temp'], 'humedad: ':values['humed'], 'fecha:':fec_y_hora}
                    datos.setdefault(values['aula'],aula_nueva)    
                    limpiar_pantalla(window,datos)
                except ValueError:
                    sg.popup('Faltan ingresar datos para el jugador nuevo o hay datos invalidos')      
        except ValueError:
            sg.popup('el numero de aula es invalido, por favor ingreselo de nuevo')
            
        