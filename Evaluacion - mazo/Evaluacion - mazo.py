import random
from functools import reduce


def armar_mazo(palos,valores):
    mazo = []
    for i in palos:
        for j in valores:
            carta=(i,j)
            mazo.append(carta)  
    return mazo


def armar_mano(mazo,jugadores):
    random.shuffle(mazo)
    dic={}
    for i in jugadores:
        mano = []
        for j in range(3):
            mano.append(mazo[j])
        for k in mano:
            mazo.remove(k)    
        dic[i] = mano
    return dic


def mayor_valor(manos):
    max = 0
    for i in manos:
        puntos = 0
        for j in manos[i]:
            puntos +=j[1]   
        if puntos > max:
            max = puntos
            nom = i       
    return (nom, max)  

def repite_palos(mano):
    d = {}
    # recorro el dic en forma de lista
    for key, value in mano.items():
        ls = []
        # accedo a los elementos de la lista y los voy agregando a una lista
        for element in value:
            ls.append(element[0])
        # luego comparamos el tamaño de la lista, con el tamaño de la lista 
        # aplicando el set.    
        # Set elimina repetidos asi que si son diferentes es xq habia palos 
        # iguales
        if (len(ls) != len(set(ls))):
            d[key] = "tiene repetidos"
        else :   
            d[key] = "NO tiene repetidos"
    return d


palos=['basto','espada','oro','copa']
valores=[1,2,3,4,5,6,7,8,9,10]
mazo = armar_mazo(palos,valores)
print(mazo)

jugadores=['pepe','lucas','raul']
manos = armar_mano(mazo,jugadores)
print(manos)


mayor = mayor_valor(manos)
print( mayor)

repetido = repite_palos(manos)
print (repetido)