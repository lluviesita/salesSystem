class Flight:
      def __init__(self,hasPassengers,destination,departureTime,arrivingTime,touristCost,businessCost,firstClassCost,touristAvailableSeats,businessAvailableSeats,firstClassAvailableSeats,departureDate):
            self.hasPassengers = hasPassengers
            self.destination = destination
            self.departureTime = departureTime
            self.arrivingTime = arrivingTime
            self.touristCost = touristCost
            self.businessCost = businessCost
            self.firstClassCost = firstClassCost
            self.touristAvailableSeats = touristAvailableSeats
            self.businessAvailableSeats = businessAvailableSeats
            self.firstClassAvailableSeats = firstClassAvailableSeats
            self.departureDate = departureDate

      def toString(self):
            return ("\t\tDestino: "+self.destination
            	+"\n\t\tHora de salida: "+self.departureTime
            	+"\n\t\tHora de llegada: "+self.arrivingTime
            	+"\n\t\tCosto de viaje Turista: "+str(self.touristCost)
            	+"\n\t\tCosto de viaje Negocios: "+str(self.businessCost)
            	+"\n\t\tCosto de viaje Primera Clase: "+str(self.firstClassCost)
            	+"\n\t\tLugares disponibles calse Turista: "+str(self.touristAvailableSeats)
            	+"\n\t\tLugares disponibles calse Negocios: "+str(self.businessAvailableSeats)
            	+"\n\t\tLugares disponibles calse Primera Clase: "+str(self.firstClassAvailableSeats)
            	+"\n\t\tFecha de salida: "+self.departureDate)
