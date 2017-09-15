from graphviz import Source
from .NodoAVL import NodoAVL

import hashlib
import time

class AVL(object):
	def __init__(self):
		self.raiz = None
		self.h = False
		self.grafo = ""
		self.xmlArt = ""
		self.clave = 0
		self.idNode = 0
#***********************************************************************************#
	def obtenerASCII(self, nombre):
		self.clave = 0
		for caracter in nombre:
			self.clave += ord(caracter)
		#print(str(self.clave) + "--" + nombre)
		return self.clave
#************************************ ROTACIONES ***********************************#
	def rotacionIzquierda(self, n, n1):
		n.hijoIzq = n1.hijoDer
		n1.hijoDer = n
		if n1.fe == -1:
			n.fe = 0
			n1.fe = 0
		else:
			n.fe = -1
			n1.fe = 1
		return n1

	def rotacionDerecha(self, n , n1):
		n.hijoDer = n1.hijoIzq
		n1.hijoIzq = n
		if n1.fe == 1:
			n.fe = 0
			n1.fe = 0
		else:
			n.fe = 1
			n1.fe = -1
		return n1

	def rotacionDobleIzquierda(self, n, n1):
		n2 = n1.hijoDer
		n.hijoIzq = n2.hijoDer
		n2.hijoDer = n
		n1.hijoDer = n2.hijoIzq
		n2.hijoIzq = n1
		if n2.fe == 1:
			n1.fe = -1
		else:
			n1.fe = 0
		if n2.fe == -1:
			n.fe = 1
		else:
			n.fe = 0
		n2.fe = 0
		return n2

	def rotacionDobleDerecha(self, n, n1):
		n2 = n1.hijoIzq
		n.hijoDer = n2.hijoIzq
		n2.hijoIzq = n
		n1.hijoIzq = n2.hijoDer
		n2.hijoDer = n1
		if n2.fe == 1:
			n.fe = -1
		else:
			n.fe = 0
		if n2.fe == -1:
			n1.fe = 1
		else:
			n1.fe = 0
		n2.fe = 0
		return n2
#***********************************************************************************#
#************************************ INSERCIÓN ************************************#
	def insertar(self, nombre, extension, raiz):
		if raiz == None:
			raiz = NodoAVL(nombre, extension)
			self.h = True
		elif nombre < raiz.nombre:
			raiz.hijoIzq = self.insertar(nombre, extension, raiz.hijoIzq)
			if self.h == True:
				if raiz.fe == 1:
					raiz.fe = 0
					self.h = False
				elif raiz.fe == 0:
					raiz.fe = -1
				elif raiz.fe == -1:
					n1 = raiz.hijoIzq
					if n1.fe == (-1):
						raiz = self.rotacionIzquierda(raiz, n1)
					else:
						raiz = self.rotacionDobleIzquierda(raiz, n1)
					self.h = False
		elif nombre > raiz.nombre:
			raiz.hijoDer = self.insertar(nombre, extension, raiz.hijoDer)
			if self.h == True:
				if raiz.fe == 1:
					n1 = raiz.hijoDer
					if n1.fe == 1:
						raiz = self.rotacionDerecha(raiz, n1)
					else:
						raiz = self.rotacionDobleDerecha(raiz, n1)
					self.h = False
				elif raiz.fe == 0:
					raiz.fe = 1
				elif raiz.fe == -1:
					raiz.fe = 0
					self.h = False
		else:
			print ("Clave repetida")
		return raiz

	def insertarAVL(self, nombre, extension):
		self.h = False
		self.raiz = self.insertar(nombre, extension, self.raiz)
		#print (str(self.idNode) + "--" + nombre)
#***********************************************************************************#
#************************************ BÚSQUEDA *************************************#
	def buscar(self, nombre, raiz):
		if raiz == None:
			print ("Nodo no existe")
		elif raiz.nombre == nombre:
			print ("Nodo: " + raiz.getNombre() + " encontrado")
		elif raiz.nombre < nombre:
			self.buscar(nombre, raiz.hijoDer)
		else:
			self.buscar(nombre, raiz.hijoIzq)

	def buscarAVL(self, nombre):
		self.buscar(nombre, self.raiz)
