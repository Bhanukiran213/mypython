class EmployeeDetails(object):

	def __init__(self, company, address, company_code):#inbuilt method...
		print ("something....")
		self.company = company
		self.address = address
		self.company_code = company_code
		
		#self.check_company_code()
		self.verify_employee_details()
		#self.view_employee_details()
		
	def check_company_code(self):
		print ("something...check_company_code.")
		company_code1 = self.company_code
		return company_code1
		
	def verify_employee_details(self):
		print ("something...verify_employee_details.")
		cc = self.check_company_code()
		print ("cc is.............", cc)
		
	def view_employee_details(self):
		
		print ("company is ....", self.company)
		print ("address is ......", self.address)
		print ("company_code is.......", self.company_code)
		
employee_details = EmployeeDetails("DXC-T", "EC-I", 12345)#object creation with some arg's.

#employee_details.view_employee_details()
