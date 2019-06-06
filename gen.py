#import datetime

#def titulop():
#	titu = '\\begin{table}[]\n\\centering\n\\caption{Cuadro de Punnett}\n\\label{cuadrodepunnett}\n'
#	return titu
	
#def anch(c1, c2):
#	a = '\\begin{tabular}{l|' + 'l'*max(len(c1), len(c2)) + '}\n\\hline\n'
#	return a
	
#def fecuencias():
#	frecuencias = '\\begin{table}[]\n\\centering\n\\caption{Frecuencias de los genotipos}\n\\label{frecgenotipo}\n\\begin{tabular}{ll}\n\\hline\nGenotipos y Frecuencias \\\ \\hline'
#	return frecuencias
		
#def abajo():
#	aba = '\n\\end{tabular}\n\\end{table}'
#	return aba
		
#Las funciones de arriba comentadas son el formato para tablas de LaTeX
	
def combinaciones(padre): # Encuentra las combinaciones que cada padre puede heredar a su descendencia. Asume que todos son independientes.
	if len(padre) == 1:
		return [padre[0][0], padre[0][1]]
	else:
		genlist = []
		for x in combinaciones(padre[1:]):
			genlist.append(padre[0][0] + x)
			genlist.append(padre[0][1] + x)
		return genlist

def fila(genotipo, alelo): 
	filaa = []
	for a in genotipo:
		filaa.append(a + alelo)
	return filaa

def tabla(padre1, padre2):
	tab = []
	for a in padre1:
		tab.append(fila(padre2, a))
	return tab

def impr_tabla(tab, c1, c2): # imprime y da formato al cuadro
	tablalatex = []
	long = (len(c1[0])*2+4)*2**(len(c1[0]))
	print('')
	print('', end=' ')
	for a in c2:
		print(' '*(len(c1[0])+3) + a + '', end=' ')
		tablalatex.append('& ' + a + ' ')
	print('\n' + ' '*(len(c1[0])+1) + '-'*(long))
	tablalatex.append('\\\ \n\\hline\n')
	
	for i, filab in enumerate(tab): 
		print(c1[tab.index(filab)], end=' ')
		tablalatex.append(c1[tab.index(filab)] + ' & ')
		print('|', end=' ')
		for j, cel in enumerate(filab):
			print(cel + ' | ', end=' ')
			if j != len(filab)-1:
				tablalatex.append(cel + ' & ')
			else:
				tablalatex.append(cel + ' ')
		print('\n' + ' '*(len(c1[0])+1) + '-'*(long))
		if i != len(tab)-1:
			tablalatex.append('\\\ \n')	
	return tablalatex		
	
def frec_geno(tab): # calcula las frecuencias para cada genotipo presente en las tablas
	frectab = []
	frectab.append('\n')
	calcu = []
	genotipos = [a for b in tab for a in b]
	for k, x in enumerate(genotipos):
		cuenta = 0
		for y in genotipos:
			if sorted(x) == sorted(y):
				cuenta += 1
		if sorted(x) not in calcu:
			print("La frecuencia del genotipo " + x + " es del " + str(float(cuenta)/float((len(genotipos)))*100) + "%.")
			frectab.append(x + ' & ' + str(float(cuenta)/float((len(genotipos)))*100) + '\\% \\\ \\hline \n')	
		calcu.append(sorted(x))
	return frectab	

print('') #Mensaje de bienvenida.
print('===================   Generador de cuadros de Punnett  ======================')
print('') 
print('Este programa genera cuadros de Punnet. Lo primero que debes de hacer es colocar los genotipos de cada padre. Tienen que ser dos genotipos por padre, mínimo.')
print('Los genes tienen que estar separados por espacios. Por ejemplo, una entrada valida sería Xx Yy. Mientras que XxYy te dará')
print('como resultado un error.')
print('') 
print('=============================================================================')
print('') 
while True:
	p1 = input("Teclea el genotipo del primer padre:  ").split(' ') #Inputs de los genotipos.
	p2 = input("Teclea el genotipo del segundo padre: ").split(' ')
	c1 = combinaciones(p1) #guarda el input para usarlo en la funcion comibnaciones 
	c2 = combinaciones(p2)
	a = tabla(c1, c2)
	tablalatex = impr_tabla(a, c1, c2)
	frectab = frec_geno(a)
	print('')

	#option = input("Teclea (g) para guardar tu cuadro en un .tex o presiona cualquier tecla para continuar sin guardar.\n")
	#if option == "g":
		#ahora = datetime.datetime.now() # Fecha
		#nom = '%s_tab.tex' % (ahora.strftime("%d-%m-%Y_%H-%M-%S")) # Asigna la fecha como nombre del .tex
		#f = open(nom, 'w') # Abre el doc
		#f.write(titulop())
		#f.write(anch(c1, c2))
		#for item in tablalatex:
			#f.write("%s" % item)
		#f.write(abajo())
		#f.write(fecuencias())
		#for i in frectab:
			#f.write("%s" % i)
		#f.write(abajo())
		#f.close()
		#print('') 
		#print('Tu archivo ' + nom + ' ha sido guarado correctamente. \n')

#Lo comantado arriba es la parte para que se guarde el resultado en un .tex

	action = input("Presiona (c) para hacer otro cuadro o cualquier otra tecla para parar el programa. \n") #opción para parar o repetir el programa
	if action == "c":
		print('')
		print("Aquí vamos de nuevo! \n")
	else:	
		quit()
