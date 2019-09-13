# -*- coding: utf-8 -*-
class Grupo():
	def __init__(self,equipos):
		self.equipos = list(equipos)
		self.costeGrupo = []
		self.distanciasEquipos = []
		self.desviacion = 0
		self.media = 0
		self.total = 0
			
	def	setCoste(self,costeGrupo,distanciasEquipos,desviacion,media,total):
		self.costeGrupo = costeGrupo
		self.distanciasEquipos = distanciasEquipos
		self.desviacion = desviacion
		self.media = media
		self.total = total
		
	def __str__(self):
		string = "Grupo \n"
		
		for equipo in self.equipos:
			string = string + equipo.nombre + "\n"
		
		string = string + "Calendarios \n"
		i=1		
		
		string =  string + "Media \n"
		string =  string + str(self.media)
		string =  string + "Total \n"
		string =  string + str(self.total)
		
		string =  string + "Desviacion \n"
		string =  string + str(self.desviacion)
		
		return string 
			
		
	def __repr__(self):
		return str(self)

	
