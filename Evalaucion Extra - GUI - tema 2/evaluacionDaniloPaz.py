import PySimpleGUI as sg
import json
import os

datos = []

layout = [[sg.InputText(key="_nombre_")], [sg.Button("promedio")], [
    sg.Button("maximo")], [sg.Button("guardar")], [sg.Button("mostrar")], [sg.Button("ok")]]
window = sg.Window("Ingrese el nombre  y pulse ok").Layout(layout)

while True:
    event, values = window.Read()
    if event == "salir" or event == None:
        break
    if event == "ok" and bool(values["_nombre_"]):
        '''
        ruta = 'datos_aulas.json'
        print(ruta)
        with open(ruta, "r") as arc:'''
        with open('/Users/lucasdilorenzo/Desktop/Evaluacio\u0301n extra 2/datos_aulas.json','r') as arc:
            dic = json.load(arc)
    elif event == "promedio" and bool(values["_nombre_"]):
        cont = 0
        for value in dic.items():
            cont += int(value[1]["temp"])
        sg.Popup("Temperatura promedio -->", cont//len(dic.keys()))
    elif event == "maximo" and bool(values["_nombre_"]):
        ord = sorted(dic.items(), key=lambda x: x[1]['temp'], reverse=True)
        sg.Popup(ord[0])
    elif event == "mostrar" and bool(values["_nombre_"]):
        layout2 = [[sg.Listbox(values=datos, size=(55, 20), key="_datos_")]]
        window2 = sg.Window("List").Layout(layout2)
        for k, v in dic.items():
            datos.append((k, v))
        event2, values2 = window2.Read()
    elif event == "guardar" and bool(values["_nombre_"]):
        try:
            with open("datos.txt", "a+") as text:
                for k, v in dic.items():
                    text.write(k+" "+str(v)+" ")
        except FileNotFoundError:
            val = sg.popup_yes_no("Archivo no encontrado,quiere generar uno?")
            print(val)
            if val == "yes":
                with open("datos.txt", "w") as arc:
                    for k, v in dic.items():
                        text.write(k+" "+str(v)+" ")
            else:
                break
window.close()
