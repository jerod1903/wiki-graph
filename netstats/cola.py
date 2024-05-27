class Cola:

	def __init__(self):
		self.primero = None
		self.ultimo = None

	def esta_vacia(self):
		return self.primero is None

	def encolar(self,dato):
		nuevo = Nodo(dato)
		if self.ultimo is None:
			self.primero = nuevo
			self.ultimo = nuevo
		else:
			self.ultimo.prox = nuevo
			self.ultimo = nuevo

	def desencolar(self):
		dato=self.primero.dato
		self.primero = self.primero.prox
		if not self.primero:
			self.ultimo = None
		return dato

	def ver_primero(self):
		return self.primero.dato

class Nodo:
	def __init__(self,dato=None,proximo=None):
		self.dato = dato
		self.prox = proximo