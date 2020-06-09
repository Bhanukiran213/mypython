class Company():
	def __init__(this, company, company_code):
		this.company = company
		this.company_code = company_code
		print (this.company)
		print (this.company_code)
		
		this.test_method()
		
	def get_company_name(this):
		print (this.company)
		return this.company
		
	def get_company_code(this):
		print (this.company_code)
		return this.company_code
		
	def test_method(this):
		pass
		
		
class Employee(Company):
	def __init__(this, company, cc):
		#Company.__init__(this, company, cc) By using class name.
		super().__init__(company, cc)#by using super keyword
		
		
	def get_employee_address(this):
		employee_address = "Marthalli"
		return employee_address
		
	def get_employee_contact(this):
		employee_contact = 9876543210
		return employee_contact
		
	def get_company_code(this):
		company_code = "123ert34"
		return company_code
		
		
employee = Employee("DXC-T", 1234)
employee_address1 = employee.get_employee_address()
employee_contact1 = employee.get_employee_contact()
#print(employee_address1)
#print(employee_contact1)


employee_company = employee.get_company_name()
employee_company_code = employee.get_company_code()
#print(employee_company)
print(employee_company_code)
print (issubclass(Employee,Company))
print (issubclass(Company,Employee))













