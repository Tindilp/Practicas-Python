
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
    # en lugar de elegir una a una , mezclo las opciones desde el principio 
    # para no ir eliminando en el proceso    
    random.shuffle(preguntas)
    for quest in preguntas:
        print(quest[0])
        ans = input('ingrese su respuesta: ')
        if ans.lower() == quest[1]:
            points+=1
            print('correcto')
        else:
            print('incorrecto')      
    print('Sumaste: ',points,' puntos')    

def ejer5():
    ok = True
    lista_numeros = []
    print('Bienvendio al menu')
    print('''Menu de opciones para la lista de numeros a ingresar: \n
             1: ingresar numeros \n
             2: ordenar numeros \n
             3: calcular el maximo \n
             4: calcular el minimo \n
             5: calcular el promedio \n
             0: para terminar''')           
    while( ok ):
        num = input('Ingrese la opcion elegida')
        if num == '1':
            num_add = input('Ingrese un numero para cargar en la lista')
            lista_numeros.append(int(num_add))
        elif num == '2':  
            lista_numeros = sorted(lista_numeros)
            print('Se ordeno la lista de numeros: ',lista_numeros)
        elif num == '3':
            try:
                print('El numero mas grande de la lista es: ',max(lista_numeros))
            except ValueError:
                print('Aun no hay numeros en la lista')    
        elif num == '4':  
            try:
                print('El numero mas chico de la lista es: ',min(lista_numeros))  
            except ValueError:
                print('Aun no hay numeros en la lista')  
        elif num == '5':
            try:
                print(sum(lista_numeros)/len(lista_numeros))
            except Exception:
                print('Aun no hay numeros en la lista')    
        elif num == '0': 
            ok = False  
            print('Adios!')            


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
    Ejer 4 Practica 2
'''
# preguntas = [['Buenos Aires limita con Santiago del Estero', 'no'], 
#            ['Jujuy limita con Bolivia', 'si'],
#            ['San Juan limita con Misiones', 'no']
#            ]
# ejer4(preguntas)            

'''
    Ejer 5 Practica 2
'''
# ejer5()