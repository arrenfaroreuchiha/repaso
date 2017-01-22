# -*- coding: utf-8 -*-

class a:
	def naruto(self):
		clave = int(raw_input("inglese la clave:"))
		return clave

	def sasuke(self, clave):
		clave5 = 1222
		while clave5 != clave:
			print "incorrecto"
			clave = int(raw_input("por favor inglese la clave:"))

		if clave5 == clave:
			print "-------------"
			print "Inglesastes correctamente"
			print "segunda clave"
			clave2 = int(raw_input("por favor inglese la segunda clave:"))
			seguir = 1111
			while seguir != clave2:
				print "incorrecto"
				clave2 = int(raw_input("clave por favor:"))

			if seguir == clave2:
				print "----------------------"
				print "Hola Eduardo Bienvenido"


b = a()
itachi = b.naruto()
madara = b.sasuke(itachi)