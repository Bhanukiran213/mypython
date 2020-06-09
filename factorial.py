def factorialImp(digit):
	res = 1
	if digit == 0:
		return res
	else:
		print (digit)
		res = digit * factorialImp(digit-1)
	return res
		
#factorial = FactorialImplementation()
factorialImp(4)