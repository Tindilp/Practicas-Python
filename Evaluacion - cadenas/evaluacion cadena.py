def calcular_caracteres_unicos(palabra):
    '''
    Recibe un string  y retorna una lista con los caracteres que aparecen una 
    única vez en el string.
    'Ejemplo: calcular_caracteres_unico("CASA") devuelve ["C","S"] dado que 
    aparecen una sola vez en el string "CASA
    "'''
    lista = []
    pal = palabra.upper()
    for i in pal:
        if pal.count(i) == 1 :
            lista.append(i)
    return lista

def gen_informacion(lista):
    '''
    Recibe una lista de strings y retorna una lista de tuplas con la cantidad
    de caracteres únicos del string y el string en mayúscula, se debe utilizar 
    la función calcular_caracteres_unicos().
    Ejemplo:
    gen_informacion(["CASA","gato"]) devuelve [(2,"CASA"),(4,"GATO")]
    '''
    list = []
    for i in lista:
        i = i.upper()
        tuple = (len(calcular_caracteres_unicos(i)),i)
        list.append(tuple)
    return list    

def ordenar_informacion(lista,criterio):
    '''
    Recibe una lista de datos procesados (generados por la función 
    gen_informacion) y un criterio de ordenamiento:
    Si el Criterio es igual a "cantidad" se debe retornar la lista ordenada por
    el valor numérico.
    Si el Criterio es igual a "palabra" se debe retornar la lista ordenada por
    la palabra alfabéticamente.
    Si se ingresa cualquier otra cosa, se debe imprimir "No se ingresó un 
    criterio válido" y se debe terminar
    obligatoriamente la ejecución de todo el programa.
    '''
    if criterio == 'cantidad': return sorted(lista, key=lambda tup: tup[0])
    elif criterio == 'palabra': return sorted(lista, key=lambda tup: tup[1])
    else: return 'No se ingreso un criterio valido'

def calcular_max_palabra(lista):
    '''
    Recibe una lista de datos procesados(generados por la función 
    gen_informacion) y retorna la tupla con la palabra con la mayor cantidad 
    de caracteres únicos.
    '''
    return max(lista)

def calcular_min_palabra(lista): 
    '''
    Recibe una lista de datos procesados(generados por la función
    gen_informacion) y retorna la tupla con la menor cantidad de caracteres
    únicos.''' 
    return min(lista)

print(calcular_caracteres_unicos('casa'))
lista = gen_informacion(["CASA","peRro",'agua','bar','gato'])
print(ordenar_informacion(lista,'palabra'))
print(calcular_max_palabra(lista))
print(calcular_min_palabra(lista)) 