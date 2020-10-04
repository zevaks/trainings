'''
Написать программу, в которой вводятся два операнда Х и Y и знак операции sign (+, –, /, *).
Вычислить результат Z в зависимости от знака.
Предусмотреть реакции на возможный неверный знак операции, а также на ввод Y=0 при делении.
Организовать возможность многократных вычислений без перезагрузки программа (т.е. построить бесконечный цикл).
В качестве символа прекращения вычислений принять ‘0’ (т.е. sign='0').
'''
while True:
    X = int(input('Enter X: '))
    Y = int(input('Enter Y: '))
    sign = input('Enter +, –, /, * or 0 for Quit: ')

    if sign == '/' and Y == 0:
        while Y == 0:
            Y = int(input('Y can not be 0, reenter Y: '))

    while sign not in ['-', '+', '/', '*', '0']:
        sign = input('Incorrect sign, reenter +, –, /, *: ')

    if sign == '0':
        print(f'Exit')
        exit()
    elif sign == '-':
        print(f'Result: {X-Y}')
    elif sign == '+':
        print(f'Result: {X+Y}')
    elif sign == '/':
        print(f'Result: {X/Y}')
    elif sign == '*':
        print(f'Result: {X*Y}')


