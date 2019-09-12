# -*- coding: utf-8 -*-
import numpy
import math
import xlsxwriter

class Calendario():
	def __init__(self,grupos,costes):
		self.grupos = grupos
		self.equiposGrupoA = grupos[0]
		self.equiposGrupoB = grupos[1]
		self.costes = costes

	def generar_calendario(self):
		matriz = numpy.zeros((5,5),dtype=numpy.int)
		descansa = [4,0,1,2,3]
		organiza = [0,1,2,3,4]
		jornadas = [
		[0,1,3,3,0,2,1,3],
		[1,2,3,4,1,3,2,4],
		[2,3,4,0,2,4,3,0],
		[3,4,0,1,3,0,4,1],
		[4,0,1,2,4,1,0,2]
		]
		
		matriz = numpy.zeros((10,10),dtype=numpy.int)
		for grupo in self.grupos:
			print(grupo)
			for i in range(len(jornadas)):
				descansa = grupo[descansa[i]]
				organiza = grupo[organiza[i]]				
								
				desplazamientos = []
				for equipo in grupo:
					if(equipo.indice != descansa.indice):
						if(equipo.indice != organiza.indice):
							desplazamientos.append(equipo)
							
				print("Jornada " + str(i))
				print("organiza " + organiza.nombre)
				print("descansa " + descansa.nombre)
					
				for desplazamiento in desplazamientos:
					matriz[organiza.indice,desplazamiento.indice] = self.costes[desplazamiento.indice,organiza.indice]
				
				print(matriz)
				distanciasEquipos = numpy.zeros((5,1),dtype=numpy.int)						
			
				desviacion = 0
				media = 0
				total = 0
				distanciasEquiposConEtiqueta = {}
				
				for i in range(5):
					for j in range(5):			
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

