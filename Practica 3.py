import random
from functools import reduce


def ejer2():
    """
        ENUNCIADO:
        Dado un texto generar una estructura que permita acceder directamente a
        una lista de palabras según la cantidad de caracteres de cada una. Es 
        decir que cada palabra esté asociada al número de caracteres que tiene.
        Nota: las palabras no tienen que estar repetidas, y se debe tener en 
        cuenta mayúsculas y minúsculas, espacios, comas y puntos.
    """
    frase = '''Si trabajas mucho CON computadoras, eventualmente encontrar as
            que te gustaria automatizar alguna tarea. Por ejemplo, podrias 
            desear realizar una busqueda y reemplazo en un gran numero DE 
            archivos de texto, o renombrar y reorganizar un monton de archivos
            con fotos de una manera compleja. Tal vez quieras escribir alguna 
            pequena base de datos personalizada, o una aplicacion especializada
            con interfaz grafica, o UN juego simple.'''
    frase = frase.lower().replace('.', '').replace(',', '')
    d = {}
    for each in frase.split(" "):
        d.setdefault(len(each), set()).add(each)
    print(d)         

def ejer3y7():
    """
        ENUNCIADO:
        3-
        Seleccione la estructura que considere más adecuada para almacenar la i
        nformación de varios usuarios ingresados desde teclado. Tener en cuenta
        que se necesita acceder a un usuario determinado en forma directa sin
        recorrerla.
        Con la estructura generada, imprimir los datos de un usuario dado sin 
        recorrerla estructura. ¿La elección sobre la estructura fue adecuada?
        ¿Cuál usó?

        Con la estructura generada en el ejercicio, imprimir sólo los nombres de
        los usuarios que jugaron sin recorrer la estructura.

        Dada la estructura generada en el ejercicio imprimir el usuario que 
        obtuvo mayor puntaje.
        Dada la estructura del ejercicio, ingresar los datos correspondientes a
        la jugada de un usuario. Si el usuario existe previamente, guardar los 
        datos de mayor puntaje.

        Luego imprimir el ranking de los 10 mejores puntajes. Nota: utilizar 
        una expresión lambda para ordenar el diccionario.
        
        ENUNCIADO:
        7-
        Utilizar como estructura de datos de referencia la generada en el 
        ejercicio 3 y generar funciones que ejecuten lo siguiente:
        
        (a) Imprimir los 10 primeros puntajes de la estructura.
        
        (b) Imprimir los datos de los usuarios ordenados alfabéticamente por
        apellido.
        
        (c) Imprimir los datos de los usuarios ordenados por nivel alcanzado.
         Nota: utilice expresiones lambda para resolver los incisos.
    """

    def remplazar(palabra,num):
        car=' '+palabra[num]+' '
        for i in palabra:
            palabra = palabra.replace(i,'-',1)
        print (palabra[:num] + car +  palabra[num + 1:])
        # palabra[:num] indica  la posicion del nuevo caracter
        # palabra[num + 1:], se remplaza con el caracter guardado PREGUNTAR! 

    jugadores = {
            'Tomy':{"Puntaje":10, "Nivel":5, "Tiempo":2},
            'Dani':{"Puntaje":45, "Nivel":2, "Tiempo":200},
            'Celes':{"Puntaje":100, "Nivel":3, "Tiempo":70},
            'Sumi':{"Puntaje":3, "Nivel":7, "Tiempo":30},
            'Fili':{"Puntaje":15, "Nivel":5, "Tiempo":2},
            'Tindi':{"Puntaje":200, "Nivel":2, "Tiempo":200},
            'Kuro':{"Puntaje":120, "Nivel":3, "Tiempo":70},
            'Pepe':{"Puntaje":300, "Nivel":7, "Tiempo":30},
            'Toti':{"Puntaje":35, "Nivel":5, "Tiempo":2},
            'Tina':{"Puntaje":80, "Nivel":2, "Tiempo":200},
            'Mini':{"Puntaje":170, "Nivel":3, "Tiempo":70},
            'Fede':{"Puntaje":50, "Nivel":7, "Tiempo":30},
          }

    # Con la estructura generada, imprimir los datos de un usuario dado sin 
    # recorrer la estructura. ¿La elección sobre la estructura fue adecuada?
    # ¿Cuál usó?'''
    print(jugadores['Celes'])

    # Con la estructura generada en el ejercicio, imprimir sólo los nombres 
    # de los usuarios que jugaron sin recorrer la estructura.
    print(jugadores.keys())      

    # En un diccionario ¿cómo obtenemos todos los datos, keys y sus valores?
    print(jugadores.items())

    # Dada la estructura generada en el ejercicio imprimir el usuario que obtuvo
    # mayor puntaje
    # ordenando la lista por puntaje e imprimir el último elemento,
    jugadores_or = sorted(jugadores.items(),key=lambda jugador: jugador[1]['Puntaje'])
    print('maximo!!! ', jugadores_or[-1:])

    # Dada la estructura del ejercicio, ingresar los datos correspondientes a 
    # la jugada de un usuario. Si el usuario existe previamente, guardar 
    # los datos de mayor puntaje.
    print('JUGADORES SIN MODIFICAR: ',jugadores)
    nombre_jugador = input("Ingrese nombre del Jugador de la jugada: ")
    puntaje_jugada = input("Ingrese puntaje de la jugada de {nombre_jugador}: ")
    if nombre_jugador in jugadores.keys():
        jugador = jugadores[nombre_jugador]
        jugador['Puntaje'] = max(jugador['Puntaje'], int(puntaje_jugada))
    print('JUGADORES MODIFICADOS: ',jugadores)
    
    # Para agregar un jugador nuevo podemos utilizar setdefault'
    print('JUGADORES TOTALES: ',jugadores)
    nombre_jugador = input("Ingrese nombre del Jugador de la jugada: ")
    puntaje_jugada = input("Ingrese puntaje de la jugada de {nombre_jugador}: ")
    nivel_jugada = input("Ingrese nivel de la jugada de {nombre_jugador}: ")
    tiempo_jugada = input("Ingrese tiempo de la jugada de {nombre_jugador}: ")
    juga_nuevo = {'Nivel': int(nivel_jugada), 'Puntaje': int(puntaje_jugada), 'Tiempo': int(tiempo_jugada)}
    jugadores.setdefault(nombre_jugador,juga_nuevo)
    print('JUGADORES CON NUEVOS: ',jugadores)
    
    # Luego imprimir el ranking de los 10 mejores puntajes
    jugadoresXL_or = sorted(jugadores.items(), key=lambda punt: punt[1]['Puntaje'],reverse=True)
    print('===== TOP TEN =====')
    print(jugadoresXL_or[:10])

    # Parte del Ejercicio 7

    # Imprimir los 10 primeros puntajes de la estructura.
    print('++++++++++++++++++  EJER 7 1 ++++++++++++++++++++++')
    result=list(map(lambda x: ["key {}, value {} ".format(x,  jugadores[x])], jugadores))[0:10]
    print(result)

    print('++++++++++++++++++  EJER 7 2  ++++++++++++++++++++++')
    # Imprimir los datos de los usuarios ordenados alfabéticamente por apellido.
    jugadores_nom = sorted(jugadores.items(), key=lambda punt: punt)
    print(jugadores_nom)

    print('++++++++++++++++++  EJER 7 3  ++++++++++++++++++++++')
    # Imprimir los datos de los usuarios ordenados por nivel alcanzado.
    jugadores_nivel = sorted(jugadores.items(), key=lambda punt: punt[1]['Nivel'])
    print(jugadores_nivel)

