# -*- coding: utf-8 -*-
from Equipos import Equipo
from Calendario import Calendario
import numpy
from itertools import combinations
import xlsxwriter

def cargaDatos():

	#Abrimos el archivo que contiene los datos

	matriz = cargaMatriz('costes')
	ciudades = cargaEquipos('datos',matriz)
	
	return ciudades,matriz

def cargaEquipos(nombre,matriz):

	equipos = []
	archivo = open(nombre,"r")

	for i in range(8):
		nombre,iniciales,indice= archivo.readline().split('\t')
		equipos.append(Equipo(nombre,iniciales,indice))
	return equipos

def cargaMatriz(nombre):
	distancias = numpy.loadtxt(nombre, delimiter="\t")
	return distancias
			
def main():
	equipos,distancias = cargaDatos()
	
	for equipo in equipos:
		equipo.ponDistancias(equipos,distancias)
		
	for i in range(3,8):
		set = list(combinations(equipos,i))
		for equipos in set:
			Calendario(equipos)
		
if __name__ == "__main__":

	main()



