class Coche():

	def __init__(self):
		self.largoChasis=380
		self.anchoChasis=170
		self.ruedas=4
		self.enmarcha= False

	def arrancar(self, arrancando):
		self.enmarcha= arrancando

	def estado(self):
		if self.enmarcha:
			return "El coche está en marcha"
		else:
			return "El coche está parado"


miCoche=Coche() 
(miCoche.arrancar(True))
print(miCoche.estado())

print("***********************Agregamos otro coche************************")


miCoche2=Coche() 

print(miCoche2.estado())
#----------------------#