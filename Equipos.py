class Equipo():
	def __init__(self,nombre,iniciales,indice):
		self.nombre = nombre
		self.iniciales = iniciales
		self.indice = int(indice)
		
	def __repr__(self):
		return self.nombre
