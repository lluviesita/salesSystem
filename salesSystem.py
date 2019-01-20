from FlightListAdministration import FlightListAdministration
from FlightAdministration import FlightAdministration
from Statistics import Statistics

class Menu:
	def __init__(self):
		self.flightList=FlightListAdministration()#Maipular lista Dic de vuelos -> Fernan
		self.statistic=Statistics()#Actualizar atributos para llevar las ventas ->Fernan
		self.flightAdmin=FlightAdministration(self.flightList)
		self.principalMenu()

	def principalMenu(self):
		while True:
			print("\n\t\t---- SISTEMA DE VENTAS ----\n")
			print("\t\t1. Administrador")
			print("\t\t2. Cliente")
			print("\t\t3. Salir")
			option = int(input("Option: "))

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
			option = int(input("Option: "))
			if option == 1:
				if self.validate():
					print("Usuario validado")
					if option == 1:
						self.sytemSalesManu()
			elif option == 2:
				break
	def sytemSalesManu(self):
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
			option = int(input("Option: ")) 
			if option == 1:
				maxNumberFlights = int(input("Ingresa el número máximo de vuelo: "))
				self.flightAdmin.setMaxNumberOfFlights(maxNumberFlights)
			elif option == 2:
				print("\n\t\t---- Ingresar nuevo vuelo----\n")
				self.flightAdmin.setFlights()
			elif option == 3:
				self.flightAdmin.printFlights()
			elif option == 9:
				break

	def validate(self):
		#Ingresar codigo de usuario  y contraseña, si es correcto regresar True - Fernan
		return True

Menu1 = Menu()
