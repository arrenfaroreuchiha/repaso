# -*- coding: utf-8 -*-

print "De matrix a vector"

class base():
	def entra(self):
		cantidad = int(raw_input("cantidad:"))
		return cantidad

	def procesa(self, cantidad):
		matrix = []
		vector = []
		matris = 0
		vector1 = 0
		total = []
		for i in range(cantidad):
			matrix.append([])
			for j in range(cantidad):
				numero = int(raw_input("numeros:"))
				matrix[i].append(numero)
				vector.insert(i, numero)
				vector.sort()
				matris = matrix
				vector1 = vector
		total = [matris, vector1]
		return total

	def sale(self, total):
		a = total[0]
		b = total[1]
		print "esta es la matix:", a
		print "eset es el vector:", b

base = base()
data = base.entra()
calcula = base.procesa(data)
total = base.sale(calcula)
