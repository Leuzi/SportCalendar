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

	for i in range(4):
		nombre,iniciales,ciudad,indice= archivo.readline().split('\t')
		equipos.append(Equipo(nombre,iniciales,ciudad,indice))
		
	return equipos

def cargaMatriz(nombre):
	matriz = numpy.loadtxt(nombre, delimiter="\t")
	return matriz


def generaGruposConCalendarioConEquipos(equipos):
	
	calendarios = []
	print("Equipos")
	print(equipos)
	
	calendario = list(itertools.permutations(equipos.__iter__(),4))
	print("Calendarios")
	print(str(len(calendario)))
	
	
	for equipos_ordenados in calendario:
		print(equipos_ordenados)
		calendarios.append(Grupo(equipos_ordenados))
					
	print("Un total de " +str(len(calendario)) +" calendarios unicos")
	"""
	print(list(calendarios)[0:5])
	"""
	return list(calendarios)
	
def main():
	equipos,costes = cargaDatos()

	i = 0
	
	grupos = generaGruposConCalendarioConEquipos(list(equipos));
	
	print(str(len(grupos)))
	"""print(grupos);
	"""
		
	calendarios = Calendario(grupos,costes)			
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



