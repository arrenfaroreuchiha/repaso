# -*- coding: utf-8 -*-

class base():
	def entra(self):
		cantidad = int(raw_input("cantidad:"))
		return cantidad

	def procesa(sefl, cantidad):
		total = []
		vector = []
		matrix = []
		for i in range(cantidad):
			matrix.append([])
			for j in range(cantidad):
				numero = int(raw_input("numero:"))
				matrix[i].append(numero)
				vector.insert(i, numero)
				vector.sort()
		print "este es el vector:", vector
		print "esta es la matrix:", matrix
		print "este es el numero menor de los numeros dados:", min(vector)
		print  "este es el numero mayor de los numeros dados:", max(vector)

		for i in range(cantidad):
			print matrix[i]

data = base()
entra1 = data.entra()
procesa2 = data.procesa(entra1)


			

			
				


