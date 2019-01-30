import getpass
import sys

'''
CLASS_DEFINITION

Contiene las clases y funciones requeridas para el funcionamiento del algoritmo,
se divide en 4 partes:
* Clases de Usuarios; donde se definen las clases para el administrador y el cliente.

* Clases de vuelos; se establece el método para crear el inventario de vuelos y demás
tareas que el administrador puede ejecutar.

* Clases de estadísticas; cubre las clases empleadas para la extracción de las métricas
de compra y dinero referente a los vuelos.

* Funciones; posee las funciones que podrán ejecutar el administrador o el cliente.

El funcionamiento del algoritmo se logra ejecutando el archivo home.py; este script es
importado por dicho fichero.

Desarrollado por:

	Lluvia Manilla
	Fernan Paul Cerón

'''
#========================================================================================
# CLASES DE USUARIOS

class Admin:
	def __init__(self,user,password):
		self.name_lastname = 'Napoleon Quintanilla'
		self.position = 'Administrador Senior'
		self.user = user
		self.password = password
		self.salary = 25000

admin1 = Admin('Admin1','1234')

class Client(Admin):
	def __init__(self,user,password,name,age):
		super().__init__(user,password)
		self.name = name
		self.age = age

#========================================================================================
# CLASE DE VUELOS
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
				print(f'\t{k}: {self.flightdata[k]}\n')  


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
		if key[0:5] == 'Costo' or key[0:4] == 'Cupo':
			obj[element].flightdata[key] = int(input(f'\n\tActualice {key}: '))
		else:
			obj[element].flightdata[key] = input(f'\n\tActualice {key}: ')

	@staticmethod
	def update_buy(obj,item,key,quantity):
		if obj[item].flightdata[key] == 0:
			print('\n\tNo hay asientos disponibles en esta categoría')
		elif quantity > obj[item].flightdata[key]:
			print(f'\nNo hay suficientes cupos, la cantidad máxima son {obj[item].flightdata[key]}')
		else:
			obj[item].flightdata[key] = obj[item].flightdata[key] - quantity

#================================================================================================
# CLASES DE ESTADÍSTICAS

class Metrics:

	tourist = 0
	business = 0
	fst_class = 0


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
			for i in range(len(att_tuples)):
				b = att_tuples[i][1]
				if b >= a:
					a = b
					c = att_tuples[i]
			listsorted.append(c)
			att_tuples.remove(c)
			a = 0
		return listsorted


class Invoicing:

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
			cls.total_incoming = cls.petty_cash + cls.bank_account
		elif p_type == 'Cash':
			cls.nCash_transactions += 1
			cls.petty_cash += amount
			cls.total_incoming = cls.petty_cash + cls.bank_account

#===============================================================================================
#===============================================================================================
#================================== DEFINICIÓN DE FUNCIONES ====================================

