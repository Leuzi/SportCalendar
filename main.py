# -*- coding: utf-8 -*-
from Equipos import Equipo
from Grupo import Grupo
from Calendario import Calendario
import numpy
import itertools
import xlsxwriter
from collections import Counter
import sys
import math
import matplotlib.pyplot as plt

def cargaDatos(datos,costes):

	#Abrimos el archivo que contiene los datos

	equipos = cargaEquipos(datos)
	matriz = cargaMatriz(costes)
	return equipos,matriz

def cargaEquipos(nombre):

	equipos = []
	archivo = open(nombre,"r", encoding='utf-8')

	for i in range(12):
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
	
def findTeams(combination):
	
	cordoba = None
	malaga = None
	
	for i in range(len(combination)):
		if combination[i].iniciales == 'COR':
			malaga = i
		if combination[i].iniciales == 'BUF':
			cordoba = i
	values = list([malaga,cordoba])
	values.sort()
	
	print(values)
	
	return values
	
def combinacionPosible(combinationA):
	validCombinations = [[0,1],[0,3],[0,4],[1,2],[1,5],[2,3],[2,4],[3,5],[4,5]]
	"""
	teams=findTeams(combinationA)
	valid = False
	
	for combination in validCombinations:
		if combination[0] == teams[0]:
			if combination[1] == teams[1]:
				valid=True
	print(valid)
	return valid
	"""
	return True	
	
def main():
	
	equipos,costes = cargaDatos(sys.argv[1],sys.argv[2])
	grupos = list()
	grupoA = list()
	grupoA.append(equipos[0])
	grupoA.append(equipos[3])
	grupoA.append(equipos[5])
	grupoA.append(equipos[8])
	grupoA.append(equipos[9])
	grupoA.append(equipos[10])
	grupoB = list()
	grupoB.append(equipos[1])
	grupoB.append(equipos[2])
	grupoB.append(equipos[3])
	grupoB.append(equipos[6])
	grupoB.append(equipos[7])
	grupoB.append(equipos[11])

	grupos.append([grupoA,grupoB])
	
	gruposPosibles = []
	
	i=0
	for posi in grupos:
	
		grupoA = posi[0]
		grupoB = posi[1]
		
		
		print("GrupoA")
		print(grupoA)
		print("GrupoB")
		print(grupoB)
		
		combinationsA = itertools.permutations(list(grupoA),6)
		combinationsB = itertools.permutations(list(grupoB),6)
		
		for combinationA in list(combinationsA):
			if(i%1000000 == 0):
				print(i)
			i = i+1
			"""
			print(combinationB)
			"""
			if combinacionPosible(combinationA):
				"""
				print(combinacionPosible(combinationB))
				"""
				for combinationB in list(combinationsB):
					"""
					print(combinationA)
					print(combinationB)
					"""
					gruposPosibles.append([combinationA,combinationB])

	i = 0
	
	print("Calendarios posibles "+str(len(gruposPosibles)))
	calendarios = []
	for grupo in gruposPosibles:	
		
		print("calendario numero" + str(i))
		
		calendario = Calendario(grupo,costes)			
		calendario.generar_calendario()
		calendarios.append(calendario)
		i = i+1
	
	calendarios.sort(key=lambda x: x.desviacion)
	minDesviacion = calendarios[0].desviacion
	maxDesviacion = calendarios[-1].desviacion
	calendarios.sort(key=lambda x: x.total)
	minKilometros = calendarios[0].total
	maxKilometros = calendarios[-1].total
	
	for calendario in calendarios:
		calendario.calculaIndice(minDesviacion,maxDesviacion,minKilometros,maxKilometros)


	calendarios.sort(key=lambda x: (x.desviacion))
	
	workbook = xlsxwriter.Workbook('desviacionSinRestriccion.xlsx')	
		
	i = 1
	
	
	for calendario in calendarios[:500]:
		nombre = 'Opcion '+ str(i)
		
		worksheet = workbook.add_worksheet(nombre)
		calendario.imprime_resultado(workbook,worksheet)
		i = i+1
	
	workbook.close()
	print('Total calendario:'+str(i))
	
	print('Plotting:')
	
	plt.plot( [x.indiceDesviacion for x in calendarios], [ y.indiceTotal for y in calendarios], 'ro')
	plt.ylabel('some numbers')
	plt.show()
	
		
if __name__ == "__main__":

	main()



