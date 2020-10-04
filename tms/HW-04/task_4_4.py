'''
Дан список. Создать новый список, сдвинутый на 1 элемент влево Пример: 1 2 3 4 5 ->  2 3 4 5 1
Примечание: Во всех задачах предоставить 2 решения.
Одно с использованием цикла while, другое с использованием цикла for с параметром. Оба решения предоставить в одном файле
'''

number = int(input('Enter how many integers you want in list: '))
counter = 0
lst = []
while counter < number:
    integer = int(input('Enter '+str(counter + 1)+'th number: '))
    lst.append(integer)
    counter += 1
print(f'Current list -> {lst}')

def for_func(lst_numbers) -> list:
    for_lst = []
    for word in range(1, len(lst_numbers)):
        for_lst.append(lst_numbers[word])
    for_lst.append(lst_numbers[0])
    print(f'List for -> {for_lst}')


def while_func(lst_numbers) -> list:
    while_lst = []
    counter = 1
    while counter < len(lst_numbers):
        while_lst.append(lst_numbers[counter])
        counter +=1
    while_lst.append(lst_numbers[0])
    print(f'List while -> {while_lst}')

for_func(lst)
while_func(lst)