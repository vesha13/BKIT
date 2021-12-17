import math
import sys

def get_coef(index, prompt):

    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
    except:
        # Вводим с клавиатуры
        coef_str = "Flag"
    while(isinstance(coef_str,str)==True):
        try:
            coef_str= float(coef_str)
        except:
            print(prompt)
            coef_str = input()
    # Переводим строку в действительное число
    coef = float(coef_str)
    return coef


def get_roots(a, b, c):
    result = []
    D = b * b - 4 * a * c
    if a != 0.0:
        if D == 0.0:
            root = -b / (2.0 * a)
            if root > 0.0:
                result.append(math.sqrt(root))
                result.append(-math.sqrt(root))
            elif root == 0.0:
                result.append(root)
        elif D > 0.0:
            sqD = math.sqrt(D)
            root1 = (-b + sqD) / (2.0 * a)
            if root1 > 0.0:
                root11 = math.sqrt(root1)
                result.append(root11)
                result.append(-root11)
            elif root1 == 0.0:
                result.append(root1)
            root2 = (-b - sqD) / (2.0 * a)
            if root2 > 0.0:
                root22 = math.sqrt(root2)
                result.append(root22)
                result.append(-root22)
            elif root2 == 0.0:
                result.append(root2)
    elif a == 0.0:
        if b != 0:
            a = b
            b = 0
            D = b * b - 4 * a * c
            if D == 0.0:
                root = -b / (2.0 * a)
                result.append(root)
            elif D > 0.0:
                sqD = math.sqrt(D)
                root1 = (-b + sqD) / (2.0 * a)
                root2 = (-b - sqD) / (2.0 * a)
                result.append(root1)
                result.append(root2)
    return result


def main():
    '''
    Основная функция
    '''
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    roots = get_roots(a, b, c)
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        if a == 0.0 and b == 0.0 and c == 0.0:
            print('Бесконечно много корней')
        else:
            print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три корня: {}, {} и {}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('Четыре корня: {},{}, {} и {}'.format(roots[0], roots[1], roots[2], roots[3]))

# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()

