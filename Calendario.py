# -*- coding: utf-8 -*-
import numpy
import math
import xlsxwriter

class Calendario():
	def __init__(self,grupos,costes ):
		self.grupos = grupos
		self.costes = costes

	def generar_calendario(self):
		matriz = numpy.zeros((9,9),dtype=numpy.int)
		
		grupo_a_organiza = [0,1,2,3,4]
		grupo_a_descansa = [4,2,1,0,3]
		for grupo in self.grupos:
			matriz = numpy.zeros((9,9),dtype=numpy.int)
			
			i = 0
			for i in range(len(grupo_a_organiza)):
				organiza = grupo.equipos_grupo_a[grupo_a_organiza[i]]
				descansa = grupo.equipos_grupo_a[grupo_a_descansa[i]]
				desplazamientos = list(set(grupo.equipos_grupo_a) - set([organiza,descansa]))
				
				matriz[desplazamientos[0].indice][organiza.indice] = self.costes[desplazamientos[0].indice][organiza.indice]
				matriz[desplazamientos[1].indice][organiza.indice] = self.costes[desplazamientos[1].indice][organiza.indice]
				matriz[desplazamientos[2].indice][organiza.indice] = self.costes[desplazamientos[2].indice][organiza.indice]
			
			for equipo in grupo.equipos_grupo_b:
				rival = list(set(grupo.equipos_grupo_b) - set([equipo]))
				"""print(rival)"""
				matriz[equipo.indice][rival[0].indice] = self.costes[equipo.indice][rival[0].indice]
				matriz[equipo.indice][rival[1].indice] = self.costes[equipo.indice][rival[1].indice]
				matriz[equipo.indice][rival[2].indice] = self.costes[equipo.indice][rival[2].indice]
			"""
			print(matriz)
			"""
			distanciasEquipos = numpy.zeros((9,1),dtype=numpy.int)
			desviacion = 0
			media = 0
			total = 0
			distanciasEquiposConEtiqueta = {}
			for i in range(9):
				for j in range(9):			
					distanciasEquipos[i] = distanciasEquipos[i] + matriz[i][j]
					distanciasEquiposConEtiqueta.update()
					total = total + matriz[i][j]

			media = sum(distanciasEquipos) / float(len(distanciasEquipos))
			for distancia in distanciasEquipos:
				desviacion = desviacion + (distancia-media)*(distancia-media)

			desviacion = math.sqrt(desviacion/9)
			
			grupo.setCoste(matriz,distanciasEquipos,desviacion,media,total)
			
		for grupo in self.grupos:
			for jornada in grupo.calendario_grupo_a:
				for equipo1, equipo2 in zip(jornada[0::2], jornada[1::2]):
					pass
		
		return matriz

