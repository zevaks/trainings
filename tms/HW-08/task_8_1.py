'''
Описать функцию fact2( n ), вычисляющую двойной факториал :n!! = 1·3·5·...·n,
если n — нечетное; n!! = 2·4·6·...·n, если n — четное (n > 0 — параметр целого типа.
С помощью этой функции найти двойные факториалы пяти данных целых чисел [01-11.2-Proc35]
'''

def fact2(n):
    factorial = 1
    if n % 2 != 0:
        for number in range(1,n+1,2):
            factorial *= number
    elif n % 2 == 0:
        for number in range(2, n + 1,2):
            factorial *= number
    return factorial


print(fact2(20))