class Statistics:
	def __init__(self):
		self.cashBalance = 0.0
		self.creditCardBalance = 0.0
		self.totalAmountOfSells = 0.0
		self.numberOfCashPayments = 0
		self.numberOfCreditCardsPayments = 0
		self.touristTickets = 0
		self.businessTickets = 0
		self.fistsClassTickets = 0

	def getBestSellerClass(self):
		message="not exist a best Seller"
		if (self.touristTickets > self.businessTickets) and (self.touristTickets > self.fistsClassTickets):
			message="Tourist Tickets are the best Seller"
		if (self.businessTickets > self.touristTickets) and (self.businessTickets > self.fistsClassTickets):
			message="Business Tickets are the best Seller"
		if (self.fistsClassTickets > self.touristTickets) and (self.fistsClassTickets > self.businessTickets):
			message="Fists Class Tickets are the best Seller"
		return message
