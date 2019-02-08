# -*- coding: utf-8 -*-
class Grupo():
	def __init__(self,equipos_grupo_a,equipos_grupo_b):
		self.equipos_grupo_a = equipos_grupo_a
		self.equipos_grupo_b = equipos_grupo_b
		
		
		self.calendario_grupo_a = Calendario().obtener_calendario_grupo_a()
		self.calendario_grupo_b =  Calendario().obtener_calendario_grupo_b()
		
	def __str__(self):
		string = "Grupo A \n"
		
		for equipo in self.equipos_grupo_a:
			string = string + equipo.nombre + "\n"
		
		string = string + "Calendarios \n"
		for calendario in self.calendario_grupo_a:
			string = string 
			string = string + self.equipos_grupo_a[calendario[0]].nombre + "-" + self.equipos_grupo_a[calendario[1]].nombre
			 
			string = string + self.equipos_grupo_a[calendario[2]].nombre + "-" + self.equipos_grupo_a[calendario[3]].nombre
		
		string =  string + "Grupo B \n"
		
		return string 
			
		
	def __repr__(self):
		return str(self)

class Calendario():
	def __init__(self):
		pass
		
	def obtener_calendario_grupo_a(self):
		calendario = dict()
		
		calendario["Jornada 1"] =
		(
			('Partido 1-2',[0,1,2,3]),
			('Partido 3-4',[0,2,3,1])
		)
		calendario['Jornada 2'] =
		(
			('Partido 1-2',[0,4,2,3]),
			('Partido 3-4',[0,3,4,2])
							
		)
		calendario['Jornada 3'] =
		(
			('Partido 1-2',[0,1,3,4]),
			('Partido 3-4',[0,3,4,1])
		)
		calendario['Jornada 4'] =
		( 
			('Partido 1-2',[0,4,1,2]),
			('Partido 3-4',[0,2,1,4])
		)
		calendario['Jornada 5'] =
		(
			('Partido 1-2',[1,2,3,4]),
			('Partido 3-4',[1,3,2,4])
		)
		return calendario
	
	def obtener_calendario_grupo_b():
		return {
		
		
			{'Jornada 1', (('Partido 1-2',[0,1,2,3]),
							('Partido 3-4',[3,0,1,2]))
			
			},
			{'Jornada 2', (('Partido 1-2',[0,2,1,3]),
							('Partido 3-4',[3,0,2,1]))				
			},
			
			{'Jornada 3', (('Partido 1-2',[0,2,3,1]),
							('Partido 3-4',[1,0,2,3]))				
			},
			{'Jornada 4', (('Partido 1-2',[0,2,3,1]),
							('Partido 3-4',[1,0,2,3]))
			}
		}	
	
		