def admin_menu(admin):	
	global f_inventory
	while True:
		try:
			print('\n'*2,'--- INTERFAZ DE ADMINISTRADOR ---\n')
			print('\t1. Ingresar vuelos','\n\t2. Mostrar lista de vuelos','\n\t3. Eliminar vuelos',
			'\n\t4. Modificar información de vuelos','\n\t5. Mostrar estadísticas de pago',
			'\n\t6. Estadísticas de pasajes','\n\t7. Información de Administrador','\n\t8. Atrás\n')
			admin_opc = int(input('Digite la opción deseada: '))
		except:
			print('\n*** Ingrese una opción válida.')
			continue

		if admin_opc == 8:
			break

		elif admin_opc == 1: # Registro de nuevos vuelos
			print('\n'*2,'--- Registro de nuevos vuelos ---\n')
			
			while True:
				try:
					n= int(input('\tNúmero de vuelos a registrar: '))
					break
				except:
					print('\n*** INGRESE UNA OPCIÓN VÁLIDA ***')
			f_inventory = Flight.fcreator(n)
			print(f'\nSe han registrado satisfactoriamente {n} nuevos vuelos.')

		elif admin_opc == 2: # Mostrar inventario de vuelos
			while True:
				print('\n'*2,'--- Inventario de vuelos ---\n')
				try:
					Flight.displayInfo(Flight.extractObject(f_inventory),f_inventory)
					back = input('\nPresione enter para volver al menú anterior.')
					break
				except NameError:
					print('\n\t*** Aún no hay vuelos registrados')
					break

		elif admin_opc == 3: # Cancelación de objetos tipo vuelo
			print('\n--- Cancelar vuelos ---\n')
			del_element = int(input('\tDigite el número de vuelo a eliminar, escriba 0 para cancelar la operación: '))
			if del_element == 0:
				continue
			try:
				Flight.del_entry(f_inventory,(del_element-1))
				print(f'\n\tEl vuelo {del_element} ha sido eliminado con exito')
			except NameError:
				print('\n\t*** Aún no hay vuelos registrados')
				continue
			except IndexError:
				print('\n\t** Ingrese un valor dentro del rango, revise nuevamente el inventario de vuelos')
				continue


		elif admin_opc == 4: # Modificacioón de datos de vuelos
			try:
				if len(f_inventory) == 0:
					print('\n*** No hay vuelos en inventario, registre nuevos vuelos ***')
					continue
			except NameError:
				print('\n*** Registre nuevos vuelos ***')
				continue
			print('\n--- Modificación de vuelos ---')
			Flight.list_flightDest(Flight.extractObject(f_inventory),f_inventory)
			while True:
				try:
					upd_element = int(input('\nIngrese el número de vuelo a modificar, 0 para regresar: '))
					break
				except ValueError:
					print('\nEscoja una opción válida')
					continue
			if upd_element == 0:
				continue
			f_item = upd_element -1
			k_list = list(f_inventory[f_item].flightdata.keys())
			print('\nPropiedades de vuelo: \n')
			i = 0	
			for k in k_list: print(f'\t{i+1}. {k}');i += 1
			
			while True:
				try:
					while True:
						numkey = int(input('\n\tEscoga propiedad a modificar, 0 para regresar: '))
						if numkey == 1:
							key = 'Destino'
						elif numkey == 2:
							key = 'Fecha de salida (DD/MM/AAAA)'
						elif numkey == 3:
							key = 'Hora de salida (HH:MM)'
						elif numkey == 4:
							key = 'Hora de llegada (HH:MM)'
						elif numkey == 5:
							key = 'Costo clase turista'
						elif numkey == 6:
							key = 'Cupo clase turista'
						elif numkey == 7:
							key = 'Costo clase negocios'
						elif numkey == 8:
							key = 'Cupo clase negocios'
						elif numkey == 9:
							key = 'Costo primera clase'
						elif numkey == 10:
							key = 'Cupo primera clase'
						elif numkey == 0:
							break
						break	
					if numkey == 0:
						break
					else:
						Flight.update_info(f_inventory,f_item,key)
						print('\n\n*** Se ha actualizado la información con éxito.***')
				except:
					print('\nEscoja una opción válida')
					continue

		elif admin_opc == 5: # Contabilidad de compras realizadas
			while True:
				print('\n--- Contabilidad ---')
				print('\n\t1. Saldo en cuenta bancaria\n\t2. Saldo en caja menor\n\t3. Ingresos totales\n\t4. Compras realizadas\n\t5. Regresar')
				try:
					opc = int(input('\n\tIndique una opción: '))
					if opc == 1:
						print(f'\n\tEl saldo en cuenta bancaria es de $ {Invoicing.bank_account}')
						input('\n\tPresione enter para regresar')
						continue
					elif opc == 2:
						print(f'\n\tEl saldo en caja menor es de $ {Invoicing.petty_cash}')
						input('\n\tPresione enter para regresar')
						continue
					elif opc == 3:
						print(f'\n\tLos ingresos totales son $ {Invoicing.total_incoming}')
						print(f'\t${Invoicing.bank_account} en cuentas y ${Invoicing.petty_cash} en caja menor')
						input('\n\tPresione enter para regresar')
						continue
					elif opc == 4:
						print(f'\nSe han realizado:\n\t{Invoicing.nCard_transactions} pagos con tarjeta\n\t{Invoicing.nCash_transactions} pagos en efectivo')
						input('\n\tPresione enter para regresar')
						continue
					elif opc == 5:
						break
					elif opc > 5:
						print('\n*** Ingrese un número dentro del rango de opciones')
						continue
				except ValueError:
					print('\n\t*** Ingrese una opción válida***')		

		elif admin_opc == 6: # Métricas de pasajes comprados
			while True:
				print('\n--- Métricas de Categorías de vuelos  ---')
				print('\n\t1. Contador de tickets vendidos (Todas las categorías)\n\t2. Categoría más vendida\n\t3. regresar')

				try:
					opc = int(input('\nIndique una opción: '))
					if opc == 1:
						print(f'\n\tSe han comprado:\n\tClase turísta: {Metrics.tourist} tiquetes\n\tClase negocios: {Metrics.business} tiquetes\n\tPrimera clase: {Metrics.fst_class} tiquetes')
						input('\nPresione enter para regresar')
						continue
					elif opc == 2:
						print('\n\tRanking de categorías vendidas:\n')
						rank = Metrics.ticket_ranking()
						for k,v in dict(rank).items(): print(f'\t {k}: {v} Tickets')
						if 	rank[0][1] == 0:
							print('\n\tNo se han vendido vuelos\n')
						else:
							print(f'\n\tLa categoría más vendida es {rank[0][0]}\n')
						input('Presione enter para regresar')
						continue
					elif opc == 3:
						break
					elif opc > 3:
						print('\n*** Ingrese un número dentro del rango de opciones')
						continue
				except ValueError:
					print('\n\t*** Ingrese una opción válida***')

		elif admin_opc == 7:
			print('\n --- Datos de administrador ---\n')
			print(f'\tNombre: {admin1.name_lastname}\n\tCargo: {admin1.position}\n\tUsuario: {admin1.user}\n\tSalario: {admin1.salary} MXN')
			input('\n*** Presione enter para volver al menú de administrador')

		elif admin_opc == 8:
			break