def ejer4():
    """
        ENUNCIADO:
        Dado el siguiente diccionario donde las claves son nombres de animales 
        y los valores representan posiciones:
        anim={’Gato Montes’:2,’Yacare overo’:4,’Boa acuática’:5}
        Imprimir un string por cada animal de la estructura, reemplazando sus 
        caracteres por el string ’_ ’ (inclusive los espacios en blanco) salvo 
        el carácter correspondiente al valor del mismo.
    """
    def remplazar(palabra,num):
        car=' '+palabra[num]+' '
        for i in palabra:
            palabra=palabra.replace(i,'-',1)
        print (palabra[:num] + car +  palabra[num + 1:])
        #palabra[:num] indica  la posicion del nuevo caracter
        #palabra[num + 1:], se remplaza con el caracter guardado PREGUNTAR!

    anim={'Gato Montes':2,'Yacare overo':4,'Boa acuatica':5}
    for key in anim:
        print  (key, ':' , anim[key])
        remplazar(key,anim[key])
 
def ejer5y6():
    """
        ENUNCIADO:
        5-
        Generar una estructura que contenga coordenadas y un color asociado.
        La forma de asociar las coordenadas con el color debe ser aleatoria sin
        importar que se repitan los colores elegidos.

        Generar una estructura que contenga coordenadas y un color asociado. La
        forma de asociar las coordenadas con el color debe ser aleatoria sin que
        se repitan los colores.
        
        6-
        Usando el diccionario del Ejercicio 5, acceder a las coordenadas (x,y) 
        y, según el color asociado, ejecutar una función asociada a la misma. 
        Las funciones pueden plantear la resolución de ejercicios simples como 
        ser:
        
        (a) Suma de dos números que se generen en forma aleatoria cada vez que 
        se llama a la función, reciba el resultado por teclado y verifique el 
        resultado.
        
        (b) Dada la estructura que contiene palabras clasificadas según su 
        acentuación:
    """

    def sumar(): 
        num1 = random.randrange(0,100)
        num2 = random.randrange(0,100)
        resultado=int(input('cual es resultado de sumar {} y {} ? ingrese el resultado: '.format(num1,num2)))
        if (num1+num2 == resultado):
            print('resultado correcto')
        else:  
            print('resultado incorrecto')

    def tipoPalabra():
        palabras = [('grave',['molesto']), ('aguda',['raton']), ('esdrujula',['murcielago'])]
        num3 = random.randrange(0,len(palabras))
        tipo=input('La palabra {} es grave, aguda, o esdrujula? Ingrese la respuesa: '.format(palabras[num3][1]))
        if (tipo==palabras[num3][0]):
            print ('correcto')
        else:
            print('incorrecto')
    
    colores = ['azul','amarillo','rojo','blanco','negro']
    coordenadas = [(2,3),(5,6),(8,8),(10,2),(-5,-8)]
    coord2 = coordenadas.copy()
    lista = []
    dic = {}

    for i in range(len(colores)):
        num = random.randrange(0,len(colores))
        num2 = random.randrange(0,len(coordenadas))
        tupla = (colores[num],coordenadas[num2])
        coordenadas.remove(coordenadas[num2])
        lista.append(tupla)
    print(lista)

    for i in range(len(coord2)):
        num = random.randrange(0,len(coord2))
        tupla = (colores[i],coord2[num])
        dic[coord2[i]] = colores[num] 
    print(dic)  

    color=dic[(2, 3)]
    # fijate como podes simplificar todo esto, te doy una pista funciones = {'negro' = sumar, 'amarillo' = tipoPalabra}
    if (color in {'negro','azul'}): sumar()
    elif(color in {'amarillo','rojo','blanco'}): tipoPalabra()

