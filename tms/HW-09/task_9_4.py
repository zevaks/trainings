'''
Создать универсальный декоратор, который меняет порядок аргументов в функции на противоположный.
'''


def dekor(func):
    def wrapper(*args):
        reversed_list = []
        for check in func(*args):
            reversed_list.append(check)
        print(f'{func.__name__}{tuple(reversed_list[::-1])}')
    return wrapper


@dekor
def word(*args):
    return args

word(1,2,3,4,5,6,7,8,9)