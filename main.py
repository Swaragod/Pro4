print('1 - ')
print()

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]


def FlatIterator(list):
	for sub_list in list:
		for element in sub_list:
			yield element


for item in FlatIterator(nested_list):
	print(item)

print()

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)

print()
print('2 - ')
print()

numbers = [[print(i) for i in small_list] for small_list in nested_list]