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
		self.distanciasEquipos = []
		self.matriz = []
		self.total = 0
		self.media = 0
		self.desviacion = 0
		
		self.jornadas = [
		[0,1,3,3,0,2,1,3],
		[1,2,3,4,1,3,2,4],
		[2,3,4,0,2,4,3,0],
		[3,4,0,1,3,0,4,1],
		[4,0,1,2,4,1,0,2]
		]
		
		self.descansa = [4,0,1,2,3]
		self.organiza = [0,1,2,3,4]

	def generar_calendario(self):
		matriz = numpy.zeros((5,5),dtype=numpy.int)
		
		
		
		matriz = numpy.zeros((10,10),dtype=numpy.int)
		for grupo in self.grupos:
			for i in range(len(self.jornadas)):
				equipoDescansa = grupo[self.descansa[i]]
				equipoOrganiza = grupo[self.organiza[i]]				
								
				desplazamientos = []
				for equipo in grupo:
					if(equipo.indice != equipoDescansa.indice):
						if(equipo.indice != equipoOrganiza.indice):
							desplazamientos.append(equipo)
				
				"""		
				print("Jornada " + str(i+1))
				print("self.organiza " + equipoOrganiza.nombre)
				print("self.descansa " + equipoDescansa.nombre)
				"""
				for desplazamiento in desplazamientos:
					matriz[desplazamiento.indice,equipoOrganiza.indice] = self.costes[desplazamiento.indice,equipoOrganiza.indice]
		"""
		print(matriz)
		"""
		distanciasEquipos = numpy.zeros((10,1),dtype=numpy.int)	
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
		print(distanciasEquipos)
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
		for distancia in distanciasEquipos:
			desviacion = desviacion + (distancia-media)*(distancia-media)

		desviacion = math.sqrt(desviacion/10)
		
		
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
				equipoDescansa = grupo[self.descansa[i]]
				equipoOrganiza = grupo[self.organiza[i]]				
				filaActual = filaActual +1
				worksheet.write(filaActual, 0+j, "Jornada" + str(i+1))
				worksheet.write(filaActual, 1+j, "Organiza " + equipoOrganiza.nombre)
				worksheet.write(filaActual, 2+j, "Descansa " + equipoDescansa.nombre)
				
				for equipo1,equipo2 in zip(self.jornadas[i][::2], self.jornadas[i][1::2]):
					filaActual = filaActual +1
					worksheet.write(filaActual, 0+j, grupo[equipo1].nombre)
					worksheet.write(filaActual, 1+j, grupo[equipo2].nombre)
					
			print(self.distanciasEquipos)
			filaActual = 8
		
		
			for i in range(len(grupo)):
				print(str(i))
				worksheet.write(filaActual+i+j,8, grupo[i].nombre)
				worksheet.write(filaActual+i+j, 9, str(self.distanciasEquipos[grupo[i].indice]) + " kms")
			j = j +5
		i=0
		
		filaActual = 0
		worksheet.write(filaActual,7,'Media por equipo',bold)
		worksheet.write(filaActual,8,str(self.media)+' kms')	
		worksheet.write(filaActual+1,7,'Klm entre todos',bold)
		worksheet.write(filaActual+1,8,str(self.total)+' kms')	
		worksheet.write(filaActual+2,7,'Desviacion',bold)
		worksheet.write(filaActual+2,8,str(self.desviacion)+' kms')
