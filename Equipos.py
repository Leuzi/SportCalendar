class Equipo():
	def __init__(self,nombre,iniciales,indice):
		self.nombre = nombre
		self.indice = int(indice)
		self.iniciales = iniciales
		self.distancias = dict()
	
	def __str__(self):
		result = self.nombre + '\n'
		return result
	
	def ponDistancias(self,equipos,distancias):
		for equipo in equipos:		
			self.distancias[equipo] = distancias[self.indice][equipo.indice]
	
	__repr__ = __str__
	
	
