from Equipos import Equipo
from Calendario import Calendario
import numpy
import itertools
import xlsxwriter

def cargaDatos():

	#Abrimos el archivo que contiene los datos

	ciudades = cargaCiudades('datos')
	matriz = cargaMatriz('costes')
	return ciudades,matriz

def cargaCiudades(nombre):

	equipos = []
	archivo = open(nombre,"r")

	for i in range(5):
		nombre,iniciales,indice= archivo.readline().split('\t')
		equipos.append(Equipo(nombre,iniciales,indice))
	return equipos

def cargaMatriz(nombre):
	matriz = numpy.loadtxt(nombre, delimiter="\t")
	return matriz
			
def obtenerCalendarios():
	variables = [0,0,1,1,2,2,3,3,4,4]
	permutations = []
	
	
	print("OBTENER CALENDARIOS")
	for permutation in itertools.permutations(variables, 10):
		#print(permutation)
		if is_valid_permutation(permutation):
			#print("Permutacion valida")
			#print(permutation)
			
			
			permutations.append(list(group(permutation, 2)))
			#print("Permutacion nueva "+ str(len(permutations)))
			
			#print(permutation)
	
	print(len(permutations))
	return permutations


def isPermutationDuplicated(permutations,validPermutation):
	#print("Comparacion")
	
	isDuplicated = False
	
	if not permutations:
		return False
	
	for permutation in permutations:
		#print("Permutacion")
		#print(permutation)
		#print("validPermutation")
		#print(validPermutation)
		#print("difference")
		difference = [item for item in validPermutation if item not in permutation]
		
		#print(difference)
		#print(bool(difference))	
		
		if(not bool(difference)):
			#print("Duplicated")
			isDuplicated = True
			break
	
	return isDuplicated
	


def getSortedPermutation(permutation):
	validpermutation = []
	for element in permutation:
		validpermutation.append(sorted(element))
		
	return validpermutation

def group(lst, n):
  for i in range(0, len(lst), n):
    val = lst[i:i+n]
    if len(val) == n:
      yield tuple(val)

def is_valid_permutation(permutation):
	
	groups = list(group(permutation, 2))

	isValid = True
	for i in range(5):
		if groups[i][0] == i or groups[i][1] ==i:
			isValid = False
		if groups[i][0] == groups[i][1]:
			isValid =  False
			
		if (i != groups[groups[i][0]][0] and
		    i != groups[groups[i][0]][1]): 
			isValid =  False
			
		if (i != groups[groups[i][1]][0] and
		   i != groups[groups[i][1]][1]): 
			isValid =  False
			
			
	return isValid 

def main():
	ciudades,matriz = cargaDatos()

	#print(ciudades)
	#print(matriz)
	i = 0
	j = 0
	k = 0
	calendarios=[]
	todosCalendarios = obtenerCalendarios()
	
	print("LONGITUDTODOS")
	print(str(len(todosCalendarios)))
	for equipos in todosCalendarios:
		print(equipos)
	
	for equipos in todosCalendarios:
		print("OBTENIENDO CALENDARIO" + str(j))
		print(equipos)
		lst = list(itertools.product([0, 1], repeat=6))
		#print(lst)
		
		for creador in lst:
			calendario = Calendario(creador,equipos,i)		
			if calendario.es_valido():
				
				print("Calendario Valido"  )
				k = k+1
				print(calendario.calendario)
				if not estaRepetido(calendarios,calendario):				
					calendario.generar_resultados(matriz)				
					calendarios.append(calendario)
					print("calendario valido "+str(i))
					print(str(len(calendarios)))
					i = i+1
		j = j +1
	calendarios.sort(key=lambda x: x.desviacion)

	workbook = xlsxwriter.Workbook('desviacion.xlsx')	
		
	i = 1
	for calendario in calendarios:
		nombre = 'Opcion '+ str(i)
		
		worksheet = workbook.add_worksheet(nombre)
		print("imprimiendo " + nombre)
		calendario.imprime_resultado(workbook,worksheet,ciudades)
		i = i+1
	
	workbook.close()
	print('Total calendario:'+str(i))

def estaRepetido(calendarios,calendario):
	repetido = False
	
	print("Longitud de calendarios "+ str(len(calendarios)))
	
	for calen in calendarios:
		#print("calen.calendario")
		#print(calen.calendario)
		#print("calendario.calendario")
		#print(calendario.calendario)
		if numpy.array_equal(calen.calendario,calendario.calendario):
			repetido = True
			break
		
	if(repetido):
		print("Repetido")
	else:
		print("No repetido")
	return repetido
if __name__ == "__main__":

	main()



