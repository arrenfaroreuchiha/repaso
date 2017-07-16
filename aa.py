# -*- coding: utf-8 -*-

class andres():
	def john(self):
		cantidad = int(raw_input("Cantidad de numeros:"))
		contador = 0
		lista = [cantidad, contador]
		return lista

	def eduar(self, lista):
		cantidad = lista[0]
		contador = lista[1]
		matrix = []
		vector = []
		for i in range(cantidad):
			matrix.append([])
			for x in range(cantidad):
				numero = int(raw_input("Cual es el numero:"))
				contador = contador + numero
				matrix[i].append(numero)
				vector.insert(i, numero)
				vector.sort()

		array = [vector, matrix, cantidad, contador]
		return array

	def eduardo(self, array):
		matrix = array[1]
		vector = array[0]
		cantidad = array[2]
		contador = array[3]
		print "\n"
		print "Esta es la matrix."
		for i in range(cantidad):
			print matrix[i]
		print "\n"

		
		print "Este es el vector."
		print vector
		print "\n"
		print "Esta es la suma de los numeros:", contador
		print "Este es el numero menor que hay en la matrix:", min(vector)
		print "Este es el numero mayor que hay en la matrix:", max(vector)
		print "Este es la cantidad de numeros que hay en la matrix:", len(vector)
		print "\n"


apola = andres()

def main():
	miguel = apola.john()
	felipe = apola.eduar(miguel)
	nataly = apola.eduardo(felipe)