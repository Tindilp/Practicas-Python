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

'''
    Ejer 2 Practica 3
'''
#ejer2()

'''
    Ejer 3 Practica 3
'''
#ejer3()