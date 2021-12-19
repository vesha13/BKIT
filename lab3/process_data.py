import json
from re import search
from lab3.cm_timer import cm_timer_1
from lab3.field import field
from lab3.gen_random import gen_random
from lab3.print_result import print_result

# Сделаем другие необходимые импорты

path = r'C:\data_light.json'
#path = r'C:\Users\hoppl\PycharmProjects\LAB3\json_file.json'
# Необходимо в переменную path сохранить путь к файлу, который был передан при запуске сценария

with open(path, encoding='utf-8') as f:
    data = json.load(f)
# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк

def Unique(items):
    for x in range(0, len(items)):
        items[x] = items[x].lower()
    temp = []
    temp2 = []
    for x in items:
        if x not in temp:
            temp.append(x)
    for x in temp:
        temp2.append(x.capitalize())
    return temp2


@print_result
def f1(arg):
    result = sorted(Unique(field(arg, 'job-name')), key=str.lower)
    # result = sorted(Unique(field(arg, 'job-name')), key=lambda s: s.lower())
    return result


@print_result
def f2(arg):
    result = list(filter(lambda x: search('^Программист', x)!=None , arg))
    return result


@print_result
def f3(arg):
    result = list(map(lambda x: x + ' с опытом Python', arg))
    return result


@print_result
def f4(arg):
    m = gen_random(len(arg), 100000, 200000)
    result = list(zip(arg, m))
    return result


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
