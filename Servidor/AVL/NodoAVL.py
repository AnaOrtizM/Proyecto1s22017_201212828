class NodoAVL(object):
	def __init__(self, nombre, extension):
		#self.idNode = idNode
		self.nombre = nombre
		self.extension = extension
		self.fe = 0
		self.hijoIzq = None
		self.hijoDer = None
	
	#def getID(self):
	#	return self.idNode

	def getNombre(self):
		return self.nombre

	def getExtension(self):
		return self.extension