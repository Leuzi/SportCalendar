import numpy
import math
import xlsxwriter
from Algoritmos import AlgoritmoTresEquipos

class Calendario():
	def __init__(self,equipos):
		self.equipos = equipos
		self.numeroEquipos = len(self.equipos)
		self.calendarios = self.generar_partidos()

	def imprimir_calendarios(self):
		pass
					
	def generar_partidos(self):
		
		if self.numeroEquipos is 3:
			return AlgoritmoTresEquipos.AlgoritmoTresEquipos(self).generar_partidos()
		elif self.numeroEquipos is 4:
			pass
		elif self.numeroEquipos is 5:
			pass
		elif self.numeroEquipos is 6:
			pass
		elif self.numeroEquipos is 7:
			pass
		elif self.numeroEquipos is 8:
			pass




