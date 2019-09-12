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

	for i in range(10):
		nombre,iniciales,ciudad,indice= archivo.readline().split('\t')
		equipos.append(Equipo(nombre,iniciales,ciudad,indice))
		
	return equipos

def cargaMatriz(nombre):
	matriz = numpy.loadtxt(nombre, delimiter="\t")
	return matriz
	
def equiposRepetido(grupo):
	ciudades = set()
	
	for equipo in grupo:
		ciudades.add(equipo.ciudad)
	return  not(len(ciudades) == len(grupo))
	
def main():
	equipos,costes = cargaDatos()

	grupos = []
	
	for grupo in itertools.permutations(equipos,10):
		grupoA = grupo[0:5]
		grupoB = grupo[5:10]
		
		if not (equiposRepetido(grupoA)) and not (equiposRepetido(grupoB)):
			grupos.append([grupoA,grupoB])
		
	
	
	i = 0
	
	
	"""print(grupos);
	"""
	calendarios = []
	for grupo in grupos:	
		calendario = Calendario(grupo,costes)			
		calendario.generar_calendario()
		calendarios.append(calendario)
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



