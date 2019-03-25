# -*- coding: utf-8 -*-
class Grupo():
	def __init__(self,equipos_grupo_a,equipos_grupo_b):
		self.equipos_grupo_a = list(equipos_grupo_a)
		self.equipos_grupo_b = list(equipos_grupo_b)
		self.calendario_grupo_a = Calendario().obtener_calendario_grupo_a()
		self.calendario_grupo_b =  Calendario().obtener_calendario_grupo_b()
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
		string = "Grupo A \n"
		
		for equipo in self.equipos_grupo_a:
			string = string + equipo.nombre + "\n"
		
		string = string + "Calendarios \n"
		i=1
		string =  string + "Grupo A \n"
		for jornada in self.calendario_grupo_a:
			string = string  +"Jornada "+str(i)
			string = string +"Partido 1" + self.equipos_grupo_a[jornada[0]].nombre + "-" + self.equipos_grupo_a[jornada[1]].nombre +"\n"
			 
			string = string +"Partido 2" + self.equipos_grupo_a[jornada[2]].nombre + "-" + self.equipos_grupo_a[jornada[3]].nombre +"\n"
		
			string = string +"Partido 3" + self.equipos_grupo_a[jornada[4]].nombre + "-" + self.equipos_grupo_a[jornada[5]].nombre +"\n"
		
			string = string +"Partido 4" + self.equipos_grupo_a[jornada[6]].nombre + "-" + self.equipos_grupo_a[jornada[7]].nombre +"\n"
		i=1
		string =  string + "Grupo B \n"
		
		for equipo in self.equipos_grupo_b:
			string = string + equipo.nombre + "\n"
			
		for jornada in self.calendario_grupo_b:
			string = string  +"Jornada "+ str(i)
			string = string +"Partido 1" + self.equipos_grupo_b[jornada[0]].nombre + "-" + self.equipos_grupo_b[jornada[1]].nombre +"\n"
			 
			string = string +"Partido 2" + self.equipos_grupo_b[jornada[2]].nombre + "-" + self.equipos_grupo_b[jornada[3]].nombre +"\n"
		
			string = string +"Partido 3" + self.equipos_grupo_b[jornada[4]].nombre + "-" + self.equipos_grupo_b[jornada[5]].nombre +"\n"
		
			string = string +"Partido 4" + self.equipos_grupo_b[jornada[6]].nombre + "-" + self.equipos_grupo_b[jornada[7]].nombre +"\n"
		
		string =  string + "Media \n"
		
		string =  string + "Total \n"
		
		string =  string + "Desviacion \n"
		
		return string 
			
		
	def __repr__(self):
		return str(self)

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
		
		worksheet.write(0,0,'Grupos',bold)
		worksheet.write(1,0,'Grupo A',bold)
		i=0
		for equipo in self.equipos_grupo_a:
			worksheet.write(2+i,0,equipo.nombre,bold)
			
			i= i+1
			
		worksheet.write(1,5,'Grupo B',bold)
		i=0
		for equipo in self.equipos_grupo_b:
			worksheet.write(2+i,5,equipo.nombre,bold)
			
			i= i+1
		
		worksheet.write(7,0,'Grupo A',bold)	
		filaActual = 8
			
		title = workbook.add_format({'bold':True})
		title.set_bg_color('000000')
		title.set_font_size(11)
		title.set_font_color('white')
		grupo_a_organiza = [0,1,2,3,4]
		grupo_a_descansa = [4,2,1,0,3]
		grupo_b_organiza = [0,1,2,3,4]
		jornada = 0
		i=0
		for jornadas in self.calendario_grupo_a:
			worksheet.write(filaActual+jornada*5,0, "Jornada " +str(jornada+1))
			worksheet.write(filaActual+jornada*5, 1,"Organiza "+ self.equipos_grupo_a[grupo_a_organiza[jornada]].nombre)
			worksheet.write(filaActual+jornada*5, 3,"Descansa "+ self.equipos_grupo_a[grupo_a_descansa[jornada]].nombre)
						
			partidojug = 1
			
			for equipo1, equipo2 in list(zip(jornadas[0::2], jornadas[1::2])):
				"""print(equipo1)
				print(equipo2)
				print(partidojug)"""
				worksheet.write(filaActual+jornada*5+partidojug, 0, self.equipos_grupo_a[equipo1].nombre)
				worksheet.write(filaActual+jornada*5+partidojug, 1, self.equipos_grupo_a[equipo2].nombre)
				partidojug = partidojug + 1
			
			jornada = jornada +1
		jornada = 0
		for jornadas in self.calendario_grupo_b:
			worksheet.write(filaActual+jornada*5,5, "Jornada " +str(jornada+1))
			worksheet.write(filaActual+jornada*5, 6,"Organiza "+ self.equipos_grupo_b[grupo_b_organiza[jornada]].nombre)
			
			
			partidojug = 1
			print(list(zip(jornadas[0::2], jornadas[1::2])))
			for equipo1, equipo2 in list(zip(jornadas[0::2], jornadas[1::2])):
				"""print(equipo1)
				print(equipo2)
				print(partidojug)"""
				worksheet.write(filaActual+jornada*5+partidojug, 5, self.equipos_grupo_b[equipo1].nombre)
				worksheet.write(filaActual+jornada*5+partidojug, 6, self.equipos_grupo_b[equipo2].nombre)
				partidojug = partidojug + 1
			
			jornada = jornada +1
		jornada = 0	
		filaActual = 0
		worksheet.write(filaActual,7,'Media por equipo',bold)
		worksheet.write(filaActual,8,str(self.media)+' kms')	
		worksheet.write(filaActual+1,7,'Klm entre todos',bold)
		worksheet.write(filaActual+1,8,str(self.total)+' kms')	
		worksheet.write(filaActual+2,7,'Desviacion',bold)
		worksheet.write(filaActual+2,8,str(self.desviacion)+' kms')
		
		for i in range(len(self.equipos_grupo_a)):
			worksheet.write(filaActual+i,9,self.equipos_grupo_a[i].nombre)
			worksheet.write(filaActual+i,10,self.distanciasEquipos[self.equipos_grupo_a[i].indice])
		for i in range(len(self.equipos_grupo_b)):
			worksheet.write(filaActual+i+5,9,self.equipos_grupo_b[i].nombre)
			worksheet.write(filaActual+i+5,10,self.distanciasEquipos[self.equipos_grupo_b[i].indice])
		
class Calendario():
	def __init__(self):
		pass
		
	def obtener_calendario_grupo_a(self):
		calendario = [
		[0,1,2,3,0,2,3,1],
		[0,1,3,4,0,3,4,1],
		[0,4,2,3,0,3,4,2],
		[1,2,3,4,1,3,2,4],
		[0,4,1,2,0,2,1,4]
		]
		
		return calendario
	
	def obtener_calendario_grupo_b(self):
		return [
		[0,1,2,3,3,0,1,2],
		[0,2,1,3,3,0,2,1],
		[0,2,3,1,1,0,2,3],
		[0,1,2,3,0,2,3,1]
		]
	
		
