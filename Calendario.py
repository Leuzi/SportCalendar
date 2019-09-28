# -*- coding: utf-8 -*-
import numpy
import math
import xlsxwriter
import statistics

class Calendario():
	def __init__(self,grupos,costes):
		self.grupos = grupos
		self.equiposGrupoA = grupos[0]
		self.equiposGrupoB = grupos[1]
		self.costes = costes
		self.distanciasEquipos = []
		self.matriz = []
		self.total = 0
		self.media = 0
		self.desviacion = 0
		self.indiceDesviacion = 0
		self.indiceTotal = 0
		self.indiceWeno = 0
		self.minDesviation = 0
		self.maxDesviation = 0
		self.minTotal = 0
		self.maxTotal = 0
				
		self.descansa = [[4,5],[3,4],[0,1],[1,2],[2,5],[0]]
		self.organiza = [0,1,2,3,4,5]
		
		self.jornadas = [
		[0,1,2,3,3,0,1,2],
		[1,5,0,2,2,1,5,0],
		[2,4,5,3,3,2,4,5],
		[3,5,4,0,0,3,5,4],
		[4,1,1,3,0,4,1,0],
		[5,1,2,5,3,4,4,2]
		]
	
	def equipoDescansaFunc(self,equipo,equiposDescansa):
		if equipo in equiposDescansa:
			return True
		else:
			return False
			
	def generar_calendario(self):
		
		matriz = numpy.zeros((12,12),dtype=numpy.int)
		for grupo in self.grupos:
			for i in range(len(self.jornadas)):
				
				equiposDescansa = self.descansa[i]
				
				equipoOrganiza = grupo[self.organiza[i]]				
				desplazamientos = []
				for equipo in grupo:
 	
					if(not self.equipoDescansaFunc(grupo.index(equipo),equiposDescansa)):
						if(equipo.indice != equipoOrganiza.indice):
							desplazamientos.append(equipo)
					
				"""
				print("Jornada " + str(i+1))
				print("self.organiza " + equipoOrganiza.nombre)
				for equipoDescansa in equiposDescansa:
					print("self.descansa " + grupo[equipoDescansa].nombre)
				
				
				print("desplazamientos")
				"""
				for desplazamiento in desplazamientos:
					"""
					print(desplazamiento.nombre)
					"""
					matriz[desplazamiento.indice,equipoOrganiza.indice] = self.costes[desplazamiento.indice,equipoOrganiza.indice]
		"""
		print(matriz)
		"""
		distanciasEquipos = numpy.zeros((12,1),dtype=numpy.int)	
		"""
		print(self.grupos)
		"""
		
		for grupo in self.grupos:
			for equipo in grupo:
				"""
				print(equipo)
				"""	
				for i  in range(len(matriz)):
					distanciasEquipos[equipo.indice,0] = distanciasEquipos[equipo.indice,0] + matriz[equipo.indice,i]		
		"""
		print(distanciasEquipos)
		print(len(distanciasEquipos))
		"""
		desviacion = 0
		media = 0
		total = 0
		distanciasEquiposConEtiqueta = {}
		
				
		total = sum(distanciasEquipos)
		"""
		print(distanciasEquipos)
		print(total)
		"""
		media = sum(distanciasEquipos) / float(len(distanciasEquipos))
		sample = []
		for distancia in distanciasEquipos:
			sample.append(distancia[0])
			desviacion = desviacion + (distancia-media)*(distancia-media)

		desviacion = statistics.stdev(sample)
		
		
		self.matriz = matriz
		self.distanciasEquipos = distanciasEquipos
		self.desviacion = desviacion
		self.media = media
		self.total = total

	def imprime_resultado(self,workbook,worksheet):
		
		worksheet.set_column(0, 0, 22)	
		worksheet.set_column(1, 1, 18)	
		worksheet.set_column(2, 2, 18)	
		worksheet.set_column(3, 3, 18)	
		worksheet.set_column(4, 4, 18)	
		worksheet.set_column(5, 5, 18)	
		worksheet.set_column(6, 6, 18)	
		worksheet.set_column(7, 7, 18)	
		

		bold = workbook.add_format({'bold': True})
		bold.set_font_color('white')
		bold.set_font_size(14)
		bold.set_bg_color('00cc00')
		
		i=0
		worksheet.write(1,0,'GrupoA',bold)	
		
		for equipo in self.equiposGrupoA:
			worksheet.write(2+i,0,equipo.nombre,bold)
				
			i= i+1
		
		i=0
		worksheet.write(1,4,'GrupoB',bold)	
		
		for equipo in self.equiposGrupoB:
			worksheet.write(2+i,4,equipo.nombre,bold)
				
			i= i+1
		
		filaActual = 8
			
		title = workbook.add_format({'bold':True})
		title.set_bg_color('000000')
		title.set_font_size(11)
		title.set_font_color('white')
		
		j = 0
		
		for grupo in self.grupos:
			for i in range(len(self.jornadas)):
				equipoOrganiza = grupo[self.organiza[i]]	
				equiposDescansa = self.descansa[i]			
				filaActual = filaActual +1
				worksheet.write(filaActual, 0+j, "Jornada" + str(i+1))
				worksheet.write(filaActual, 1+j, "Organiza " + equipoOrganiza.nombre)
				worksheet.write(filaActual, 2+j, "Descansa ")
				for k in range(len(equiposDescansa)):
					
					worksheet.write(filaActual+k, 2+j, grupo[equiposDescansa[k]].nombre)
				
				for equipo1,equipo2 in zip(self.jornadas[i][::2], self.jornadas[i][1::2]):
					filaActual = filaActual +1
					worksheet.write(filaActual, 0+j, grupo[equipo1].nombre)
					worksheet.write(filaActual, 1+j, grupo[equipo2].nombre)
				
			"""
			print(self.distanciasEquipos)
			"""
			filaActual = 8
		
		
			for i in range(len(grupo)):
				worksheet.write(filaActual+i+j,9, grupo[i].nombre)
				worksheet.write(filaActual+i+j, 10, str(self.distanciasEquipos[grupo[i].indice]) + " kms")
			j = j +6
		i=0
		
		filaActual = 0
		
		for i in range(len(self.matriz)):
			fila = self.matriz[i]
			for j in range(len(fila)):
				celda = fila[j]
				worksheet.write(filaActual+i+5,12+j,celda,bold)
		
		worksheet.write(filaActual,7,'Media por equipo',bold)
		worksheet.write(filaActual,8,str(self.media)+' kms')	
		worksheet.write(filaActual+1,7,'Klm entre todos',bold)
		worksheet.write(filaActual+1,8,str(self.total)+' kms')	
		worksheet.write(filaActual+2,7,'Desviacion',bold)
		worksheet.write(filaActual+2,8,str(self.desviacion)+' kms')
		worksheet.write(filaActual+3,7, 'Indice desviacion')
		worksheet.write(filaActual+3,7, str(self.indiceDesviacion))
		worksheet.write(filaActual+3,7, 'Indice kilometros')
		worksheet.write(filaActual+3,8, str(self.indiceWeno))
		worksheet.write(filaActual+4,7, 'Min Kilometros ' +str(self.minTotal))
		worksheet.write(filaActual+5,7, 'Max Kilometros '+str(self.maxTotal))
		worksheet.write(filaActual+6,7, 'Min Desviacion '+str(self.minDesviacion))
		worksheet.write(filaActual+7,7, 'Max Desviacion '+str(self.maxDesviacion))
		
		worksheet.write(filaActual+0, 10, 'Indice total ' +str(self.indiceTotal))
		worksheet.write(filaActual+1, 11, 'Indice desv '+str(self.indiceDesviacion))
		
	def calculaIndice(self,minDesviacion,maxDesviacion,minKilometros,maxKilometros):
		self.indiceDesviacion = (self.desviacion-minDesviacion)/(maxDesviacion-minDesviacion)
		self.indiceTotal = (self.total-minKilometros)/(maxKilometros-minKilometros)
		self.indiceTotal = self.indiceTotal[0]		
		self.minDesviacion = minDesviacion
		self.maxDesviacion = maxDesviacion
		self.minTotal = minKilometros
		self.maxTotal = maxKilometros
		
		self.indiceWeno =  math.sqrt(self.indiceDesviacion*self.indiceDesviacion+ self.indiceTotal*self.indiceTotal) * math.sqrt( abs(self.indiceTotal + self.indiceDesviacion) * abs(self.indiceTotal + self.indiceDesviacion))
