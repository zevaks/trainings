'''
Создать lambda функцию, которая принимает на вход неопределенное количество именных аргументов
и выводит словарь с ключами удвоенной длины. {‘abc’: 5} -> {‘abcabc’: 5}
'''


lam = lambda **kwargs: { k+k:v for k,v in kwargs.items()}

print(lam(abc=5, duf=6))







