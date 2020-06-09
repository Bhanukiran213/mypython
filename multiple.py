class Sbi():
	def __init__(self):
		pass
	def sbiBanch(self):
		print("ATP")
		
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
		
apgb =Apgb()
apgb.sbiBanch()
print(issubclass(Apgb,Sbi))#True
print(issubclass(Sbh,Apgb))#False
print(issubclass(Sbh,Sbi))#True