def client_login(): # MENÚ DE INICIO DE SESIÓN COMO CLIENTE
	global client1
	def client_menu():
		while True:
			print(f'\n---- Bienvenido {client1.name} ----\n')
			print('\t1. Ver vuelos disponibles')
			print('\t2. Comprar vuelos')
			print('\t3. Ver mi información')
			print('\t4. Cerrar sesión')

			try:
				c_opc = int(input('Opción: '))
				if not 0<= c_opc <= 4:
					print('\n**Número fuera del rango válido, seleccione nuevamente.')
					input('\nPresione enter para continuar')
					continue
			except ValueError:
				print('\n**Opción inválida. Ingrese un número del menú, no letras.')
				input('\nPresione enter para continuar.')
				continue
			if c_opc == 1:	# Check available flights
				while True:
					print('\n'*2,'--- Inventario de vuelos ---\n')
					try:
						Flight.displayInfo(Flight.extractObject(f_inventory),f_inventory)
						back = input('\nPresione enter para volver al menú anterior.')
						break
					except NameError:
						print('\n\t*** Aún no hay vuelos registrados',sys.exc_info(),'\n')
						print()
						break
			elif c_opc == 2: # PROCESO DE COMPRA DE VUELOS
				print('--- Compra de tiquetes ---')

				while True: # Selección de categoría de viaje
					try:
						item = int(input('\n\tIngrese el número de vuelo a comprar, para cancelar digite 0: '))
						if item == 0:
							break
						elif (item-1) > (len(f_inventory)-1):
							print('\n**El Vuelo expecificado está fuera del rango')	
							continue
						print('\n\tIndique el tipo de pasaje:\n\t1. Clase Turista\n\t2. Clase Negocios\n\t3. Primera Clase')
						while True:
							sit_type = int(input('\nIngrese su opción: '))
							if sit_type == 1:
								sit_key = 'Cupo clase turista'
								cost_key = 'Costo clase turista'
								break
							elif sit_type == 2:
								sit_key = 'Cupo clase negocios'
								cost_key = 'Costo clase negocios'
								break
							elif sit_type == 3:
								sit_key = 'Cupo primera clase'
								cost_key = 'Costo primera clase'
								break
							else:
								print('\n\t** Ingrese una opción válida')
								continue
					except ValueError:
						print('\n\t*** Escriba solo números')
						continue

					try:
						quantity = int(input('Ingrese el número de pasajeros: '))
						if f_inventory[item-1].flightdata[sit_key] < quantity:
							print('\nLa cantidad de compra supera el cupo disponible en esta\ncategoría de pasaje.')
							continue
						else:
							total_cost = f_inventory[item-1].flightdata[cost_key]*quantity
							print('\n\t-- Forma de pago --\n\t\t1. Pago en efectivo\n\t\t2. Transacción bancaria')
							while True:	
								try:	
									pay_opt=int(input('Opción: '))
									break
								except ValueError:
									print('\n\t** Ingrese una opción válida')
									continue
									
							if pay_opt == 1:
								p_type = 'Cash'
								print('\nSu vuelo será reservado, para culminar el proceso de compra\nrealice el pago en nuestras oficinas.')
								print(f'\nSu compra tiene un costo total de ${total_cost},\nproporcione sus datos en ventanilla para concluir la compra')
								Flight.update_buy(f_inventory,item-1,sit_key,quantity)
								Invoicing.capture_invoice(p_type,total_cost)
								Metrics.count_tickets(sit_type,quantity)
								break

							elif pay_opt == 2:
								p_type = 'Card'
								print('\n\t-- Ingrese sus datos de cuenta --')
								while True:
									try:
										client_account = int(input('\n\tNúmero de cuenta: '))
										client_pin = int(getpass.getpass('\n\tDigite su pin: '))
										client_pin2 = int(getpass.getpass('\n\tConfirme su pin: '))
									except ValueError:
										print('\n\tSolo se admiten valores numéricos, ingrese sus datos de cuenta nuevamente.')
										continue
									if client_pin == client_pin2:
										print('####### Validando datos de cuenta #######')
										break
									else:
										print('\n\tLas claves no coinciden, por favor ingrese su información nuevamente.')
										continue	
								print(f'\n\tEl saldo a debitar de la cuenta {client_account} es de ${total_cost}.')
								try:	
									conf = int(input('\n\t1. Confirmar compra\t2. Cancelar compra: '))
								except ValueError:
									print('\n\t*** Opción inválida, por su seguridad ha sido cancelada su compra. ***')
									break
								if conf == 1:
									Flight.update_buy(f_inventory,item-1,sit_key,quantity)
									Invoicing.capture_invoice(p_type,total_cost)
									Metrics.count_tickets(sit_type,quantity)
									print('\n\tLa transacción ha sido realizada con éxito\n\t**Gracias por su compra**')
									input('\nPresione enter para retroceder.')
									break
							else:
								print('** Opción inválida')
								continue			
					except ValueError:
						print('\n\t*** Escriba solo números')			
					except NameError:
						print('\nNo hay vuelos en inventario')
						break


				
