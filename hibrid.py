class Sbi():
	def __init__(self):
		pass
	def sbiBanch(self):
		pass
		
class Sbh(Sbi):
	def __init__(self):
		pass
	def sbhBranch(self):
		pass
class Apgb(Sbh):
	def __init__(self):
		pass
	def apbpBranch(self):
		pass
class Icici(Apgb,Sbh):
	def __init__(self):
		pass
		
icici = Icici()
print(issubclass(Icici,Sbi))



