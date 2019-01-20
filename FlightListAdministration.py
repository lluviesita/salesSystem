class FlightListAdministration:
	
	def __init__(self):
		self.fligths = {}

	def addFlight(self, flightNumber, fligthData):
		self.fligths[flightNumber] = fligthData

	def deleteFlight(self, flightNumber):
		self.fligths.pop(flightNumber)

	def updateFlight(self,  flightNumber, fligthData):
		self.fligths.update({flightNumber: fligthData})

	def getFlight(self, flightNumber):
		return self.fligths.get(flightNumber)

	def getFlights(self):
		return self.fligths