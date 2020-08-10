
import random

def ejer1(tam):
    list1, list2 = [], []
    num = int(input('ingrese un numero: '))
    for pal in tam:
        if int(pal.split()[1].split(',')[0]) < num:
            list1.append(pal)
        else:
            list2.append(pal)    
    return list1, list2

def ejer2(tam):
    result = list(map(lambda x: tuple(x.split()[1].split(',')), tam))
    result2 = sorted(list(map(lambda x: (int(x[0]),int(x[1])), result)))
    return result2

def ejer3(lista):
    '''
        Filtro los elemtos que son decimales de la lista:
            - El isDecimal() me devuelve true o false si el string es un numero
            - Con el Filter generamos la lista reducida con los elementos decimales
              que son los que dan como resultado TRUE en el isDecimal()
            - Luego con el map, pasamos todos los elementos de la lista de string a
              entero, y ordenamos la lista
            (todo estos se puede hacer en una linea, pero es mas legible en dos)     
    '''
    filterList= list(filter(lambda x: x.isdecimal(), lista ))
    aEntero = sorted(list(map(lambda x: int(x), filterList)))
    return aEntero

def ejer4(preguntas):
    points = 0

    for quest in range(len(preguntas)):
        indice = random.randrange(len(preguntas))
        print(quest[0])
        ans = input('ingrese su respuesta: ')
        if ans.lower() == ques[1]:
            points+=0
        else:
            print('incorrecto')
        del preguntas[indice]        

    print(points)    

    


'''
    Ejer 1 Practica 2
'''
# tam = ['im1 4,14', 'im2 33,15', 'im3 6,34', 'im4 410,134']
# list1, list2 = ejer1(tam)
# print('Ejer 1 - list 1: ',list1, 'list 2: ' , list2)

'''
    Ejer 2 Practica 2
'''
# list3 = ejer2(tam)
# print('Ejer 2 : ', list3)

'''
    Ejer 3 Practica 2
'''
# lista = ['Auto', '123', 'Viaje', '50', '120']
# list4 = ejer3(lista)
# print('Ejer 3 : ', list4)

'''
    Ejer 1 Practica 2
'''
preguntas = [['Buenos Aires limita con Santiago del Estero', 'no'], 
            ['Jujuy limita con Bolivia', 'si'],
            ['San Juan limita con Misiones', 'no']
            ]
ejer4(preguntas)            
