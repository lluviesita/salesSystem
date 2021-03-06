import getpass
from class_definition import *

'''
HOME 

Este algoritmo es el iniciador de la plataforma de ventas. En esta pantalla se presentan
las opciones de ingreso como Administrador o Cliente, el flujo del programa dependerá de las
opciones escogidas por el usuario.

LÍMITES: 

* El programa solo posee un administrador.
* Únicamente se puede registrar un cliente, en caso de registrar uno nuevo,
 se reescribe la instancia
* Los vuelos mantienen almacenados durante la ejecución del programa, no son escritos.
* No se importa ninguna información, los vuelos deben ser registrados en cada ejecución.

Desarrollado por:

	Lluvia Mancilla
	Fernan Paul Cerón
'''
while True:
	print("\n---- Reservas de vuelos en línea ----\n")
	print('Seleccione una opción de usuario:\n')
	print('\t1. Administrador')
	print('\t2. Cliente')
	print('\t3. Salir')	
	try:
		opc = int(input('Opción: '))
		if not 1<= opc <= 3:
			print('Número fuera del rango válido, seleccione nuevamente.')
			continue
	except ValueError:
		print('\nOpción inválida')
		print('Ingrese un número del menú, no letras')
		continue
	if opc	== 3:
		print('\nHasta luego')
		break
	elif opc == 1:
		while True:
			print('\n--- Inicio de sesión como Administrador ---\n')
			print('\t1. Ingresar datos de usuario\n\t2. Regresar')

			try:
				adm_opc = int(input('\nDigite la opción deseada: '))
				if not 1<= adm_opc <= 2:
					print('Número fuera del rango válido, seleccione nuevamente.')
					continue

			except ValueError:
				print('\nOpción inválida')
				print('Ingrese un número del menú, no letras')
				continue
			
			if adm_opc == 1:
				while True:
					print('\n--- Ingrese sus datos de cuenta ---\n')
					username = input("\tIngrese el nombre de usuario: ")
					password = getpass.getpass("\tContraseña: ")		
					if username == admin1.user and password == admin1.password:
						logged = 1
						print('\n*** Ha iniciado sesión como:', admin1.user,'***\n')
						
						admin_menu(admin1) #AQUÍ SE LLAMA AL MENÚ DE ADMINISTRADOR

						break
					else:
						print('El usuario o la contraseña son incorrectos, por favor ingrese los datos nuevamente.')
						continue
			else:
				break
	elif opc == 2:
		print('Continúa como cliente') # AQUÍ SE LLAMA AL MENÚ DE CLIENTE
		client_login()




