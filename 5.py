 # -*- coding: utf-8 -*-

print "repaso"

class naruto():
 	def sasuke(self):
 		cantidad = int(raw_input("cantidad de numeros:"))
 		return cantidad

 	def sakura(self, cantidad):
 		vector = []
 		vector1 = []
 		contador = 0
 		data = []
 		for i in range(cantidad):
 			numero = int(raw_input("cual es el numero:"))
 			vector.insert(i, numero)
 			par = numero % 2
 			contador = contador + numero
 			if par == 0:
 				vector1.insert(i, numero)
 		data = [vector, vector1, contador, cantidad]
 		return data

 	def hinata(self, data):
 		promedio = 0
 		manzana = data[0]
 		pera = data[1]
 		banano = data[2]
 		cantidad = data[3]
 		promedio = banano / cantidad
 		print "este es el vector de los numeros inglesados:", manzana
 		print "este es el vector de los numeros pares:", pera
 		print "este es la suma de lois numeros dados:", banano
 		print "este es el promedio de los numeros inglesados:", promedio

hinata = naruto()
itachi = hinata.sasuke()
sasuke = hinata.sakura(itachi)
naruto = hinata.hinata(sasuke)
