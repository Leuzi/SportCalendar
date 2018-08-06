import numpy
import math
import xlsxwriter

class Calendario():
	def __init__(self,originador,partidos,numero):
		self.numero = numero
		self.originador = originador
		self.partidos = partidos
		self.calendario = self.generar_calendario()
		self.distancias = None
		self.distanciasEquipos = None
		self.media = 0
		self.desviacion = 0
		self.total = 0

	def es_valido(self):
		isValid = True
		visitante = 0
		doble = 0
		#print(self.calendario)
		for fila in self.calendario:
			#print(fila)
			for partido in fila:				
				if partido == 1:	
					visitante = visitante + 1
				if partido == 2:
					doble = doble + 1
			#print(visitante == 1)
			#print(doble == 2)
			#print (visitante == 1 and doble == 2)
			if visitante == 1 and doble == 2:
				pass
			else:
				isValid = False
				break
			visitante = 0
			doble = 0
			
		return isValid
		
	def generar_calendario(self):
		matriz = numpy.zeros((5,5),dtype=numpy.int)
		#print("MATRIZ BASE")
		
		for i in range(5):
			matriz[i][self.partidos[i][0]] = 2
			matriz[i][self.partidos[i][1]] = 2
			
		#print(matriz)
		
		
		k = 0
		for i in range(0,5):
			for j in range(i+1,5):
				if matriz[i][j] != 2:
					#print(str(i))
					#print(str(j))
					matriz[i][j] = self.originador[k]
					matriz[j][i] = -1*(self.originador[k]-1)
					k = k+1	
	
		
		#print("MATRIZ FINAL")
		#print(matriz)
			
		return matriz
		
	def generar_resultados(self,distanciaCiudades):

		self.distancias = numpy.zeros((5,5),dtype=numpy.int)
	
		for i in range(5):
			for j in range(5):
				if self.calendario[i][j] == 2:
					self.distancias[i][j] = 1
				else:
					self.distancias[i][j] = self.calendario[i][j]	
				self.distancias[i][j] = self.distancias[i][j]*distanciaCiudades[i][j]

		self.distanciasEquipos = numpy.zeros(5)		
		for i in range(5):
			for j in range(5):			
				self.distanciasEquipos[i] = self.distanciasEquipos[i] + self.distancias[i][j]
				self.total = self.total + self.distancias[i][j]

		
		self.media = sum(self.distanciasEquipos) / float(len(self.distanciasEquipos))
		

		for distancia in self.distanciasEquipos:
			self.desviacion = self.desviacion + (distancia-self.media)*(distancia-self.media)

		self.desviacion = math.sqrt(self.desviacion/5)

		

		
	def imprime_resultado(self,workbook,worksheet,ciudades):
		
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
		
		worksheet.write(0,0,'Enfrentamientos',bold)
		
		filaActual = 3
		for i in range(5):
			worksheet.write(1,i,ciudades[i].nombre,bold)
			posicion = 0
			for j in range(5):				
				if i is not j:
					if self.calendario[i][j] == 2:
						enfrentamiento = 'Doble vs '
					elif self.calendario[i][j] == 0:
						enfrentamiento = 'Casa vs '
					else:
						enfrentamiento = 'Fuera vs '
					enfrentamiento = enfrentamiento + ciudades[j].nombre			
					worksheet.write(2+posicion,i,enfrentamiento)		
					posicion = posicion +1				
			filaActual = filaActual+1		
		
		

		filaActual = filaActual+2		
		worksheet.write(filaActual-1,7,'Dist Km')
		title = workbook.add_format({'bold':True})
		title.set_bg_color('000000')
		title.set_font_size(11)
		title.set_font_color('white')

		for i in range(5):
			worksheet.write(filaActual-1,i+1,ciudades[i].nombre,title)
			worksheet.write(filaActual+i,0,ciudades[i].nombre,title)
			for j in range(5):
				if i == j:
					worksheet.write(filaActual+i,j+1,'X')
				else:
					worksheet.write(filaActual+i,j+1,self.distancias[i][j])
			worksheet.write(filaActual+i,7,self.distanciasEquipos[i])

		worksheet.write(17,0,'Media por equipo',bold)
		worksheet.write(17,1,str(round(self.media,2))+' kms')		
		worksheet.write(18,0,'Klm entre todos',bold)
		worksheet.write(18,1,str(self.total)+' kms')	
		worksheet.write(19,0,'Desviacion',bold)
		worksheet.write(19,1,str(self.desviacion)+' kms')	


