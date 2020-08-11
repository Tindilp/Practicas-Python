import random

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

def ejer3():
    """
        ENUNCIADO:
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
    juga_nuevo = {'Nivel': nivel_jugada, 'Puntaje': puntaje_jugada, 'Tiempo': tiempo_jugada}
    jugadores.setdefault(nombre_jugador,juga_nuevo)
    print('JUGADORES CON NUEVOS: ',jugadores)
    
    # Luego imprimir el ranking de los 10 mejores puntajes
    jugadoresXL_or = sorted(jugadores.items(), key=lambda punt: punt[1]['Puntaje'],reverse=True)
    print('===== TOP TEN =====')
    print(jugadoresXL_or[:10])

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
        palabras = [('grave',['molesto']), ('aguda',['ratón']), ('esdrujula',['murciélago'])]
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

'''
    Ejer 2 Practica 3
'''
# ejer2()

'''
    Ejer 3 Practica 3
'''
# ejer3()

'''
    Ejer 4 Practica 3
'''
# ejer4()

'''
    Ejer 5 y 6 Practica 3
'''
ejer5y6()
5