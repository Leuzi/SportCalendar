# -*- coding: utf-8 -*-
from Equipos import Equipo
from Grupo import Grupo
from Calendario import Calendario
import numpy
import itertools
import xlsxwriter
from collections import Counter

def cargaDatos():

	#Abrimos el archivo que contiene los datos

	equipos = cargaEquipos('datos')
	matriz = cargaMatriz('costes')
	return equipos,matriz

def cargaEquipos(nombre):

	equipos = []
	archivo = open(nombre,"r", encoding='utf-8')

	for i in range(9):
		nombre,iniciales,ciudad,indice= archivo.readline().split('\t')
		equipos.append(Equipo(nombre,iniciales,ciudad,indice))
		
	return equipos

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

def generaGruposConCalendarioConEquipos(equipos):
	
	calendarios = []
	print("Equipos")
	print(equipos)
	
	divisiones = list(itertools.combinations(equipos.__iter__(),5))
	print("Divisiones")
	print(str(len(divisiones)))
	
	calendarios = set()
	for grupo in divisiones:
		"""
		print(grupo)
		print(Counter(getattr(recuento, 'ciudad') for recuento in grupo))
		"""
		concentraciones = Counter(getattr(recuento, 'ciudad') for recuento in grupo)  
		
		if concentraciones['GRA'] is 1 and concentraciones['COR'] is 1 :
				for calendario in itertools.permutations(grupo):
					calendarios.add(Grupo(calendario, set(equipos)-set(calendario)))
					
	print("Un total de " +str(len(calendarios)) +" calendarios unicos")
	print(list(calendarios)[0:5])
	
	return list(calendarios)
	
def main():
	equipos,matriz = cargaDatos()

	i = 0
	
	grupos = generaGruposConCalendarioConEquipos(list(equipos));
	print(grupos)
	"""print(grupos);
	"""
	
	
	
	calendarios=[]
		
	for equipos in all_pairs(equipos):
		lst = list(itertools.product([0, 1], repeat=12))
		for creador in lst:
			calendario = Calendario(creador,equipos,i)			
			if calendario.es_valido():				
				calendario.generar_resultados(matriz)				
				calendarios.append(calendario)
				i = i+1

	calendarios.sort(key=lambda x: x.total)

	workbook = xlsxwriter.Workbook('total.xlsx')	
		
	i = 1
	for calendario in calendarios:
		nombre = 'Opcion '+ str(i)
		
		for equipos in calendario.partidos:
			if ciudades[0] in equipos and ciudades[5] in equipos:
				for equipos1 in calendario.partidos:
					if ciudades[1] in equipos1 and ciudades[4] in equipos1:
						for equipos2 in calendario.partidos:
							if ciudades[2] in equipos2 and ciudades[3] in equipos2:
								nombre = nombre + 'Respeta ranking'
		worksheet = workbook.add_worksheet(nombre)
		calendario.imprime_resultado(workbook,worksheet,ciudades)
		i = i+1
	
	workbook.close()
	print('Total calendario:'+str(i))
	
		
if __name__ == "__main__":

	main()



