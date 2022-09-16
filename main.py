print('new 1 - ')
print()


nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None, 11],
]

class SampleIterator:

	def __init__(self,my_list):
		self.my_list = my_list

	def __iter__(self):
		self.cur = -1
		return self

	def __next__(self):
		self.cur += 1
		if self.cur == len(self.my_list):
			raise StopIteration
		return self.my_list[self.cur]


my_iterator = SampleIterator(nested_list)
for item in my_iterator:
	my_iterator_low = SampleIterator(item)
	for item_low in my_iterator_low:
		print(item_low)

print('*')
# print('old 1 - ')
print()

# def FlatIterator(list):
# 	for sub_list in list:
# 		for element in sub_list:
# 			yield element
#
#for item in FlatIterator(nested_list):
# 	print(item)


flat_list = [item_low for item in my_iterator for item_low in item]
print(flat_list)

print()
print('2 - ')
print()

numbers = [[print(i) for i in small_list] for small_list in nested_list]