def ejer8():
    """
        ENUNCIADO:
        Definir dos funciones que reciban una cantidad variable de argumentos:
        a) una función que puede llegar a recibir hasta 30 números como 
        parámetros y debe devuelva la suma total de los mismos
        b) otra función que reciba un número variable de parámetros nombrados 
        (usar **kwargs), e imprima dichos parámetros. De antemano no se sabe 
        cuáles de los siguientes tres posibles parámetros se reciben:
        nombre apellido sexo
    """
    def sumar(*args):
        print(reduce(lambda x,y: x+y, list(args)))

    def mostrarParametros(**kwargs):
        [print(x) for x in kwargs]
      
    sumar(23,3,4,56,7,8,9,10,77,89)
    mostrarParametros(nombre = 'pepe',apellido = 'diaz',sexo = 'hombre',apellido2='dss')

def ejer9(*args):
    """
        ENUNCIADO:
        Escribir una función que reciba una cantidad variable de argumentos 
        correspondientes a nombres de personas e imprima por pantalla los 
        nombres enumerándolos.
        Nota: consultar el uso de enumerate.
    """
    [print(name) for name in enumerate(args,0)]

def ejer10(operador,*args,**kwargs):
    """
        ENUNCIADO:
        Escribir una función que reciba al menos un argumento y opcionalmente
        una lista de argumentos variables y una lista de argumentos con nombre.
        El argumento fijo deberá ser la operación que se desea hacer con lista
        de números que se reciba como variable y los argumentos con nombre 
        corresponden a los datos de la persona que solicitó la operación. Las 
        operaciones posibles son: “+” y “*”. Los datos con nombre variables 
        pueden ser: nombre, apellido y dirección. 
        Nota: investigar la función reduce del módulo functools.
    """
    if (operador=='+'):
         print('El resultado es: ', reduce(lambda a, b: a+b, *args),' La operacion la solicito ', kwargs['nombre'],kwargs['apellido'] ) 
    else:
         print('El resultado es: ', reduce(lambda a, b: a*b, *args),' La operacion la solicito ', kwargs['nombre'],kwargs['apellido'] )
      
'''
    Ejer 2 Practica 3
'''
# ejer2()

'''
    Ejer 3 Practica 3
'''
# ejer3y7()

'''
    Ejer 4 Practica 3
'''
# ejer4()

'''
    Ejer 5 y 6 Practica 3
'''
# ejer5y6()

'''
    Ejer 8 Practica 3
'''
#ejer8()

'''
    Ejer 9 Practica 3
'''
#ejer9("Dani 1","Tomy 2","Lucas 3")

'''
    Ejer 10 Practica 3
'''
#ejer10("*",[1,2,3,4,5],nombre='Lucas',apellido='Di Lorenzo')


