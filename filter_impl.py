from functools import reduce
class FilterImplementation():
	
	def filterTest(self):
		filter_sequence = range(50)		
		filter_seq_result = list(filter(lambda x:x%2==0, filter_sequence))
		print (filter_seq_result)
		
	def mapTest(self):
		map_sequence = range(20)
		map_seq_result = list(map(lambda x: x*5, map_sequence))
		print (map_seq_result)
	
	def reduceTest(self):
		red_sequence = range(10)
		red_seq_result = reduce(lambda val1,val2: val1-val2, red_sequence)
		print(red_seq_result)#
		
filter_impl = FilterImplementation()
filter_impl.filterTest()
filter_impl.mapTest()
filter_impl.reduceTest()