# -----------------------------------------------------------------------------------------------------------------------------
			elif c_opc == 3:
				try:
					print('\n--- Datos de Cuenta de Cliente ---')
					print(f'\n\tNombre de cliente {client1.name}\n\tEdad: {client1.age}\n\tUsuario: {client1.user}')
					input('\nPresione enter para continuar.')
				except NameError:
					print('\n\t*** No hay usuarios registrados ***')

			elif c_opc == 4:
				break
	# ============= Log in Screen ================
	while True:
		print("\n---- Cliente ----\n")
		print('Seleccione una opción:\n')
		print('\t1. Ingresar')
		print('\t2. Registrarse como nuevo usuario')
		print('\t3. Atrás')

		try:
			opc = int(input('Opción: '))
			if not 0<= opc <= 3:
				print('Número fuera del rango válido, seleccione nuevamente.')
				continue
		except ValueError:
			print('\nOpción inválida')
			print('Ingrese un número del menú, no letras')
			continue
	
		if opc	== 3: # Sale del menú cliente
			print('\nDe vuelta al menú principal')
			break
	
		elif opc == 1: # Inicio de sesión de Cliente
			print('\nIngrese sus datos de cuenta\n')
			while True:
				username = input("\tUsuario: ")
				password = getpass.getpass("\tContraseña: ")
				try:
					if username == client1.user and password == client1.password:
						print('\n- Ha iniciado sesión como:', client1.user,'-\n')
						login = 1
						break
					else:
						login = 0
						print('\n*** El usuario o la contraseña son incorrectos, por favor ingrese los datos nuevamente.')
						input('\nPresione enter para salir')
						break
				except NameError:
					print('\n\t** No hay clientes registrados **')
					input('\n\tPresione enter para volver al menú anterior.')
					login = 0
					break
			if login == 1:
				client_menu() # AQUÍ EMPIEZA EL MENÚ DE CLIENTE
			else:
				continue

		elif opc == 2: # Creación de nuevo cliente
			print("\nIngrese sus datos de usuario:\n")
			client_name = input("Escriba su nombre completo: ")
			client_user = input("Ingrese su nombre de usuario: ")
			client_age = input("Ingrese su edad: ")

			while True:
				client_passw = getpass.getpass('Ingrese su contraseña: ')
				client_passw2 = getpass.getpass('Confirme su contraseña: ')
				if client_passw == client_passw2:
					print('\n--- Usuario registrado con éxito ---\n')
					client1 = Client(client_user,client_passw,client_name,client_age)
					print('Nombre de cliente:',client1.name)
					print('Edad del cliente:',client1.age)
					print('Usuario:',client1.user)
					input('\nPresione enter para realizar inicio de sesión')
					break
				else:
					print("\n**No hay coincidencia, escriba su contraseña nuevamente**\n")
					continue