import random

def gen_random(num_count, begin, end):
    # Необходимо реализовать генератор
    mas = []
    for i in range(0, num_count):
        mas.append(random.randint(begin, end))
    return mas

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(10, 5, 10)
data3 = ['a', 'A', 'B', 'a', 'A', 'b', 'B']
# Итератор для удаления дубликатов
ignore_case = {False, True}

class Unique(object):
    def __init__(self, items, **kwargs):
        self.ignore_case = False
        if len(kwargs) > 0:
            self.ignore_case = kwargs['ignore_case']
        mas = sorted(list(set(items)))
        if self.ignore_case == True:
            for x in range(0, len(mas)):
                mas[x] = mas[x].lower()
            mas2 = list(set(mas))
            print(*mas2)
        else:
            print(*mas)

    def __next__(self):
        return self

    def __iter__(self):
        return self


Unique(data1)
Unique(data2)
Unique(data3)
Unique(data3, ignore_case=False)
Unique(data3, ignore_case=True)




