# -*- coding: utf-8 -*-
print "john es loca"

class a():
	def eduardo(self):
		cantidad = int(raw_input("cantidad:"))
		return cantidad

	def andres(sefl, cantidad):
		vector = []
		matriz = []
		resultado = []
		for i in range(cantidad):
			numero = int(raw_input("numero:"))
			elevado = numero ** 2
			vector.insert(i, numero)
			matriz.insert(i, elevado)
		resultado = [vector, matriz]
		return resultado

	def john(self, resultado):
		lee = resultado[0]
		tenten = resultado[1]
		print "este es el vector:", lee
		print "esta es la elevacion:", tenten

b = a()
hinata = b.eduardo()
sakura = b.andres(hinata)
gara = b.john(sakura)


