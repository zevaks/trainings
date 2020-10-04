'''
Для каждого натурального числа в промежутке от m до n вывести все делители, кроме единицы и самого числа.
m и n вводятся с клавиатуры. Пример:m =100, n = 105

100: 2 4 5 10 20 25 50  101:  102: 2 3 6 17 34 51  103:  104: 2 4 8 13 26 52  105: 3 5 7 15 21 35
'''

M = int(input('Enter M: '))
N = int(input('Enter N: '))

diff = N - M
lst = []
lst_2 = []
for step in range(diff + 1):
    lst.append(M + step)
string = ''
for step in lst:
    print(f'{step}: ', end='')
    for step_2 in range(1,step+1):
        if step % step_2 == 0 and step_2 != 1 and step_2 != step:
            string = str(step_2) + ' '
            print(string, end=' ')















