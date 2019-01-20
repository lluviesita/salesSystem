from Flight import Flight

class FlightAdministration:

	def __init__(self,flightListAdministration):
		self.flightListAdministration = flightListAdministration

	def setMaxNumberOfFlights(self, MaxNumberOfFlights):
		self.MaxNumberOfFlights=MaxNumberOfFlights+1
		print("Se asignaron "+str(MaxNumberOfFlights)+" vuelos.")

	def setFlights(self):
		for x in range(1,self.MaxNumberOfFlights):
			print("Vuelo no.: ",x)
			hasPassengers = False
			destination = input("\t\tDestino: ")
			departureTime = input("\t\tHora Salida (HH:ss): ")
			arrivingTime = input("\t\tHora Llegada: (HH:ss)")
			touristCost = float(input("\t\tCosto de viaje Turista: $ "))
			businessCost = float(input("\t\tCosto de viaje Negocios: $"))
			firstClassCost = float(input("\t\tCosto de viaje Primera Clase: "))
			touristAvailableSeats = int(input("\t\tLugares disponibles calse Turista: "))
			businessAvailableSeats = int(input("\t\tLugares disponibles calse Negocios: "))
			firstClassAvailableSeats = int(input("\t\tLugares disponibles clase Primera Clase: "))
			departureDate = input("\t\tFecha de salida (yyyy/mm/dd): ")
			flight = Flight(hasPassengers,destination,departureTime,arrivingTime,
				touristCost,businessCost,firstClassCost,touristAvailableSeats, 
				businessAvailableSeats,firstClassAvailableSeats,departureDate)
			self.flightListAdministration.addFlight(x,flight)

	def printFlights(self):
		flightsDict=self.flightListAdministration.getFlights()
		for x in flightsDict:
			print("\n\tVuelo no.: "+str(x)+"\n")
			print(flightsDict[x].toString())

	def deleteFlight(self, flightNumber):
		self.flightListAdministration.deleteFlight(flightNumber)

	def updateFlight(self, flightNumber, flightAttrNumber):
		print("\n\tModificar Vuelo no.: "+str(flightNumber)+"\n")
		fligthData=self.flightListAdministration.getFlight(flightNumber)
		if flightNumber == 1:
			print("\t\tDestino: "+fligthData.destination)
			fligthData.destination=input("\t\tNuevo destino: ")
		elif flightNumber == 2:
			print("\t\tHora de salida: "+fligthData.departureTime)
			fligthData.departureTime=input("\t\tNueva Hora Salida: ")
		elif flightNumber == 3:
			print("\t\tHora Llegada: "+fligthData.arrivingTime)
			fligthData.arrivingTime=input("\t\tNueva Hora Llegada: ")
		elif flightNumber == 4:
			print("\t\tCosto de viaje Turista: "+fligthData.touristCost)
			fligthData.touristCost=input("\t\tCosto de viaje Turista: ")
		elif flightNumber == 5:
			print("\t\tCosto de viaje Negocios: "+fligthData.businessCost)
			fligthData.businessCost=input("\t\tCosto de viaje Negocios: ")
		elif flightNumber == 6:
			print("\t\tCosto de viaje Primera Clase: "+fligthData.firstClassCost)
			fligthData.firstClassCost=input("\t\tCosto de viaje Primera Clase: ")
		elif flightNumber == 7:
			print("\t\tLugares disponibles clase Turista: "+fligthData.touristAvailableSeats)
			fligthData.touristAvailableSeats=input("\t\tLugares disponibles calse Turista: ")
		elif flightNumber == 8:
			print("\t\tLugares disponibles clase Negocios: "+fligthData.businessAvailableSeats)
			fligthData.businessAvailableSeats=input("\t\tLugares disponibles calse Negocios: ")
		elif flightNumber == 9:
			print("\t\tLugares disponibles clase Primera Clase: "+fligthData.firstClassAvailableSeats)
			fligthData.firstClassAvailableSeats=input("\t\tLugares disponibles calse Primera Clase: ")
		elif flightNumber == 10:
			print("\t\tFecha de salida: "+fligthData.departureDate)
			fligthData.departureDate=input("\t\tFecha de salida: ")

		#Etc. under construction
		#

		self.flightListAdministration.updateFlight(flightNumber, fligthData)
		
