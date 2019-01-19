import getpass

class Admin:
	def __init__(self,username,password):
		self.username = username
		self.password = password

user_data = "Admin1"
pass_data = '1234'

class Client(Admin):
		def __init__(self,name,lastname,age):
			self.name = name
			self.lastname = lastname
			self.age = age

while True:
	print("\n---- Reservas de vuelos en línea ----\n")
	print('Seleccione una opción:\n')
	print('\t1. Administrador')
	print('\t2. Cliente')
	print('\t3. Salir')	
	try:
		opc = int(input('Opción: '))
		if not 0<= opc <= 3:
			print('Número fuera del rango válido, seleccione nuevamente.')
			continue
	except ValueError:
		print('\nOpción inválida')
		print('Ingrese un número del menú, no letras')
		continue
	if opc	== 3:
		print('Hasta luego')
		break
	elif opc == 1:
		print('Continúa como administrador')
		while True:
			username = input("Ingrese el nombre de usuario: ")
			password = getpass.getpass("Contraseña: ")
			admin1 = Admin(username,password)
			if username == user_data and password == pass_data:
				logged = 1
				print('Ha iniciado sesión como:', admin1.username)
				break
			else:
				print('El usuario o la contraseña son incorrectos, por favor ingrese los datos nuevamente.')
				continue		
	elif opc == 2:
		print('Continúa como cliente')
		break





