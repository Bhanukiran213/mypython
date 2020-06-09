class DataTypesTest():#testing datatypes
	
	def listDataType(self):
	
		employeeDetails = []#declaration of empty list
		employeeDetails.append("Bhanu")
		employeeDetails.append("11741S034")
		employeeDetails.append(45678.90)
		employeeDetails.append("Bangalore")
		
		employeeDetails.append("Bangalore")
		#print (employeeDetails)
		
		employeeDetails[4] = "AP"
		#print (employeeDetails)
		
		if "JKL" in employeeDetails:
			print (employeeDetails)
		else:
			employeeDetails.clear()
			
		print (employeeDetails)
		
		del employeeDetails
		
		print (employeeDetails)
		
		
	def tupleDataType(self):
		
		company_tuple = ("DXC Technology", "DXC001", "EC1", 9876543210)#tuple declaration
		print (company_tuple[0])
		#company_tuple.clear()
		
		print (company_tuple)
		
	def dictionryImplementation(self):
		
		passengerDictionaryList = []
		passengerDictionary = {}#dict declaration..
		
		passengerDictionary1 = {}#dict declaration..
		
		passengerDictionary["name"] = "Bhanu"
		passengerDictionary["ticketNumber"] = 1234
		passengerDictionary["phoneNumber"] = 9866264892
		passengerDictionary["source"] = "Anantapur"
		passengerDictionary["destination"] = "Bangalore"
		
		passengerDictionary1["name"] = "RRR"
		passengerDictionary1["ticketNumber"] = 12341
		passengerDictionary1["phoneNumber"] = 9866264891
		passengerDictionary1["source"] = "Anantapur"
		passengerDictionary1["destination"] = "Bangalore"
		
		#print (passengerDictionary)# [{""}
		
		passengerDictionaryList.append(passengerDictionary)
		passengerDictionaryList.append(passengerDictionary1)
		
		#print (passengerDictionaryList)
		
		#iterating passengerDictionaryList using for loop..
		for passenger in passengerDictionaryList:
			print (passenger)# printing each record..
			#accessing values from each record using keys...
			name = passenger['name']
			print ("name is .....", name)
		
dataTypesTest = DataTypesTest()# Object creation for DataTypesTest class..
#dataTypesTest.listDataType()#method calling..

#SSdataTypesTest.tupleDataType()#method calling..
dataTypesTest.dictionryImplementation()#method calling...