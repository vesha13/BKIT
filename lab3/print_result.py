# Здесь должна быть реализация декоратора
def print_result(fn):
    def wrapped(*args, **kwargs):
        print(fn.__name__)
        if isinstance(fn(*args, **kwargs), dict)==True:
           # for dict.items in range()
            m = fn(*args, **kwargs)
            for key, value in m.items():
                print('{0} = {1}'.format(key, value))
        elif isinstance(fn(*args, **kwargs), list) == True:
            m = fn(*args, **kwargs)
            for value in m:
                if isinstance(value, tuple) == True:
                    print('{0}, зарплата {1} руб'.format(value[0], value[1]))
                else:
                    print(value)
        elif isinstance(fn(*args, **kwargs), (int, str)):
            print(fn(*args, **kwargs))
        return fn(*args, **kwargs)
    return wrapped


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()

