# print('new 1 - ')
# print()
#
#
# nested_list = [
# 	['a', 'b', 'c'],
# 	['d', 'e', 'f', 'h', False],
# 	[1, 2, None, 11],
# ]
#
# class SampleIterator:
#
# 	def __init__(self,my_list):	# инициализируем все необходимые свойства
# 		self.my_list = my_list
#
# 	def __iter__(self):
# 		self.cur = -1
# 		return self
#
# 	def __next__(self):
# 		self.cur += 1
# 		if self.cur == len(self.my_list):
# 			raise StopIteration  # выход из цикла
# 		return self.my_list[self.cur]  # в цикле for item in SampleIterator() returned_item подставится в item
#
#
# my_iterator = SampleIterator(nested_list)
# for item in my_iterator:
# 	my_iterator_low = SampleIterator(item)
# 	for item_low in my_iterator_low:
# 		print(item_low)  # при каждой итерации выполняется __next__ и результат подставляется в item.
# # Когда выбрасывается StopIteration цикл завершается
#
#
# # print('old 1 - ')
# # print()
#
# # def FlatIterator(list):
# # 	for sub_list in list:
# # 		for element in sub_list:
# # 			yield element
# #
# #
# # for item in FlatIterator(nested_list):
# # 	print(item)
#
# # print()
# #
# flat_list = [item_low for item_low in my_iterator_low]
# print(flat_list)
# #
# # print()
# # print('2 - ')
# # print()
# #
# # numbers = [[print(i) for i in small_list] for small_list in nested_list]

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None, 11],
]

class Nested_iter:
    def __init__(self,nested_list):
        self.start = -1
        self.end = len(nested_list)

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start == self.end:
            raise StopIteration
        print(type(self))
        return self

    def __str__(self):

        return '\n'.join(str(elem) for elem in nested_list[self.start])


if __name__ == '__main__':

    for elem in Nested_iter(nested_list):
        print(type(elem))
        print(elem)
