class Flight:
	def __init__(self,flightdata):
		self.flightdata = flightdata #Flight data es un atributo en forma de diccionario
		
	@classmethod  #Con un método de clase, puede crearse una instancia empleando una función, gracias a que esta no emplea al self
	def fcreator(cls,x,flightRecord =[]):
		for j in range(x):
			data_descriptor = ['Destino','Fecha de salida (DD/MM/AAAA)','Hora de salida (HH:MM)','Hora de llegada (HH:MM)','Costo clase turista','Cupo clase turista','Costo clase negocios','Cupo clase negocios','Costo primera clase','Cupo primera clase']
			data_filler = []
			print(f'\nIngrese datos de vuelo {j+1}:\n')

			for i in range(len(data_descriptor)):
				info = input(f"Ingrese {data_descriptor[i]}: ")
				data_filler.append(info)

			flight_dict = dict(zip(data_descriptor,data_filler))
			fdata = Flight(flight_dict)
			flightRecord.append(fdata)
		return flightRecord

	def displayInfo(self): # Método de objeto, para imprimir los datos de cada vuelo (instancia)
		for k,v in self.flightdata.items():
			print('\t'+k +': ',self.flightdata[k]+'\n')

	@staticmethod # Método estático, para poder manipular la variable obj, puesto que esta es solo un almacenador de instancias, no una instancia en sí.
	def extractObject(element):
		for i in range(len(element)):
			print(f'\nVuelo {i+1}:')
			element[i].displayInfo()  # El método estático, invoca al método de objeto para extraer la info de cada instancia.

n= int(input('Número de vuelos a registrar: '))
print()
obj = Flight.fcreator(n) #Se asigna la lista de objetos a la variable obj
Flight.extractObject(obj) #Imprime cada vuelo con su información
