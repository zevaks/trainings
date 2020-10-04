'''
Дан список целых чисел. Подсчитать сколько четных чисел в списке

Примечание: Во всех задачах предоставить 2 решения.
Одно с использованием цикла while, другое с использованием цикла for с параметром. Оба решения предоставить в одном файле
'''

list_of_integers = list(range(int(input('Enter list range: '))))
counter = 0
even_count = 0
for_even_count = 0
new_while_list = []
new_for_list = []
while counter < len(list_of_integers):
    if list_of_integers[counter] % 2 == 0:
        even_count +=1
        new_while_list.append(list_of_integers[counter])
    counter += 1
print(f"Even for WHILE: {even_count} -> {new_while_list}")

for integer in list_of_integers:
    if integer % 2 == 0:
        for_even_count += 1
        new_for_list.append(integer)
print(f"Even for FOR: {for_even_count} -> {new_for_list}")