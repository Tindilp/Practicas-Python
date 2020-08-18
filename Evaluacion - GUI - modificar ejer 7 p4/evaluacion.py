import csv
import PySimpleGUI as sg

col_mujeres = 10 # la columna en que se encuentran la cantidad de mujeres es la 10
col_universidad = 2 # la columna en que se encuentran la universidad es la 2
col_varones = 9 # la columna en que se encuentran la cantidad de hombres es la 9

def ordenar_diccionario(dic): #retorna lista ordenada.
    return sorted(dic.items(), key=lambda item: item[1], reverse= True)


def abrir_procesar(ruta):
    global col_mujeres
    global col_universidad
    with open(ruta,'r', encoding='utf8') as arch:
        csv_reader = csv.reader(arch,delimiter=',',quotechar = '"')
        next(arch)
        dic = {}
        for row in csv_reader:
            # vamos a recoorer todo el archivo guardando datos
            # primero guardo la universidad actual.
            universidad_actual = row[col_universidad] 
            # luego la cantidad de mujeres de esa univeridad
            # Sí el lugar de cant mujeres tiene '' -> cantMujeres = 0. sino, retorno la cantidad
            mujeres_actual = (int(row[col_mujeres])if row[col_mujeres] != '' else 0)
            # luego la cantidad de hombres de esa univeridad
            # Sí el lugar de cant varones tiene '' -> cantVarones = 0. sino, retorno la cantidad
            varones_actual = (int(row[col_varones])if row[col_varones] != '' else 0)

            #Sí la universidad no existe en el diccionario, la agregamos
            if universidad_actual not in dic:
                dic[universidad_actual] = [mujeres_actual,varones_actual]
            #sino, la actualizamos con las cantidades guardadas
            else:
                dic[universidad_actual][0] += mujeres_actual
                dic[universidad_actual][1] += varones_actual
    lista_ordenada = ordenar_diccionario(dic)
    return lista_ordenada


layout = [ [ sg.Text('INGRESE EL NOMBRE DEL ARCHIVO:')],
           [ sg.InputText(key='nombre_archivo')],
           [ sg.Button('Cargar'),sg.Button('Salir')],
           [ sg.Button('Mostrar ordenado',key= '-ORDENAR-',disabled=True)],
           [ sg.Listbox(values='',size = (60,20),key = '-LISTA-',enable_events=True)]
         ]
window = sg.Window('ejer7',layout)   
while True:
    event , values = window.read() 
    if event is 'Salir' or event is None:
        break 
    if event is 'Cargar':
        name = values['nombre_archivo']
        try:
            lista_ordenada = abrir_procesar(name)
            window['-ORDENAR-'].update(disabled=False)
        except FileNotFoundError:
            sg.popup("no fue encontrado tal archivo")    
    if event is '-ORDENAR-':
        window['-LISTA-'].update(map(lambda x: "{}: {}".format(x[0], (str(x[1][0]) + ', ' + str(x[1][1]))),lista_ordenada))