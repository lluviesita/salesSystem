class Admin:
	def __init__(self):
		self.name_lastname = 'Napoleon Quintanilla'
		self.position = 'Administrador Senior'
		self.user = 'Admin1'
		self.password = '1234'
		self.salary = 25000
		
class Client(Admin):
	def __init__(self,user,password,name,age):
		super().__init__(user,password)
		self.name = name
		self.age = age