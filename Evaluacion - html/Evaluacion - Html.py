def procesar_button(texto):
	# eliminamos la parte '</button>' del string recibido x parametro
	texto = texto.strip('</button>')
	# eliminamos la parte '<div class="navbar-next">' del string recibido por
	# parametro
	texto = texto.strip('<div class="navbar-next">')
	# eliminamos los blancos ' ' del string recibido x parametro
	texto = texto.strip()
	# generamos una lista con elementos separados por blancos
	separar = texto.split(' ')
	# generamos un diccionario vacio
	diccionario = {}
	# vamos a iterar sobre los elementos de la lista
	for valores in separar:
		# generamos una lista con los elemtos separados por un '=' en caso de 
		# que haya, habra mas de un elemento en la lista
		separado = valores.split('=')
		# si la longitud es mayor a 1, asignamos el primer valor de la lista 
		# como llave del diccionario y la segunda corresponde al valor de esa
		# llave
		if len(separado) > 1:
			diccionario[separado[0]] = separado[1]
	print('-------------')
	print(diccionario)
	return diccionario


    
def encontrar_button(texto):
	'''Recibe un string que representa código html que puede contener
	 varios botones con diferentes valores asociados a sus características, 
	 todas las líneas que identifican los botones respetan el formato:

	<button type="valor", class="valor",... >
	</button>
	Y debe devolver una lista con la información correspondiente a cada botón,
	la cual es generada por la función procesar_boton(). A cada elemento 
	devuelto por la función se le dede agregar la clave "span"  con el valor 
	True o False, dependiendo si se encuentra o no dentro del contenido de 
	los tags del botón el siguiente tag:
	'''
	# le quitamos el '</div>' a la cadena recibida x parametro
	lista_botones= texto.split('</div>')
	# generamos una lista vacia para ir guardando los string de los botones
	lista=[]
	# iteramos sobre la lista que se genero con  el string partido
	for boton in lista_botones:
		# cada string boton ser algo asi:
		# <div class="navbar-header">
     	#   <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navHeaderCollapse">
        #  		<span class="sr-only">Toggle navigation</span>
        #   </button>
		# esta porcion de string ira a procesar_button
		diccionarioBoton= procesar_button(boton)

		# si dentro delstring se encuentra la porcion de codigo 
		# <span class="sr-only">Toggle navigation</span> la clave spam del 
		# diccionario guardara Ture, False en caso contrario
		if '<span class="sr-only">Toggle navigation</span>' in boton:
			diccionarioBoton['span']=True
		else:
			diccionarioBoton['span']=False
		# al final de procesar el boton se agrega el diccionario a la lista
		lista.append(diccionarioBoton)


	return lista
 
def contar_clase(lista, clase):
	cantidad=0
	# contamos la cantidad de clases que hay en la lista
	for valores in lista:
		# si existe dentro de valores la llave 'class' accedemos al elemento 
		# ese de la lista, si no preguntara luego saltaria un error en caso de
		# que no exista esa clave, por eso lo filtro primero
		if 'class' in valores:
			# si el valor dentro de 'class' es igual al pasado por parametro se
			#  cuenta la cantidad.
			# Le hago un strip para quitar las " al comparar la clase recibida 
			# con la clase pasada por parametro
			if (valores['class'].strip('"') == clase): 
				cantidad= cantidad+1
	return cantidad	
	
	
	
html = '''
<div class="navbar-header">
    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navHeaderCollapse">
        <span class="sr-only">Toggle navigation</span>
    </button>
</div>
<div class="navbar-next">
    <button type="button_next" class="navbar-next" data-toggle="collapse" data-target=".navHeaderNext">
    </button>
</div>
<div class="navbar-next">
    <button type="button_next" class="navbar-next" data-toggle="collapse" data-target=".navHeaderNext">
    	<span class="sr-only">Toggle navigation</span>
    </button>
</div>
<div class="navbar-next">
    <button type="button_next" class="navbar-toggle" data-toggle="collapse" data-target=".navHeaderNext">
    </button>
</div>
<div class="navbar-next">
    <button type="button_next" class="navbar-toggle" data-toggle="collapse" data-target=".navHeaderNext">
    </button>
</div>
'''
botones=encontrar_button(html)
print(botones)

print(contar_clase(botones, 'navbar-toggle'))
