'''
В заданной строке расположить в обратном порядке все слова. Разделителями слов считаются пробелы. [02-7.2-HL08
'''

stroka = input('Enter sentence: ')
lst = stroka.split(' ')

lst_2 = []
for word in lst:
    lst_2.append(word[::-1])

for word in lst_2:
    print(word, end=' ')