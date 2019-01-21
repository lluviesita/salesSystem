import getpass

class Admin:
	def __init__(self,user,password):
		self.user = user
		self.password = password

class Client(Admin):
	def __init__(self,user,password,name,age):
		super().__init__(user,password)
		self.name = name
		self.age = age

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

# AQUÍ EMPIEZA EL MENÚ DE COMPRA DE VUELOS

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
				client1 = Client(client_user,client_passw,client_name,client_age)
				break
			else:
				print("\n**No hay coincidencia, escriba su contraseña nuevamente**\n")
				continue
		print(client1.user)
		print(client1.password)
		print(client1.name)
		print(client1.age)