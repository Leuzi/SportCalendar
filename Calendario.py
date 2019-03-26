# -*- coding: utf-8 -*-
import numpy
import math
import xlsxwriter

class Calendario():
	def __init__(self,grupos,costes):
		self.grupos = grupos
		self.costes = costes

	def generar_calendario(self):
		matriz = numpy.zeros((4,4),dtype=numpy.int)
		calendario = [
		[0,0,0,1],
		[1,0,0,0],
		[1,1,0,0],
		[0,1,1,0]
		]
		
		for grupo in self.grupos:
			matriz = numpy.zeros((4,4),dtype=numpy.int)
			print(grupo.equipos)
			for i in range(4):
				for j in range(4):
					matriz[i][j] = calendario[i][j] * self.costes[grupo.equipos[i].indice][grupo.equipos[j].indice]
			print(matriz)
			grupo.costeGrupo = matriz
			distanciasEquipos = numpy.zeros((4,1),dtype=numpy.int)
					
		
			desviacion = 0
			media = 0
			total = 0
			distanciasEquiposConEtiqueta = {}
			
			for i in range(4):
				for j in range(4):			
					distanciasEquipos[grupo.equipos[i].indice] = distanciasEquipos[grupo.equipos[i].indice] + matriz[grupo.equipos[i].indice][grupo.equipos[j].indice]
					distanciasEquiposConEtiqueta.update()
			total = sum(distanciasEquipos)
			print(distanciasEquipos)
			print(total)

			media = sum(distanciasEquipos) / float(len(distanciasEquipos))
			for distancia in distanciasEquipos:
				desviacion = desviacion + (distancia-media)*(distancia-media)

			desviacion = math.sqrt(desviacion/9)
			
			grupo.setCoste(matriz,distanciasEquipos,desviacion,media,total)
	

		
		return matriz

