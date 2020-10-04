'''
Дан список целых чисел.  Создать новый список, каждый элемент которого равен исходному элементу умноженному на -2

Примечание: Во всех задачах предоставить 2 решения.
Одно с использованием цикла while, другое с использованием цикла for с параметром. Оба решения предоставить в одном файле
'''
list_of_integers = list(range(int(input('Enter list range: '))))
count = 0
new_while_list = []
new_for_list = []
while count < len(list_of_integers):
    new_while_list.append(int(list_of_integers[count]) * 2)
    count += 1
print(f"List for WHILE: {new_while_list}")

for integer in list_of_integers:
    new_for_list.append(int(integer) * 2)
print(f"List for FOR: {new_while_list}")