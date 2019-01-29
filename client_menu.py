import getpass
import Flights as flt
import users_classes as usr

class Admin:
	def __init__(self):
		self.name_lastname = 'Napoleon Quintanilla'
		self.position = 'Administrador Senior'
		self.user = 'Admin1'
		self.password = '1234'
		self.salary = 25000
		
class Client(Admin):
	def __init__(self,user,password,name,age):
		super().__init__(user,password)
		self.name = name
		self.age = age
		
	# @staticmethod
	# def buy_tickets(flight):
	# 	while True :
	# 		print('\n--- Menú de compra ---\n')
	# 		flight_tobuy = input("\tIngrese el destino a comprar: ")
	# 		flight_to_display = flight.FlightListAdministration.getFlight(flight_tobuy)
	# 		print('\nEscoja la categoría: ')
	# 		print("\n\t1. Clase turista: $",flight_to_display.touristCost)
	# 		print("\t2. Clase negocios: $",flight_to_display.businessCost)
	# 		print("\t3. Primera clase: $",flight_to_display.firstClassCost)
	# 		print("\t4. Regresar")
	# 		flight_class = int(input("Indique el tipo de pasaje a comprar: "))
	# 		if flight_class == 4:
	# 			break
	# 		else:
	# 			n_tickets = int(input('Ingrese la cantidad de pasajes a comprar: '))
	# 			if flight_class == 1:
	# 				print(f'\nCosto de compra: ${flight_to_display.touristCost*n_tickets}')
	# 			elif flight_class == 2:
	# 				print(f'\nCosto de compra: ${flight_to_display.businessCost*n_tickets}')
	# 			elif flight_class == 3:
	# 				print(f'\nCosto de compra: ${flight_to_display.firstClassCost*n_tickets}')
				

	# 				print("Seleccione el método de pago: \n\t1. Tarjeta de crédito\n\t2. Efectivo")
	# 				m_payment = int(input("Método de pago: "))
	# 				if m_payment == 1:
	# 					while True:
	# 						print("-- Ingrese los datos de su cuenta bancaria --")
	# 						client_card_num = input("Digite el numero de su tarjeta: ")
	# 						card_cvv = getpass.getpass('Digite el código cvv de su tarjeta: ')
	# 						while True:
	# 							card_pin = getpass.getpass('Ingrese su clave: ')
	# 							card_pin2 = getpass.getpass('Confirme su clave: ')
	# 							if card_pin == card_pin2:
	# 								if flight_class == 1:
	# 									statistics.touristTickets += 1

	# 								print('** Operación realizada con éxito **')

def client_menu(): # MENÚ DE INICIO DE SESIÓN COMO CLIENTE
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

	# Sale del menú cliente
		if opc	== 3:
			print('\nDe vuelta al menú principal')
			break

	# Inicio de sesión de Cliente
		elif opc == 1:
			print('\nIngrese sus datos de cuenta\n')
			while True:
				username = input("Nombre de usuario: ")
				password = getpass.getpass("Contraseña: ")
				try:
					if username == client1.user and password == client1.password:
						logged = 1
						print('Ha iniciado sesión como:', client1.user)

# AQUÍ EMPIEZA EL MENÚ DE CLIENTE
					while True:
						print(f'---- Bienvenido {client1.name} ----\n')
						print('\t1. Ver vuelos disponibles')
						print('\t2. Comprar vuelos')
						print('\t3. Ver mi información')
						print('\t4. Atrás')

						try:
							c_opc = int(input('Opción: '))
							if not 0<= c_opc <= 4:
								print('Número fuera del rango válido, seleccione nuevamente.')
								continue
						except ValueError:
							print('\nOpción inválida')
							print('Ingrese un número del menú, no letras')
							continue
						if c_opc == 1:
						# Check available flights
							while True:
								print('\n'*2,'--- Inventario de vuelos ---\n')
								try:
									flt.Flight.displayInfo(flt.Flight.extractObject(f_inventory),f_inventory)
									back = input('\nPresione enter para volver al menú anterior.')
									break
								except NameError:
									print('\n\t*** Aún no hay vuelos registrados')
									break
						elif c_opc == 2:
							print('--- Compra de tiquetes ---')
							item = int(input('\n\tIngrese el número de vuelo a comprar: '))
							while True:
								print('\n\tIndique el tipo de pasaje:\n\t1. Clase Turista\n\t2. Clase Negocios\n\t3. Primera Clase')
								sit_type = int(input('Ingrese su opción: '))
								if sit_type == 1:
									sit_key = 'Cupo clase turista'
									break
								elif sit_type == 2:
									sit_key = 'Cupo clase negocios'
									break
								elif sit_type == 3:
									sit_key = 'Cupo primera clase'
									break
								else:
									print('\n\t** Ingrese una opción válida')
									continue
								# Pedir la cantidad de tiquetes.
							flt.Flight.update_buy(f_inventory,item,sit_key,)
							(obj,item,key,quantity)
						# Buy some tickets
						
						elif c_opc == 3:
							# Check client's info
							usr.
						elif c_opc == 4:
							break

					break # Este es removible
				else:
					print('\nEl usuario o la contraseña son incorrectos, por favor ingrese los datos nuevamente.\n')
					continue
			except NameError:
				print('\nNo existe el usuario aún, regístrese.')
				break

# Creación de nuevo cliente	
	elif opc == 2:
		print("\nIngrese sus datos de usuario:\n")
		client_name = input("Escriba su nombre completo: ")
		client_user = input("Ingrese su nombre de usuario: ")
		client_age = input("Ingrese su edad: ")

		while True:
			client_passw = getpass.getpass('Ingrese su contraseña: ')
			client_passw2 = getpass.getpass('Confirme su contraseña: ')
			if client_passw == client_passw2:
				print('\nUsuario registrado con éxito\n')
				client1 = usr.Client(client_user,client_passw,client_name,client_age)
				break
			else:
				print("\n**No hay coincidencia, escriba su contraseña nuevamente**\n")
				continue
		print(client1.user)
		print(client1.password)
		print(client1.name)
		print(client1.age)