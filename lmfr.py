class LambdaImplementation():
	
	def lambdaTest(self):
		#lambda_sequence = [1,2,3,4]
		addition_result = (lambda digit1, digit2: digit1 + digit2)
		print ("addition_result.......", addition_result(3,4))
		
		test_lambda = (lambda digit1, digit2: "Bhanu" if digit1<digit2 else "Mohan")
		print ("test_lambda.......", test_lambda(3,4))
		
lambda_test = LambdaImplementation()
lambda_test.lambdaTest()