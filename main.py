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
	"""
	print(list(calendarios)[0:5])
	"""
	return list(calendarios)
	
def main():
	equipos,matriz = cargaDatos()

	i = 0
	
	grupos = generaGruposConCalendarioConEquipos(list(equipos));
	
	print(str(len(grupos)))
	"""print(grupos);
	"""
		
	calendarios = Calendario(grupos,matriz)			
	calendarios.generar_calendario()
	i = i+1

	calendarios.grupos.sort(key=lambda x: x.desviacion)

	workbook = xlsxwriter.Workbook('desviacion.xlsx')	
		
	i = 1
	for calendario in calendarios.grupos[:500]:
		nombre = 'Opcion '+ str(i)
		
		worksheet = workbook.add_worksheet(nombre)
		calendario.imprime_resultado(workbook,worksheet)
		i = i+1
	
	workbook.close()
	print('Total calendario:'+str(i))
	
		
if __name__ == "__main__":

	main()