#***********************************************************************************#
#********************************** MODIFICACIÓN ***********************************#
	"""def modificar(self, idNode, descA, raiz):
		if raiz == None:
			print ("Nodo no existe")
		elif raiz.idNode == idNode:
			print ("Nodo Encontrado: " + idNode + "--" + raiz.getDescripcion())
			raiz.descripcion = descA
			print ("Nodo Modificado: " + idNode + "--" + raiz.getDescripcion())
			return "Nodo Modificado: " + idNode + "--" + raiz.getDescripcion()
		elif raiz.idNode < idNode:
			self.modificar(idNode, descA, raiz.hijoDer)
		else:
			self.modificar(idNode, descA, raiz.hijoIzq)

	def modificarAVL(self, idNode, descA):
		self.modificar(idNode, descA, self.raiz)"""
#***********************************************************************************#
#********************************** DISPONIBILIDAD *********************************#
	"""def cambiarEstado(self, idNode, raiz):
		if raiz == None:
			print ("Nodo no existe")
		elif raiz.idNode == idNode:
			print ("Estado Encontrado: " + idNode + "--" + str(raiz.getDisponibilidad()))
			raiz.rentado = True
			print ("Estado Modificado: " + idNode + "--" + str(raiz.getDisponibilidad()))			
		elif raiz.idNode < idNode:
			self.cambiarEstado(idNode, raiz.hijoDer)
		else:
			self.cambiarEstado(idNode, raiz.hijoIzq)

	def cambiarEstadoAVL(self, idNode):
		self.cambiarEstado(idNode, self.raiz)"""
#***********************************************************************************#
#*********************************** ELIMINACIÓN ***********************************#
	def eliminar(self, nombre, extension, raiz):
		if raiz == None:
			print ("Nodo no existe")
		elif nombre < raiz.nombre:
			raiz.hijoIzq = self.eliminar(nombre, extension, raiz.hijoIzq)
			if self.h == True:
				raiz = self.equilibrar1(raiz)
		elif nombre > raiz.nombre:
			raiz.hijoDer = self.eliminar(nombre, extension, raiz.hijoDer)
			if self.h == True:
				raiz = self.equilibrar2(raiz)
		else:
			q = raiz
			if q.hijoIzq == None:
				raiz = q.hijoDer
				self.h = True
			elif q.hijoDer == None:
				raiz = q.hijoIzq
				self.h = True
			else:
				raiz.hijoIzq = self.reemplazar(q, q.hijoIzq)
				if self.h:
					raiz = self.equilibrar1(raiz)
			q == None		
		return raiz

	def eliminarAVL(self, nombre, extension):
		self.h = False
		self.raiz = self.eliminar(nombre, extension, self.raiz)
		#self.enOrden(self.raiz)

	def reemplazar(self, n, actual):
		if actual.hijoDer != None:
			actual.hijoDer = self.reemplazar(n, actual.hijoDer)
			if self.h:
				actual = self.equilibrar2(actual)
		else:
			n.nombre = actual.nombre
			n = actual
			actual = actual.hijoIzq
			self.h = True
		return actual

	def equilibrar1(self, n):
		if n.fe == -1:
			n.fe = 0
		elif n.fe == 0:
			n.fe = 1
			self.h = False
		elif n.fe == 1:
			n1 = n.hijoDer
			if n1.fe >= 0:
				if n1.fe == 0:
					self.h = False
				n = self.rotacionDerecha(n, n1)
			else:
				n = self.rotacionDobleDerecha(n, n1)
		return n

	def equilibrar2(self, n):
		if n.fe == -1:
			n1 = n.hijoIzq
			if n1.fe <= 0:
				if n1.fe == 0:
					self.h = False
				n = self.rotacionIzquierda(n, n1)
			else:
				n = self.rotacionDobleIzquierda(n, n1)
		elif n.fe == 0:
			n.fe = -1
			self.h = False
		elif n.fe == 1:
			n.fe = 0
		return n
