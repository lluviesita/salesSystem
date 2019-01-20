
class Administrator:
      def __init__(self,FirtName,lastName,salary,birthDate):
            self.FirstName = FirtName
            self.lastName = lastName
            self.salary = salary
            self.birthDate = birthDate
            print("El nombre del Administrador es: "+self.FirstName+lastName+" , su salario es: "+str(self.salary)+" años. Su fecha de nacimiento es: "+birthDate+".")

FirtName = "Lluvia"
lastName = "Manilla"
salary = 10000.00
birthDate = "1997/04/24"

Admin1 = Administrator(FirtName,lastName,salary,birthDate)

Admin1
