'''
Дано число. Найти сумму и произведение его цифр.
'''
number = int(input('Enter a number: '))
lst = list(range(1,number+1))

def summa(lst):
    summa = 0
    for number in lst:
        summa += number
    return summa

def proizv(lst):
    proizv = 1
    for number in lst:
        proizv *= number
    return proizv

print(f'Summa: {summa(lst)}')
print(f'Proizvedenije: {proizv(lst)}')