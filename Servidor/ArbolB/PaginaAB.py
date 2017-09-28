from .NodoAB import NodoAB

class PaginaAB(object):
	def __init__(self):
		self.claves = []
		self.ramas = []
		self.sizeC = 4
		self.sizeR = 5
		self.contador = 0
		self.idPage = 0

		for i in range(self.sizeC):
			self.claves.append(None)

		for i in range(self.sizeR):
			self.ramas.append(None)

		#self.claves[0] = clave
		#self.contador += 1
		
	def estaVacia(self):
		if self.contador == 0:
			return True
		else:
			return False

	def estaLlena(self):
		if self.contador > 3:
			return True
		else:
			return False

	def insertarOrdenado(self, clave, pos, ramaDer):
		for i in range(self.contador, pos, -1):
			self.claves[i] = self.claves[i - 1]
			self.ramas[i + 1] = self.ramas[i]
		self.claves[pos] = clave
		self.ramas[pos + 1] = ramaDer
		self.contador += 1