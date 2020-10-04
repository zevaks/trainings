'''
Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’: ‘value’}).
Чтобы получить список ключей - использовать метод .keys()
(подсказка: создается новый ключ с цифрой в конце, старый удаляется)

Примечание: Во всех задачах предоставить 2 решения.
Одно с использованием цикла while, другое с использованием цикла for с параметром. Оба решения предоставить в одном файле
'''

dictn = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}

# FOR
dictn_new = {}
for key in dictn.keys():
    k = key + str(len(key))
    dictn_new[k] = dictn[key]
print(dictn_new)

# While
lenght = len(dictn)
lst = list(dictn.keys())
step = 0
dict_new_while = {}
while step < lenght:
    new_key = lst[step] + str(len(lst[step]))
    dict_new_while[new_key] = dictn[lst[step]]
    step += 1
print(dict_new_while)
















