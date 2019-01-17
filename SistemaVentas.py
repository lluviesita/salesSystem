flag = True
while flag:
    print("     ---- SISTEMA DE VENTAS ----")
    print("           1. Administrador")
    print("           2. Cliente")
    print("           3. Salir")

    option = int(input("option: "))
    if option == 3:
        flag = False
        break
    if option == 1:
        print("         ---- Administrador ----")
        print("                1. Ingresar")
        print("                2. Regresar")
        option = int(input("option: "))
    if option == 1:
            print("     ---- SISTEMA DE VENTAS ----")
            print()
            print("     1. Ingresar número máximo de vuelos")
            print("     2. Ingresar vuelos")
            print("     3. Listar vuelos")
            print("     4. Cancelar vuelos")
            print("     5. Actualizar vuelos")
            print("     6. Estadísticas de pago")
            print("     7. Estadísticas de clases")
            print("     8. Información administrador")
            print("     9. Regresar")
            print()
            option = int(input("option: "))
    if option == 2:
        print("         ---- Cliente ----")
        print("         1. Ingresar")
        print("         2. Registrarse")
        print("         3. Regresar")
        option = int(input("option: "))
