import random
# gen_random(5, 1, 3) должен выдать выдать 5 случайных чисел
# в диапазоне от 1 до 3, например 2, 2, 3, 2, 1
# Hint: типовая реализация занимает 2 строки
def gen_random(num_count, begin, end):
    pass
    # Необходимо реализовать генератор
    mas = []
    for i in range(0, num_count):
        mas.append(random.randint(begin, end))
    return mas

#print(gen_random(2,3,10))

