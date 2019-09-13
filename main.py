# -*- coding: utf-8 -*-
from Equipos import Equipo
from Grupo import Grupo
from Calendario import Calendario
import numpy
import itertools
import xlsxwriter
from collections import Counter
import sys

def cargaDatos(datos,costes):

	#Abrimos el archivo que contiene los datos

	equipos = cargaEquipos(datos)
	matriz = cargaMatriz(costes)
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
	
	equipos,costes = cargaDatos(sys.argv[1],sys.argv[2])

	grupos = [equipos[0],
	equipos[1],
	equipos[2],
	equipos[3],
	equipos[5],
	equipos[6],
	equipos[7],
	equipos[9]]
	
	gruposPosibles = []
	
	for posi in itertools.permutations(grupos,4):
		grupoA = list(posi)
		grupoB = [x for x in grupos if x not in grupoA]
		grupoA.append(equipos[4])
		
		grupoB.append(equipos[8])
	
		print("GrupoA")
		print(grupoA)
		print("GrupoB")
		print(grupoB)
		
		combinationsA = itertools.permutations(grupoA,5)
		combinationsB = itertools.permutations(grupoB,5)
		for combinationA in combinationsA:
			for combinationB in combinationsB:
				print(combinationA)
				print(combinationB)
				gruposPosibles.append([combinationA,combinationB])
	
	
	
	i = 0
	
	
	"""print(grupos);
	"""
	calendarios = []
	for grupo in gruposPosibles:	
		print("calendario numero" + str(i))
		calendario = Calendario(grupo,costes)			
		calendario.generar_calendario()
		calendarios.append(calendario)
		i = i+1

	calendarios.sort(key=lambda x: x.total)

	workbook = xlsxwriter.Workbook('total.xlsx')	
		
	i = 1
	for calendario in calendarios[:500]:
		nombre = 'Opcion '+ str(i)
		
		worksheet = workbook.add_worksheet(nombre)
		calendario.imprime_resultado(workbook,worksheet)
		i = i+1
	
	workbook.close()
	print('Total calendario:'+str(i))
	
		
if __name__ == "__main__":

	main()



