# -*- coding: utf-8 -*-
class Equipo():
	def __init__(self,nombre,iniciales,indice):
		self.nombre = nombre
		self.iniciales = iniciales
		self.indice = int(indice)
		
	def __str__(self):
		return self.nombre