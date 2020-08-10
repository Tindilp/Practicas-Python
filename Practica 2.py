
import random
from collections import Counter

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

def ejer6():
    ok = True
    print('''Bienvendio al menu \n
    Primero ingresa dos numeros''')
    num1 = int(input ('Ingresa el numero 1: '))         
    num2 = int(input ('Ingresa el numero 2: '))  
    print('''Menu de opciones para realizar operaciones sobre esos dos numeros: \n
             1: para sumar \n
             2: para restar \n
             3: para multiplicar \n
             4: para dividir \n
             0: para terminar''')      
    while( ok ):
        opc = input('Ingrese la opcion elegida: ')
        if opc == '1': print('La suma da un total de', num1+num2)
        elif opc == '2': print('La resta da un total de', num1-num2)
        elif opc == '3': print('La multiplicacion da un total de', num1*num2)
        elif opc == '4': 
            try:
               print('La division da un total de', num1/num2)  
            except Exception:
                print('numero 2 no puede ser 0, vuelva a iniciar')
                break   
        elif opc == '0':
            ok = False 
            print('Adios!')            

def ejer7():
    texto = input('Ingrese una palabra para ver si es palindromo: ')
    if texto.lower() == texto.lower()[::-1]: print(' Es palindromo')
    else: print(' NO es palindromo')

def esPrimo(num):
  if num < 2:# si es menos que 2 no es primo, por lo tanto devolverá Falso
    return False
  for i in range(2,num): # un rango desde el dos hasta el numero que nosotros elijamos
    if num % i == 0:# si el resto da 0 no es primo, por lo tanto devuelve Falso
      return False
  return True # de lo contrario devuelve Verdadero

def ejer8():
    texto = 'Python es genial'
    c = Counter(texto.lower())
    print(c)
    for key in c:
        num = c[key]
        if esPrimo(num):
            print ('El caracter: ',key, ' aparece ', c[key], ' veces - El numero: ', c[key], "es primo")

def ejer9():
    intentos = 0

    print('Hola! cual es tu nombre?')
    mi_nombre = input()

    number = random.randint(1, 50)
    print('Bueno, ' + mi_nombre + ', estoy pensando un numero entre 1 y 50!')

    for intentos in range(6):
        print('Intentan adivinar cual es.') # Four spaces in front of "print"
        print('Intento numero: ',intentos)
        guess = input()
        guess = int(guess)
            
        if guess < number:
            print('Tu intento es muy bajo.') # Eight spaces in front of "print"

        if guess > number:
            print('Tu intento es muy alto.')

        if intentos==2:
            if number%2==0:print('PISTA ADICIONAL: ES PAR.')
            else:print('PISTA ADICIONAL: ES IMPAR.') 

        if guess == number:
            break

    if guess == number:
        intentos = str(intentos + 1)
        print('Bien, ' + mi_nombre + '! Adivinaste el numero en ' +
                intentos + ' intentos!')

    if guess != number:
        number = str(number)
        print('Nope. El numero en el que pensaba era el ' + number + '.')

def ejer10():
    imagenes=['im1','im2','im3']
    imagenesCord=[]
    for i in range(3):
        print('ingrese x: ')
        x=input()
        print('ingrese y: ')
        y=input()
    while y==x:
        print('El numero ingresado es el mismo que en x, POR FAVOR INGRESE OTRO')
        y=input()
        cords=imagenes[i]+ ': (' + x + ',' + y + ')'
        imagenesCord.append(cords)
    
    #imprimo el resultado
    for w in imagenesCord:
        print(w)

  
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

'''
    Ejer 6 Practica 2
'''
# ejer6()

'''
    Ejer 7 Practica 2
'''
# ejer7()

'''
    Ejer 8 Practica 2
'''
# ejer8()

'''
    Ejer 9 Practica 2
'''
# ejer9()

'''
    Ejer 10 Practica 2
'''
ejer10()