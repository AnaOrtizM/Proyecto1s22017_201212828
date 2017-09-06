from graphviz import Source
from .NodoLCD import NodoLCD

class ListaCircularDoble(object):
	
	def __init__(self):
		self.inicio = None
		self.fin = None
		self.indice = 0
		self.grafo = ""
		
	def estaVacia(self):
		if self.inicio == None:
			return True
		else:
			return False

	def insertar(self, name, password):
		if len(password) >= 4:

			nuevo = NodoLCD(self.indice, name, password)
			
			if self.estaVacia() == True:
				self.inicio = nuevo
				self.inicio.siguiente = self.inicio
				self.inicio.anterior = self.inicio
			else:
				actual = self.inicio
				while actual.siguiente != self.inicio:
					actual = actual.siguiente
					pass
				actual.siguiente = nuevo
				nuevo.anterior = actual		
				nuevo.siguiente = self.inicio
				self.inicio.anterior = nuevo
				self.fin = nuevo

			self.indice += 1
		else:
			print (str(name) + " Contraseña no valida. Debe ser mayor a 4 caracteres")

	def buscar(self, name):
		if self.estaVacia() == True:
			print ("Lista Circular Vacia")
		else:
			temp = self.inicio
			while True:
				if temp.getName() == name:
					print ("Nombre encontrado: " + temp.getName())
					return temp
				temp = temp.siguiente
				if temp == self.inicio:
					break
		return None

	def mostrar(self):
		if self.estaVacia() == True:
			print ("Lista Circular Vacia")
		else:
			temp = self.inicio
			while True:
				print (temp.getName() , "<->" , temp.siguiente.getName())
				temp = temp.siguiente
				if temp == self.inicio:
					break

	def eliminar(self, name):
		if self.estaVacia() == False:
			temp = self.inicio
			temp2 = None

			while True:
				if temp.getName() == name:
					if temp2 == None:
						if temp.siguiente == self.inicio:
							self.inicio = None
							print ("Usuario eliminado")
							return
						else:
							temp2 = temp.anterior
							temp2.siguiente = temp.siguiente
							temp = temp.siguiente
							temp.anterior = temp2
							self.inicio = temp
							temp2 = None
							print ("Usuario eliminado")
							return
					else:
						if temp == self.fin:
							self.fin = temp2
						temp.anterior = None
						temp2.siguiente = temp.siguiente
						temp = temp.siguiente
						temp.anterior = temp2
						print ("Usuario eliminado")
						return
				else:
					temp2 = temp
					temp = temp.siguiente

				if temp == self.inicio:
					break
		else:
			print ("Lista Circular Vacia")

	def verificarUsuario(self, name, password):
		usuario = self.buscar(name)
		if (name == usuario.getName()) and ( password == usuario.getPassword()):
			print ("Usuario " + usuario.getName() + " correcto")
			return True
		else:
			print ("Usuario " + usuario.getName() + " incorrecto")
			return False

	def graficar(self):
		self.grafo = "digraph G {\n" + "node [shape = record,height=.1];  {\n"

		if self.estaVacia() == True:
			self.grafo += "\"ListaVacia\" [label = \"Lista Circular Vacia\"]"
		else:
			temp = self.inicio
			i = 1
			while True:
				self.grafo += "\"" + str(i) + "\" [label = \"" + "Nombre: " + temp.getName() 
				self.grafo += "\\nContraseña: " + temp.getPassword() + "\"];\n"
				temp = temp.siguiente
				if temp == self.inicio:
					self.grafo +=  "\"" + str(i) + "\" -> \"" + str(1) + "\" ;\n"
					self.grafo +=  "\"" + str(1) + "\" -> \"" + str(i) + "\" ;\n"
				else:
					self.grafo += "\"" + str(i + 1) + "\" [label = \"" + "Nombre: " + temp.siguiente.getName() 
					self.grafo += "\\nContraseña: " + temp.siguiente.getPassword() + "\"];\n"

					self.grafo +=  "\"" + str(i) + "\" -> \"" + str(i + 1) + "\" ;\n"
					self.grafo +=  "\"" + str(i + 1) + "\" -> \"" + str(i) + "\" ;\n"				
				i = i + 1
				if (temp == self.inicio):
					break

		self.grafo += "} labelloc=\"t\"; label=\" LISTA CIRCULAR DOBLE\";}"
		print(self.grafo)
		src = Source(self.grafo)
		src.format = "png"
		src.render('test-output/ListaCircularDoble', view = True)
#**************************************************************************#