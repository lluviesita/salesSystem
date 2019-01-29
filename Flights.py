'''
Definición de clase Flight, esta clase se encarga de capturar la información de los vuelos, ingresados
por el administrador. Además, tambien proporcionará métodos para modificar la información.
'''

class Flight:
	def __init__(self,flightdata):
		self.flightdata = flightdata
			
	@classmethod
	def fcreator(cls,x,flightRecord =[]):
		for j in range(x):
			data_descriptor = ['Destino','Fecha de salida (DD/MM/AAAA)','Hora de salida (HH:MM)','Hora de llegada (HH:MM)','Costo clase turista','Cupo clase turista','Costo clase negocios','Cupo clase negocios','Costo primera clase','Cupo primera clase']
			data_filler = []
			print(f'\nIngrese datos de vuelo {j+1}:\n')

			for i in data_descriptor:
				if 4 <= data_descriptor.index(i) <= 9:
					while True:
						try:
							info = int(input(f"Ingrese {i}: "))
							data_filler.append(info)
							break
						except ValueError:
							print('\n\t** Ingrese un valor numérico')
							continue
				else:
					info = input(f"Ingrese {i}: ")
					data_filler.append(info)
			flight_dict = dict(zip(data_descriptor,data_filler))
			fdata = Flight(flight_dict)
			flightRecord.append(fdata)
		return flightRecord

	@staticmethod
	def extractObject(element):
	# Generador; extrae cada elemento de la lista de vuelos como objeto generador
		for i in range(len(element)):
			yield element[i]

	def displayInfo(self,element):
	# Extrae cada característica del objeto vuelo y lo imprime en pantalla
		i = 0
		for self in Flight.extractObject(element):
			print(f'\nVuelo {i+1}:')
			i += 1
			for k,v in self.flightdata.items():
				print('\t'+k +': ',self.flightdata[k]+'\n')  


	def list_flightDest(self,element):
	# Lista el destino y fecha de partida de cada vuelo. Para orientar al momento de 
	# editar las instancias.
		i = 0
		for self in Flight.extractObject(element):
			print(f'\nVuelo {i+1}:')
			print('Destino: ',self.flightdata.get('Destino'))
			print('Fecha de salida: ',self.flightdata.get('Fecha de salida (DD/MM/AAAA)'))
			print('Hora de salida: ',self.flightdata.get('Hora de salida (HH:MM)'))
			i += 1
				
	@staticmethod
	def del_entry(obj,item):
		del obj[item]

	@staticmethod
	def update_info(obj,element,key):
		obj[element].flightdata[key] = input(f'\n\tActualice {key}: ')

	@staticmethod
	def update_buy(obj,item,key,quantity):
		if obj[item].flightdata[key] == 0:
			print('\n\tNo hay asientos disponibles en esta categoría')
		else:
			obj[item].flightdata[key] = obj[item].flightdata[key] - quantity



class metrics:

	tourist = 0
	business = 0
	fst_class = 0
	# Formular una forma de obtener el key con el valor más alto

	@classmethod
	def count_tickets(cls,f_type,quantity):
		if f_type == 1:
			cls.tourist  += quantity
		elif f_type == 2:
			cls.business += quantity
		elif f_type == 3:
			cls.fst_class += quantity

	@classmethod
	def ticket_ranking(cls):
		att_tuples = [('Categoría Turista',cls.tourist),('Categoría Negocios',cls.business),('Primera clase',cls.fst_class)]
		a = 0
		c = None
		listsorted = []
		while True:
			i = len(att_tuples)
			if i == 0:
				break
			for i in range(len(att_tuples)): # 0 1 2 3 4 5 6
				b = att_tuples[i][1]
				if b >= a:
					a = b
					c = att_tuples[i]
			listsorted.append(c)
			att_tuples.remove(c)
			a = 0
		return listsorted


class invoicing:

	nCash_transactions = 0
	nCard_transactions = 0

	bank_account = 0
	petty_cash = 0
	total_incoming = bank_account + petty_cash

	@classmethod
	def capture_invoice(cls,p_type,amount): #este se invoca en el módulo de compra de clientes
		if p_type == 'Card':
			cls.nCard_transactions += 1
			cls.bank_account += amount
		elif p_type == 'Cash':
			cls.nCash_transactions += 1
			cls.petty_cash += amount