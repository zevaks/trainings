'''
Для заданного числа N составьте программу вычисления суммы S=1+1/2+1/3+1/4+...+1/N, где N – натуральное число. [02-3.2-ML21]
'''

N = int(input('Enter N: '))
S = 0
lst = []
for number in range(1, N+1):
    S += 1/number
print(f'Summa: {S}')