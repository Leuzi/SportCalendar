import numpy
import math
from itertools import permutations

class AlgoritmoTresEquipos():
	def __init__(self,calendario):
		self.calendario = calendario
		self.matriz = self.generar_matriz()
		self.calendarios = self.generar_partidos()

	def generar_partidos(self):

		combinaciones = []		

		for combinacion in permutations(self.calendario.equipos):
			if self.es_valido(combinacion):
				combinaciones.append(combinacion)
		
		
		return self.generar_resultados(combinaciones)

	def es_valido(self,combinacion):
		
		if combinacion[0].indice < combinacion[1].indice and  combinacion[1].indice < combinacion[2].indice:
			return True
			
		return False
		
	def generar_matriz(self):
		
		matriz = numpy.zeros((3,3),dtype=numpy.int)
		
		matriz[0][1]=1
		matriz[0][2]=2
		matriz[1][0]=2
		matriz[1][2]=1
		matriz[2][0]=1
		matriz[2][1]=2
						
		return matriz
		
	def generar_resultados(self,combinaciones):

		self.distancias = numpy.zeros((3,3),dtype=numpy.int)
	
		for i in range(6):
			for j in range(6):
				if self.calendario[i][j] == 2:
					self.distancias[i][j] = 1
				else:
					self.distancias[i][j] = self.calendario[i][j]	
				self.distancias[i][j] = self.distancias[i][j]*distanciaCiudades[i][j]

		self.distanciasEquipos = numpy.zeros(6)		
		for i in range(6):
			for j in range(6):			
				self.distanciasEquipos[i] = self.distanciasEquipos[i] + self.distancias[i][j]
				self.total = self.total + self.distancias[i][j]

		
		self.media = sum(self.distanciasEquipos) / float(len(self.distanciasEquipos))
		

		for distancia in self.distanciasEquipos:
			self.desviacion = self.desviacion + (distancia-self.media)*(distancia-self.media)

		self.desviacion = math.sqrt(self.desviacion/5)


