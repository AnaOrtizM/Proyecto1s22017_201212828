from graphviz import Source
from .NodoAB import NodoAB
from .PaginaAB import PaginaAB

class ArbolB(object):
	def __init__(self):
		self.raiz = PaginaAB()
		self.auxPos = 0
		self.claveMedia = None
		self.auxDe = None
		self.pagina = 0
		self.esta = False
		self.idEncontrados = []
		self.contador = 0
		self.grafo = ""
		
	def buscarNodoEnPagina(self, clave, raiz):
		print("dsf")
		if clave.nombre < raiz.claves[0].nombre :
			self.auxPos = 0
			return False
		else:
			limite = raiz.contador
			while clave.nombre < raiz.claves[limite - 1].nombre:
				limite -= 1
			self.auxPos = limite
			if clave.nombre == raiz.claves[limite - 1].nombre:
				return True
			return False

	def ingresar(self, clave):
		nodo = NodoAB(clave)
		self.insertar(self.raiz, nodo)
		print(clave)

	def insertar(self, raiz, clave):
		if raiz.estaVacia():
			raiz.insertarOrdenado(clave, 0, None)
		else:
			if self.buscarNodoEnPagina(clave, raiz):
				print ("Nodo Repetido")
			else:
				if raiz.ramas[self.auxPos] == None:
					if raiz.estaLlena():
						self.dividirPagina(clave, raiz)
					else:
						raiz.insertarOrdenado(clave, self.auxPos, None)
						self.contador += 1
				else:
					self.insertar(raiz.ramas[self.auxPos], clave)
					self.contador += 1
					if self.claveMedia != None:
						self.buscarNodoEnPagina(self.claveMedia, raiz)
						if raiz.estaLlena():
							self.dividirPagina(self.claveMedia, raiz)
						else:
							raiz.insertarOrdenado(self.claveMedia, self.auxPos, self.auxDe)
							self.claveMedia = None
							self.auxDe = None

	def dividirPagina(self, clave, raiz):
		temp = PaginaAB()

		if self.auxDe == None:
			temp.ramas[0] = None
		else:
			temp.ramas[0] = self.auxDe
		self.auxDe = temp
		posMedia = 0
		if self.auxPos <= 2:
			temp.insertarOrdenado(raiz.claves[2], 0, raiz.ramas[3])
			temp.insertarOrdenado(raiz.claves[3], 1, raiz.ramas[4])
			raiz.contador = 3
			raiz.insertarOrdenado(clave, self.auxPos, None)
			raiz.contador = 2
			self.claveMedia = raiz.claves[2]
		else:
			temp.insertarOrdenado(raiz.claves[3], 0, raiz.ramas[4])
			rama = None if (self.auxPos == 4) else raiz.ramas[3]
			temp.insertarOrdenado(clave, self.auxPos - 3, rama)
			raiz.contador = 2
			self.claveMedia = raiz.claves[2]
			posMedia = 2
		if raiz == self.raiz:
			nuevaRaiz = PaginaAB()
			nuevaRaiz.ramas[0] = raiz
			nuevaRaiz.insertarOrdenado(self.claveMedia, 0, temp)
			self.raiz = nuevaRaiz
			self.auxDe = None
			self.claveMedia = None

	def buscarNodo(self, nombre):
		return buscarNodoB(nombre, self.raiz)
	
	def buscarID(self, n):
		self.idEncontrados = [self.contador]
		self.pagina = 0
		self.buscarIDb(self.raiz, n)

	def buscarIDb(self, raiz, n):
		k = 0
		if raiz != None:
			j = 0
			f = 1
			while j < raiz.contador:
				if n == raiz.claves[j].nombre:
					self.idEncontrados[k] = raiz.claves[j].nombre
					k += 1
				f += 2
				j += 1
			j = 0
			f = 0
			while j <= raiz.contador:
				if raiz.ramas[j] != None:
					self.buscarIDb(raiz.ramas[j], n)
				f += 2
				j += 1
		x = 0
		while self.idEncontrados[x] != None:
			print(self.idEncontrados[k])

	def buscarNodoB(self, nombre, raiz):
		if raiz == None:
			return None
		else:
			if 0 > (nombre > raiz.claves[0].nombre):
				return self.buscarNodoB(nombre, raiz.ramas[0])
			else:
				limite = raiz.contador
				while 0 > (nombre > raiz.claves[limite - 1].nombre):
					limite -= 1
				if nombre == raiz.claves[limite - 1].nombre:
					return raiz.claves[limite - 1]
				return self.buscarNodoB(nombre, raiz.ramas[limite])

	def eliminarNodo(self, nombre):
		tempRaiz = self.raiz
		self.raiz = PaginaAB()
		if nombre != None:
			self.eliminarNodoB(nombre, tempRaiz)

	def eliminarNodoB(self, nombre, raiz):
		if raiz != None:
			for i in range(0,len(raiz.claves)):
				if raiz.claves[i] != None:
					if raiz.claves[i].nombre != nombre:
						self.ingresar(raiz.claves[i].nombre)
			self.contador -= 1
			for i in range(0,len(raiz.ramas)):
				self.eliminarNodoB(nombre, raiz.ramas[i])
#************************************ GRAFICAR *************************************#
	def graficarNodo(self, raiz):
		grafo = ""		
		if raiz != None:
			i = 1
			j = 0

			grafo = "p" + str(self.pagina) + "[label=\"<f0> -  " 
			while j < raiz.contador:
				grafo += "|<f" + str(i) + "> " + "Nombre: " + str(raiz.claves[j].getNombre())
				grafo += " |<f" + str(i + 1) + "> -"
				i += 2
				j += 1
			j = 0
			grafo += "\"]; \n"
			a = self.pagina
			i = 0
			while j <= raiz.contador:
				if raiz.ramas[j] != None:
					self.pagina += 1
					grafo += "p" + str(a) + ":f" + str(i) + " -> " + "p" + str(self.pagina) + ";\n"
					grafo += self.graficarNodo(raiz.ramas[j])
				i += 2
				j += 1
		return grafo

	def graficarNodoAB(self):
		grafo = ""
		pagina = 0
		grafo += self.graficarNodo(self.raiz)
		return grafo

	def graficarAB(self):
		pagina = 0
		self.grafo = "digraph G { node[shape=record, height=0.1];\n"
		self.grafo += "{ \n"
		#print(self.raiz.claves[0].nombre)
		if self.raiz == None:
			print ("La raiz es nula")
			self.grafo += "arbolvacio [label = \"Arbol Vacio\",shape=record];\n"
		else:
			self.grafo += self.graficarNodoAB()
		
		self.grafo += "} \n"
		self.grafo += "labelloc=\"t\";\nlabel=\" ARBOL B\";}"
		print(self.grafo)
		src = Source(self.grafo)
		src.format = "png"
		src.render('test-output/ArbolB', view = True)
		#return self.grafo
#***********************************************************************************#