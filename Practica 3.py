def ejer2():
    """
    ENUNCIADO:
    Dado un texto generar una estructura que permita acceder directamente a una
    lista de palabras según la cantidad de caracteres de cada una. Es decir que
    cada palabra esté asociada al número de caracteres que tiene. Nota: las 
    palabras no tienen que estar repetidas, y se debe tener en cuenta 
    mayúsculas y minúsculas, espacios, comas y puntos.
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



ejer2()