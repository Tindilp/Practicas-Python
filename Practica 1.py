'''
    Ejer 1 - Probamos el split el cual elimina el caracter de una cadena de 
    caracteres
'''
# texto = ' Esto es un texto con agrego numeros y espacio al principio / 4567813312/ / espacio' 
# text2 = texto.split('/')
# print (text2)


'''
    Ejer 1 - Probamos el strip el cual elimina los espacios al final y 
    comienzo de una cadena de strings
'''
# texto = '''     En la cursada vamos a trabajar con Python 3.6 '''
# text2 = texto.strip()
# print (text2)

'''
     Ejer 1 - Probamos el join 
'''
# texto = ' Esto es un texto con agrego numeros y espacio al principio / 4567813312/ / espacio'
# print('@'.join(texto)) 
# text2 = texto.split('/')
# print (text2)
 
# conj={'1','2','3','u','cancion'} 
# print(', '.join(e for e in conj))


'''
    ejer 2. 1 con for
'''
# text= 'cadena para testeo de string'
# list=[]
# for pal in text.split():
#    list.append(pal)
# print(list)    


'''
    ejer 2. 1 con map
'''
# utilizo el map y lambda para generar lo mismo que con el for, el map genera 
# una lista, y lleva dos operadores , en este caso "lambda x: x" es uno y el 
# otro es el "text.split()". Entonces el segundo elemnto es el elemento sobre
# el cual se va a iterar, en este caso es la cadena "texto", pero dividida en 
# palabras por eso esta el "split()"
# En cuanto al primer elemento, en general se pone una funcion, pero el lambda
# trabaja como una funcion rapida, es para una asignacion rapida de cada elemento
# de texto a la lista que genera MAP
# Al final para impirmirlo, result se castea tipo "list" en caso que no se haga
# eso se impimira un objeto

# text= 'cadena para testeo de string'
# result = map(lambda x: x, text.split())
# print(list(result))

'''
    Ejer 2. 2
'''
# frase='esto es una frase'
# teclado='test dsds'
# result = list(map(lambda x: x, frase.split()))
# result.append(teclado)
# print(len(result))

'''
    Ejer 2. 3
'''
# text= 'cadena para testeo de string'
# result = list(map(lambda x: x, text.upper().split()))
# print(result)
    
'''
    Ejer 2. 5
'''    
# frase= 'Esto es UNA frase Frase para probara algo, para testear. es un Ejercicio ES esto'
# result = list(set(map(lambda x: x, frase.lower().split())))
# print(result)

