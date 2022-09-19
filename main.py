nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


print('\n', 'итератор', '\n')


class SampleIterator:

    def __init__(self, my_list):
        self.my_list = my_list

    def __iter__(self):
        self.list_cur = 0
        self.sub_list_cur = -1

        return self

    def __next__(self):
        self.sub_list_cur += 1
        self.sub_list = self.my_list[self.list_cur]
        if self.sub_list_cur == len(self.sub_list):
            self.sub_list_cur = 0
            self.list_cur += 1
            if self.list_cur == len(self.my_list):
                raise StopIteration
        return self.my_list[self.list_cur][self.sub_list_cur]


my_iterator = SampleIterator(nested_list)
for item in my_iterator:
    print(item)

print('\n', 'комперхеншн', '\n')

flat_list = [item for item in SampleIterator(nested_list)]
print(flat_list)

print('\n', 'генератор', '\n')


def my_generator(my_list):
    for sub_list in my_list:
        for element in sub_list:
            yield element


for item in my_generator(nested_list):
    print(item)