#***********************************************************************************#
#************************************ RECORRIDOS ***********************************#
	def preOrden(self, nodo):
		if nodo != None:
			print(nodo.nombre + ",")
			self.preOrden(nodo.hijoIzq)
			self.preOrden(nodo.hijoDer)
	def preOrdenAVL(self):
		self.preOrden(self.raiz)
	
	def enOrden(self, nodo):
		if nodo != None:
			self.enOrden(nodo.hijoIzq)
			print("--" + nodo.nombre + ",")
			self.enOrden(nodo.hijoDer)
	def enOrdenAVL(self):
		self.enOrden(self.raiz)

	def postOrden(self, nodo):
		if nodo != None:
			self.postOrden(nodo.hijoIzq)
			self.postOrden(nodo.hijoDer)
			print(nodo.nombre + ",")
	def postOrdenAVL(self):
		self.postOrden(self.raiz)
#***********************************************************************************#
#************************************ GRAFICAR *************************************#
	def graficarNodo(self, nodo):
		if nodo != None:
			i = self.obtenerASCII(nodo.nombre)
			self.grafo += "\"" + str(i) + "\"[label=\"<f0> Izq|<f1>" 
			#self.grafo += "ID: " + nodo.getID() ** esta estaba comentada.?
			self.grafo += "Nombre: " + nodo.getNombre() + "\\nExtension: " + nodo.getExtension()
			self.grafo += "|<f2> Der\"]; \n"
			

			if nodo.hijoIzq != None:
				idIzq = self.obtenerASCII(nodo.hijoIzq.nombre)	
				self.grafo += "\"" + str(i) + "\":f0 -> "
				self.grafo += "\"" + str(idIzq) + "\":f1 ;\n"
				self.graficarNodo(nodo.hijoIzq)
				
			if nodo.hijoDer != None:
				self.grafo += "\"" + str(i) + "\":f2 -> " 
				idDer = self.obtenerASCII(nodo.hijoDer.nombre)
				self.grafo += "\"" + str(idDer) + "\":f1 ;\n"
				self.graficarNodo(nodo.hijoDer)

	def graficarAVL(self):
		self.grafo = "digraph G {node[shape=record, height=0.1];\n"
		self.grafo += "{ \n"

		if self.raiz == None:
			print ("La raiz es nula")
			self.grafo += "arbolvacio [label = \"Arbol Vacio\",shape=record];\n"
		else:
			self.graficarNodo(self.raiz)
		
		self.grafo += "} \n"
		self.grafo += "labelloc=\"t\";\nlabel=\" AVL\";}"
		print(self.grafo)
		src = Source(self.grafo)
		src.format = "png"
		src.render('test-output/AVLTree', view = True)
		#return self.grafo
#***********************************************************************************#
#*********************** XML AVL **********************#
	def xmlNodo(self, nodo):
		if nodo != None:
			i = nodo.getID()

			self.xmlArt += "<articulo>\n"
			self.xmlArt += "<id> " + nodo.getID() + " </id>\n"
			self.xmlArt += "<nombre> " + nodo.getNombre() + " </nombre>\n"
			self.xmlArt += "<descripcion> " + nodo.getDescripcion() + " </descripcion>\n"
			self.xmlArt += "<estado> " + str(nodo.getDisponibilidad()) + " </estado>\n"			
			self.xmlArt += "</articulo>\n"

			if nodo.hijoIzq != None:
				idIzq = nodo.hijoIzq.getID()
				self.xmlNodo(nodo.hijoIzq)

			if nodo.hijoDer != None:
				idDer = nodo.hijoDer.getID()
				self.xmlNodo(nodo.hijoDer)

	def xmlAVL(self):

		if self.raiz != None:
			self.xmlArt += "<articulos>\n"
			self.xmlNodo(self.raiz)
			self.xmlArt += "</articulos>\n"

		#print(self.xmlArt)
		return str(self.xmlArt)	
		#src = Source(self.grafo)
		#src.format = "png"
		#src.render('test-output/AVLTree', view = True)
#******************************************************#