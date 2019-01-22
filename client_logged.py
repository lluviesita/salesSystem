# Pantalla de bienvenida luego de haber log in de cliente

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

	elif c_opc == 2:
		
		# Buy some tickets
	
	elif c_opc == 3:
		# Check client's info
	elif c_opc == 4:
		break