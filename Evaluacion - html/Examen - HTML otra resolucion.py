
def procesar_boton(string):
	string = string.replace('<','').replace('>','').replace('button ','')
	string = string.split()

	dic={}
	for i in string:
		x= i.split('=')
		dic[x[0]]=x[1].replace('"','')
		
	return dic
def encontrar_botones(string):
	
	listaString= string.split('</button>')
	listaTot=[]

	for i in listaString:
		i=i.strip()
		x=i.split('\n')		
		dicc= procesar_boton(x[0])
		if (len(dicc)) != 0:	
			if '<span class="sr-only">Toggle navigation</span>' in i:#if len(x)== 2:#'span' in i[1]:
				dicc['spn'] = True
			else :
				dicc['spn'] = False
			listaTot.append(dicc)
	
	return listaTot
def contar_clase(lista, string):
	cont=0
	
	for i in lista:
		if i['class'] == string:
			cont=cont+1
		print(i)
	print('el string aparece: '+ str(cont))
				
html = '''
    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navHeaderCollapse">
    <span class="sr-only">Toggle navigation</span>
    </button>
    <button type="button_next" class="navbar-next" data-toggle="collapse" data-target=".navHeaderNext">
    </button>
    <button type="button_next" class="navbar-next" data-toggle="collapse" data-target=".navHeaderNext">
    <span class="sr-only">Toggle navigation</span>
    </button>
    <button type="button_next" class="navbar-toggle" data-toggle="collapse" data-target=".navHeaderNext">
    </button>
    <button type="button_next" class="navbar-toggle" data-toggle="collapse" data-target=".navHeaderNext">
    </button>
'''
lista = encontrar_botones(html)
str1 = str(input())
print(type(str1))
contar_clase(lista, str1)		


