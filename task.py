class PassengerDetails():
	def __init__ (self, passengerName, source, destination, mobileNumber):
		self.passengerName = passengerName
		self.source = source
		self.destination = destination
		self.mobileNumber = mobileNumber
	def getPassengerName(self):
		name = self.passengerName
		return name
	def getSource(self):
		source = self.source
		return source
	def getDestination(self):
		destination = self.destination
		return destination
	def getMobileNumber(self):
		mobileNumber = self.mobileNumber
		return mobileNumber
passengerdetails = PassengerDetails("bhanukiran", "Anantapur", "Bangalore", 9866264892)
passenger_name = passengerdetails.getPassengerName()
passenger_source = passengerdetails.getSource()
passenger_destination = passengerdetails.getDestination()
passenger_mobile_number = passengerdetails.getMobileNumber()

print(passenger_name)
print(passenger_source)
print(passenger_destination)
print(passenger_mobile_number)

	