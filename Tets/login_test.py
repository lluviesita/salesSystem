from getpass import getpass

class Administrator:
    def __init__(self,user,password):
    		self.user = user
    		self.password = password

    def login(user,password):
        if user:
            if password:
                return 1
            else:
                print("\n\tCONTRASEÑA INCORRECTA\n")
        else:
            return 2

    user = input("Administrador: ")
    password = getpass("Contraseña: ")

    if login(user,password)==1:
        print('Bienvenido!!!')
    else:
        print('Contrasenia o usurio incorrecto :P')
