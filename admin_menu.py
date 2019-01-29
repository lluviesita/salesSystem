'''
Menú de opciones para usuario tipo Administrador, posterior al inicio de sesión.
'''
import Flights as flt
import users_classes as usr

admin1 = usr.Admin()
def admin_menu():	
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


			f_inventory = flt.Flight.fcreator(n)
			print(f'\nSe han registrado satisfactoriamente {n} nuevos vuelos.')

		elif admin_opc == 2: # Mostrar inventario de vuelos
			while True:
				print('\n'*2,'--- Inventario de vuelos ---\n')
				try:
					flt.Flight.displayInfo(flt.Flight.extractObject(f_inventory),f_inventory)
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
				flt.Flight.del_entry(f_inventory,(del_element-1))
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
			print('--- Ingrese el velo a modificar ---')
			flt.Flight.list_flightDest(flt.Flight.extractObject(f_inventory),f_inventory)
			upd_element = int(input('\nIngrese el número de vuelo a modificar: '))
			f_item = upd_element -1
			k_list = list(f_inventory[f_item].flightdata.keys())
			print('\nPropiedades de vuelo: ')
			i = 0	
			for k in k_list: print(f'{i+1}. {k}');i += 1
			
			while True:
				try:
					numkey = int(input('\tEscoga propiedad a modificar: '))
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
					break
				except:
					print('Escoja una opción válida')
					continue

			flt.Flight.update_info(f_inventory,f_item,key)
			print('Se ha actualizado la información con éxito.')

		elif admin_opc == 5: # Contabilidad de compras realizadas
			while True:
				print('\n--- Contabilidad ---')
				print('\n\t1. Saldo en cuenta bancaria\n\t2. Saldo en caja menor\n\t3. Ingresos totales\n\t4. Compras realizadas\n\t5. Regresar')
				try:
					opc = int(input('\n\tIndique una opción: '))
					if opc == 1:
						print(f'\n\tEl saldo en cuenta bancaria es de $ {flt.invoicing.bank_account}')
						input('\n\tPresione enter para regresar')
						continue
					elif opc == 2:
						print(f'\n\tEl saldo en caja menor es de $ {flt.invoicing.petty_cash}')
						input('\n\tPresione enter para regresar')
						continue
					elif opc == 3:
						print(f'\n\tLos ingresos totales son $ {flt.invoicing.total_incoming}')
						print(f'\t${flt.invoicing.bank_account} en cuentas y ${flt.invoicing.petty_cash} en caja menor')
						input('\n\tPresione enter para regresar')
						continue
					elif opc == 4:
						print(f'\nSe han realizado:\n\t{flt.invoicing.nCard_transactions} pagos con tarjeta\n\t{flt.invoicing.nCash_transactions} pagos en efectivo')
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
				print('\n\t1. Contador de tickets vendidos (Todas las categorías)\n\t2. Categoría más comprada\n\t3. regresar')

				try:
					opc = int(input('\nIndique una opción: '))
					if opc == 1:
						print(f'\n\tSe han comprado:\n\tClase turísta: {flt.metrics.tourist} tiquetes\n\tClase negocios: {flt.metrics.business} tiquetes\n\tPrimera clase: {flt.metrics.fst_class} tiquetes')
						input('Presione enter para regresar')
						continue
					elif opc == 2:
						print('\n\tRanking de categorías vendidas:\n')
						rank = flt.metrics.ticket_ranking()
						for k,v in dict(rank).items(): print(f'\t {k}: {v} Tickets')
						if 	rank[0][1] == 0:
							print('\n\tNo se han vendido vuelos')
						else:
							print(f'\n\tLa categría más vendida es {rank[0][0]}\n')
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