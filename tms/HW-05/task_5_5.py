'''
В массиве целых чисел с количеством элементов 19, определить максимальное число и заменить им все четные по значению элементы. [02-4.1-BL19]
'''
lenght = input('Enter list of elements: ')
lst = lenght.split(',')
lst_1 = [int(x) for x in lst]
maximum = max(lst_1)

lst_2 =[]

for number in lst_1:
    if number % 2 == 0:
        lst_2.append(maximum)
    else:
        lst_2.append(number)

print(f"List: {lst_2}")






