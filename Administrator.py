
class Administrator:
	def __init__(self,FirstName,lastName,salary,birthDate):
		self.FirstName = FirstName
		self.lastName = lastName
		self.salary = salary
		self.birthDate = birthDate

	def toString(self):
		return ("\t\tNombre: "+self.FirstName
			+"\n"+"\t\tApellido: "+self.lastName
			+"\n"+"\t\tSalario: "+str(round(self.salary,2))
			+"\n"+"\t\tFecha de nacimiento: "+self.birthDate)


