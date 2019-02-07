# -*- coding: utf-8 -*-
class Equipo():
	def __init__(self,nombre,iniciales,ciudad,indice):
		self.nombre = nombre
		self.iniciales = iniciales
		self.ciudad = ciudad
		self.indice = int(indice)
		
	def __str__(self):
		return self.nombre
		
	def __repr__(self):
		return str(self)