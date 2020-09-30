'''
Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’: ‘value’}).
Чтобы получить список ключей - использовать метод .keys()
(подсказка: создается новый ключ с цифрой в конце, старый удаляется)

Примечание: Во всех задачах предоставить 2 решения.
Одно с использованием цикла while, другое с использованием цикла for с параметром. Оба решения предоставить в одном файле
'''

# with two dicts
a = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
b = {}
for k,j in a.items():
    k_new = k + str(len(k))
    b[k_new] = j
print(b)
'''
'''
a = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
for
for k,j in a.items():
    k_new = {k + str(len(k)): j}
    a.update(k_new)
    a.pop(k)
print(a)
'''

myDict = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
for k in myDict.copy().keys():
    myDict[k + str(len(k))] = myDict[k]
    del myDict[k]
print(f'Измененный словарь:\n{myDict}')
