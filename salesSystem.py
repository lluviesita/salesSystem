from FlightListAdministration import FlightListAdministration
from FlightAdministration import FlightAdministration
from Statistics import Statistics
from Administrator import Administrator

class Menu:
	def __init__(self):
		self.flightList=FlightListAdministration()#Maipular lista Dic de vuelos -> Fernan
		self.statistic=Statistics()#Actualizar atributos para llevar las ventas ->Fernan
		self.flightAdmin=FlightAdministration(self.flightList)
		self.Admin=Administrator("Lluvia","Manilla",10000.555,"1999/04/24")
		self.principalMenu()

	def principalMenu(self):
		while True:
			print("\n\t\t---- SISTEMA DE VENTAS ----\n")
			print("\t\t1. Administrador")
			print("\t\t2. Cliente")
			print("\t\t3. Salir")
			option = int(input("Opción: "))

			if option == 1:
				self.adminMenu()
			elif option == 2:
				#Agregar codigo para menu cliente -> Fernan
				pass
			elif option == 3:
				break

	def adminMenu(self):
		while True:
			print("\n\t\t---- Administrador ----\n")
			print("\t\t1. Ingresar")
			print("\t\t2. Regresar")
			option = int(input("Opción: "))
			if option == 1:
				if self.validate():
					print("Usuario validado")
					if option == 1:
						self.sytemSalesMenu()
			elif option == 2:
				break

	def sytemSalesMenu(self):
		while True:
			print("\n\t\t---- SISTEMA DE VENTAS ----\n")
			print("\t\t1. Ingresar número máximo de vuelos")
			print("\t\t2. Ingresar vuelos")
			print("\t\t3. Listar vuelos")
			print("\t\t4. Cancelar vuelos")
			print("\t\t5. Actualizar vuelos")
			print("\t\t6. Estadísticas de pago")
			print("\t\t7. Estadísticas de clases")
			print("\t\t8. Información administrador")
			print("\t\t9. Regresar")
			print()
			option = int(input("Opción: ")) 
			if option == 1:
				maxNumberFlights = int(input("Ingresa el número máximo de vuelo: "))
				self.flightAdmin.setMaxNumberOfFlights(maxNumberFlights)
			elif option == 2:
				print("\n\t\t---- Ingresar nuevo vuelo ----\n")
				self.flightAdmin.setFlights()
			elif option == 3:
				self.flightAdmin.printFlights()
			elif option == 4:
				flightNumber = int(input("Ingrese el vuelo que desea cancelar: "))
				self.flightAdmin.deleteFlight(flightNumber)
				print("Vuelo {}".format(flightNumber)+" cancelado")
			elif option == 5:
				print("\n\t\t---- Modificar vuelo ----\n")
				print("\t\t1. Destino")
				print("\t\t2. Hora Salida (HH:ss)")
				print("\t\t3. Hora Llegada (HH:ss)")
				print("\t\t4. Costo de viaje Turista")
				print("\t\t5. Costo de viaje Negocios")
				print("\t\t6. Costo de viaje Primera Clase")
				print("\t\t7. Lugares disponibles clase Turista")
				print("\t\t8. Lugares disponibles clase Negocios")
				print("\t\t9. Lugares disponibles clase Primera Clase")
				print("\t\t10. Fecha de salida (yyyy/mm/dd)")
				print("\t\t11. Regresar")
				fligthData = int(input("Opción: "))
				
				if fligthData != 11:
					flightNumber = int(input("Número de vuelo a modificar: "))
					self.flightAdmin.updateFlight(flightNumber,fligthData)
			elif option == 6:
				self.statisticPayMenu()
			elif option == 7:
				self.statisticClassMenu()
			elif option == 8:
				print("\n\t\t---- Datos del Administrador ----\n")
				print(self.Admin.toString())
			elif option == 9:
				break

	def statisticPayMenu(self):
		while True:
			print("\n\t\t---- Estadísticas de Pago ----\n")
			print("\t\t1. Efectivo total en cajas")
			print("\t\t2. Saldo de pagos por tarjeta")
			print("\t\t3. Saldo total de ventas")
			print("\t\t4. Número de pagos realizados en efectivo")
			print("\t\t5. Número de pagos realizados con tarjeta")
			print("\t\t6. Regresar")
			option = int(input("Opción: "))
			if option == 1:
				print(self.statistic.cashBalance)
			elif option == 2:
				print(self.statistic.creditCardBalance)
			elif option == 3:
				print(self.statistic.totalAmountOfSells)
			elif option == 4:
				print(self.statistic.numberOfCashPayments)
			elif option == 5:
				print(self.statistic.numberOfCreditCardsPayments)
			elif option == 6:
				break

	def statisticClassMenu(self):
		while True:
			print("\n\t\t---- Estadísticas de Clase ----\n")
			print("\t\t1. Boletos vendidos de la Clase Turista")
			print("\t\t2. Boletos vendidos de la Clase Negocios")
			print("\t\t3. Boletos vendidos de Primera clase ")
			print("\t\t4. Clase con mayor número de ventas")
			print("\t\t5. Regresar")
			option = int(input("Opción: "))
			if option == 1:
				print(self.statistic.touristTickets)
			elif option == 2:
				print(self.statistic.businessTickets)
			elif option == 3:
				print(self.statistic.fistsClassTickets)
			elif option == 4:
				print(self.statistic.getBestSellerClass())
			elif option == 5:
				break

	def validate(self):
		#Ingresar codigo de usuario  y contraseña, si es correcto regresar True - Fernan
		return True

Menu1 = Menu()
