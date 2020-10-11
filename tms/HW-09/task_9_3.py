'''
Создать декоратор для функции, которая принимает список чисел.
Декоратор должен производить предварительную проверку данных - удалять все четные элементы из списка.
'''

def decor_func(func):
    def wrapper(*args):
        fixed_lst = []
        for check in func(*args):
            if check % 2 != 0:
                fixed_lst.append(check)
        print(fixed_lst)
    return wrapper

@decor_func
def lst(*args):
    return args

lst(100,200,300,3,5,11,50)