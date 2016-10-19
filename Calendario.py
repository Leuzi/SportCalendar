import numpy

class Calendario():
	def __init__(self,originador,partidos):
		self.originador = originador
		self.partidos = partidos
		self.calendario = self.generar_calendario()
		self.valido = self.es_valido()
		self.media = 0
		self.desviacion = 0

	def es_valido(self):
		local = 0
		doble = 0
		for fila in self.calendario:
			for partido in fila:
				if partido == 1:	
					local = local + 1
				if partido == 2:
					doble = doble + 1

			if local is not 2 or doble is not 1 :
				return False
			local = 0
			doble = 0
			
		return True
		
	def generar_calendario(self):
		matriz = numpy.zeros((6,6),dtype=numpy.int)
		
		for equipo1,equipo2 in self.partidos:
			matriz[equipo1.indice][equipo2.indice] = 2
			matriz[equipo2.indice][equipo1.indice] = 2
		
		k = 0
		
		for i in range (0,6):
			for j in range(i+1,6):
				if matriz[i][j] != 2:
					matriz[i][j] = self.originador[k]
					matriz[j][i] = -1*(self.originador[k]-1)
					k = k+1		
					
		return matriz
		
	def imprimir_calendario(self):
		
		print('------------------------------')
		print('Enfrentamientos dobles')
		for equipo1,equipo2 in self.partidos:
			print(equipo1.nombre+' contra '+ equipo2.nombre)
		
		for i in range(0,6):
			for j in range(i+1,6):
				
			
			