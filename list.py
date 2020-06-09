class Practice():
	def listPractice(self, v1, v2, v3):
		list =[]
		list.append(v1)
		list.append(v2)
		list.append(v3)
		print(list)
		print(list[-1])
		print(list[0:2])
		print(list[:1])
		print(list[1:])
		list[2] = 9866264892
		print(list)
		for i in list:
			print(i)
			for i in v2:
				print(i)
			for i in list:
				print(i)
				if i == "kiran":
					break
				print(i)
			"""for i in list:
				print(i)
			if i == "kiran":
				continue"""
			for i in range(2):
				print(i)
practice = Practice()
practice.listPractice("bhanu", "kiran" , "battala")