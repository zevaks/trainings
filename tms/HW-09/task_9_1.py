'''
Дан список строк.
Отформатировать все строки в формате ‘{i} - {string}’, где i это порядковый номер строки в списке.
Использовать генератор списков.
'''

input_words = input('Enter list of words comma separated: ')
list_of_words = input_words.split(',')
gen_list = [ f'{i} - {list_of_words[i]}' for i in range(len(list_of_words))]
print(type(gen_list))
print(gen_list)