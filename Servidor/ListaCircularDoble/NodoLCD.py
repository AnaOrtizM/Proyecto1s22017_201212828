class NodoLCD(object):
	def __init__ (self, indice, name, password):
		self.indice = indice
		self.name = name
		self.password = password
		self.anterior = None
		self.siguiente = None

	def getIndice(self):
		return self.indice

	def getName(self):
		return self.name

	def getPassword(self):
		return self.password