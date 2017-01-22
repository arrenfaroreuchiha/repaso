cantidad = int(raw_input("cantidad:"))
vector = []
matriz = []
for i in range(cantidad):
	numero = int(raw_input("numero:"))
	elevado = numero ** 2
	vector.insert(i, numero)
	matriz.insert(i, elevado)

print "este es el vector:", vector
print "esta es la elevacion:", matriz