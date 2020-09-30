# Создать строку равную всем элементам введенной строки с четными индексами.
# (считая, что индексация начинается с 0, поэтому символы выводятся начиная с первого, индексы 0,2,4,6….).

string = input('Введите строку: ')
dictionary = dict(enumerate(string))
final_str = str()
for k,v in dictionary.items():
    if k % 2 == 0:
        final_str += str(v)
print(final_str)


