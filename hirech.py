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
class Apgb(Sbi):
	def __init__(self):
		pass
	def apbpBranch(self):
		pass
		
apgb =Apgb()
apgb.sbiBanch()
print(issubclass(Apgb,Sbi))#True
print(issubclass(Apgb,Sbh))#False
print(issubclass(Sbh,Sbi))#True


