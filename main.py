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

	ciudades = []
	archivo = open(nombre,"r")

	for i in range(6):
		nombre,indice= archivo.readline().split('\t')
		ciudades.append(Equipo(nombre,indice))
	return ciudades

def cargaMatriz(nombre):
	matriz = numpy.loadtxt(nombre, delimiter="\t")
	return matriz
			
def all_pairs(lst):
    if len(lst) < 2:
        yield lst
        return
    a = lst[0]
    for i in range(1,len(lst)):
        pair = (a,lst[i])
        for rest in all_pairs(lst[1:i]+lst[i+1:]):
            yield [pair] + rest

def main():
	ciudades,matriz = cargaDatos()
	
	i = 0

	calendarios=[]
		
	for equipos in all_pairs(ciudades):
		lst = list(itertools.product([0, 1], repeat=12))
		for creador in lst:
			calendario = Calendario(creador,equipos,i)			
			if calendario.es_valido():				
				calendario.generar_resultados(matriz)				
				calendarios.append(calendario)
				i = i+1

	calendarios.sort(key=lambda x: x.total)

	workbook = xlsxwriter.Workbook('distancia.xlsx')	
		
	for calendario in calendarios:
		worksheet = workbook.add_worksheet()
		calendario.imprime_resultado(workbook,worksheet,ciudades)
	
	workbook.close()
	print('Total calendario:'+str(i))
	
		
if __name__ == "__main__":

	main()



