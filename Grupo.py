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
		for equipo in self.equipos:
			worksheet.write(2+i,0,equipo.nombre,bold)
			
			i= i+1
		
		worksheet.write(7,0,'Grupo',bold)	
		filaActual = 8
			
		title = workbook.add_format({'bold':True})
		title.set_bg_color('000000')
		title.set_font_size(11)
		title.set_font_color('white')
		
		jornada = 0
		i=0
		worksheet.write(filaActual, 0, "Jornada 1")
		worksheet.write(filaActual+1, 0, self.equipos[0].nombre)
		worksheet.write(filaActual+1, 1, self.equipos[1].nombre)
		worksheet.write(filaActual+2, 0, self.equipos[2].nombre)
		worksheet.write(filaActual+2, 1, self.equipos[3].nombre)
		
		filaActual = filaActual + 3
		
		worksheet.write(filaActual, 0, "Jornada 2")
		worksheet.write(filaActual+1, 0, self.equipos[3].nombre)
		worksheet.write(filaActual+1, 1, self.equipos[0].nombre)
		worksheet.write(filaActual+2, 0, self.equipos[1].nombre)
		worksheet.write(filaActual+2, 1, self.equipos[2].nombre)
		
		filaActual = filaActual + 3
		worksheet.write(filaActual, 0, "Jornada 3")
		worksheet.write(filaActual+1, 0, self.equipos[0].nombre)
		worksheet.write(filaActual+1, 1, self.equipos[2].nombre)
		worksheet.write(filaActual+2, 0, self.equipos[1].nombre)
		worksheet.write(filaActual+2, 1, self.equipos[3].nombre)
		
		filaActual = 0
		worksheet.write(filaActual,7,'Media por equipo',bold)
		worksheet.write(filaActual,8,str(self.media)+' kms')	
		worksheet.write(filaActual+1,7,'Klm entre todos',bold)
		worksheet.write(filaActual+1,8,str(self.total)+' kms')	
		worksheet.write(filaActual+2,7,'Desviacion',bold)
		worksheet.write(filaActual+2,8,str(self.desviacion)+' kms')
		
		for i in range(len(self.equipos)):
			worksheet.write(filaActual+i,9,self.equipos[i].indice)
			worksheet.write(filaActual+i,10,self.equipos[i].nombre)
			worksheet.write(filaActual+i,11, self.distanciasEquipos[i])

			