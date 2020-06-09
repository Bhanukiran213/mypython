class PassengerDetails():
	def __init__ (self, name, source, destination, mobileNumber):
		self.name = name
		self.source = source
		self.destination = destination
		self.mobileNumber = mobileNumber
	def get_passengerDetails(self):
		print("passenger name:",self.name)
		print("passenger source:",self.source)
		print("passenger destination:",self.destination)
		print("passenger mobileNumber:",self.mobileNumber)
passengerdetails = PassengerDetails("Bhanukiran", "Bangalore", "Anantapur", 9866264892)
passengerdetails.get_passengerDetails()