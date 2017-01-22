# -*- coding: utf-8 -*-

class a():
	def cantidadNumeros(self):
		cantidad = int(raw_input("cantidad de numeros:"))
		return cantidad

	def vector(self, cantidad):
		vector = []
		data = []
		suma = 0
		for i in range(cantidad):
			numero = int(raw_input("cual es el numero:"))
			vector.insert(i, numero)
			# john = vector
			suma = suma + numero

		data = [vector, suma, cantidad]
		return data

	def promedio(self, vector):
		v = vector[0]
		suma = vector[1]
		cantidad = vector[2]
		promedio = suma / cantidad
		print "este es el vector", v
		print "esta es la suma", suma
		print "este es el promedio", promedio

objeto = a()

cantidad = objeto.cantidadNumeros()
vector = objeto.vector(cantidad)
#vector, suma, cantidad
# objeto.promedio(vector[0], vector[1], vector[2])
objeto.promedio(vector)

		
