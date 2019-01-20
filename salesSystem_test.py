flag = True
while flag:
    print("\n\t\t---- SISTEMA DE VENTAS ----\n")
    print("\t\t1. Administrador")
    print("\t\t2. Cliente")
    print("\t\t3. Salir")

    option = int(input("Option: "))
    if option == 3:
        flag = False
        break
    elif option == 1:
        print("\n\t\t---- Administrador ----\n")
        print("\t\t1. Ingresar")
        print("\t\t2. Regresar")
        option = int(input("Option: "))

    if option == 1:
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
            numMaxFlight = int(input("Ingresa el número máximo de vuelos:"))
        elif option == 2:
            print("\n\t\t---- Ingresar nuevo vuelo----\n")
            destination = str(input("\t\tDestino: "))
            departureHour = str(input("\t\tHora salida: "))
            arrivedHour = str(input("\t\tHora llegada: "))
            touristCost = str(input("\t\tCosto de viaje Turista: "))
            bussinessCost = str(input("\t\tCosto de viaje Negocios: "))
            firstClassCost = str(input("\t\tCosto de viaje Primera Clase: "))
            placesAvailableTourist = str(input("\t\tLugares disponibles calse Turista: "))
            placesAvailableBusiness = str(input("\t\tLugares disponibles calse Negocios: "))
            placesAvailableFisrtClass = str(input("\t\tLugares disponibles calse Primera Clase: "))
            departureDate = str(input("\t\tFecha de salida: "))
            print("\tVuelo registrado satisfactoriamente") 
        elif option == 3:
            print("\n\tVuelo no: 1\n")
            destination = "\t\tDestino: "
            print(destination)
            departureHour = "\t\tHora salida: "
            print(departureHour)
            arrivedHour = "\t\tHora llegada: "
            print(arrivedHour)
            touristCost = "\t\tCosto de viaje Turista: "
            print(touristCost)
            bussinessCost = "\t\tCosto de viaje Negocios: "
            print(bussinessCost)
            firstClassCost = "\t\tCosto de viaje Primera Clase: "
            print(firstClassCost)
            placesAvailableTourist = "\t\tLugares disponibles calse Turista: "
            print(placesAvailableTourist)
            placesAvailableBusiness = "\t\tLugares disponibles calse Negocios: "
            print(placesAvailableTourist)
            placesAvailableFisrtClass = "\t\tLugares disponibles calse Primera Clase: "
            print(placesAvailableFisrtClass)
            departureDate = "\t\tFecha de salida: "
            print(departureDate)
            print()
        elif option == 4:
            numFlight = input("¿Qué vuelo desea cancelar?: ")
            print("El vuelo a cancelar es: ",numFlight)
        elif option == 5:
            print("\n\t\t-----Mofificar vuelo-----\n")
            destination = "\t\tDestino: "
            print(destination)
            departureHour = "\t\tHora salida: "
            print(departureHour)
            arrivedHour = "\t\tHora llegada: "
            print(arrivedHour)
            touristCost = "\t\tCosto de viaje Turista: "
            print(touristCost)
            bussinessCost = "\t\tCosto de viaje Negocios: "
            print(bussinessCost)
            firstClassCost = "\t\tCosto de viaje Primera Clase: "
            print(firstClassCost)
            placesAvailableTourist = "\t\tLugares disponibles calse Turista: "
            print(placesAvailableTourist)
            placesAvailableBusiness = "\t\tLugares disponibles calse Negocios: "
            print(placesAvailableTourist)
            placesAvailableFisrtClass = "\t\tLugares disponibles calse Primera Clase: "
            print(placesAvailableFisrtClass)
            departureDate = "\t\tFecha de salida: "
            print(departureDate)
            numFlight = str(input("Numero de vuelo a modificar: "))
            print("Número de vuelo a modificar: ",numFlight)
            print()
        elif option == 6:
            print("\n\t\t---- Estadísticas de pago ----\n")
            print("\t\t1. Efectivo total en cajas")
            if option == 1:
                print("El efectivo total en cajas es: ")
            print("\t\t2. Saldo de pagos por tarjeta")
            if option == 2:
                print("Estoy en pago tarjeta")
            print("\t\t3. Saldo total de ventas")
            print("\t\t4. Numero de pagos realizados en efectivo")
            print("\t\t5. Numero de pagos realizados en tarjeta")
            print("\t\t6. Regresar")
            option = int(input("Option: ")) 
            print()
        elif option == 7:
            print("\n\t\t---- Estadísticas de Clase ----\n")
            print("\t\t1. Boletos vendidos de la clase Turista")
            print("\t\t2. Boletos vendidos de la clase Negocios")
            print("\t\t3. Boletos vendidos de Primera Clase")
            print("\t\t4. Clase con mayor número de ventas")
            print("\t\t5. Regresar")
            print()
        elif option == 8:
            ID = "1234567"
            name = "Lluvia Alejandra Manilla Hernández"
            sueldo = "10000"
            print("Administrador {0} con identificador {1}, su sueldo asignado es: {2}".format(name,ID,sueldo))
    elif option == 2:
        print("\n\t\t---- Cliente ----\n")
        print("\t\t1. Ingresar")
        print("\t\t2. Registrarse")
        print("\t\t3. Regresar")
        option = int(input("option: "))
