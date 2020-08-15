from functools import reduce

def es_colega(numeros):
    return len(numeros) != len(set(numeros))
    

def es_primo(num):
    num=int(num)  
    # si es menos que 2 no es primo, por lo tanto devolverá Falso
    if num < 2:
        print('salio por aca')
        return False
    # un rango desde el dos hasta el numero que nosotros elijamos    
    for i in range(2,num):
        # si el resto da 0 no es primo, por lo tanto devuelve Falso
        if num % i == 0:
            return False
    # de lo contrario devuelve Verdadero        
    return True 


def es_capicua(numeros):   
    return numeros == numeros[::-1]


def suma_es_primo(numero):
    nums = list(map(lambda a:a,numero))
    return es_primo((reduce(lambda a,b : int(a)+int(b), nums)))


def get_informacion(lista_numeros):
    numeros = lista_numeros.split()
    print (numeros)
    dic = {}
    for i in numeros:
        if es_colega(i):
            dic[i]={'Es capicua?: ':es_capicua(i),'es Primo?: ':suma_es_primo(i)}
    return dic      


ok = False
while not ok:
    numeros = input('Ingrese un numero:')
    try:
        # intentamos transformarlo a int para ver si el numero ingresado es un
        # numero
        int(numeros)
        ok = True
    except ValueError:
        print('El numero ingresado es incorrecto')

print('Es Colega?--->',es_colega(numeros))
print('Es Primo?---->',es_primo(numeros))
print('Es Capicua?-->',es_capicua(numeros))

lista_numeros = '111 4334 334 4 5 773'
print('Obtener informacion: \n',get_informacion(lista_numeros))