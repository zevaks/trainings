'''
Ввести строку. Если длина строки больше 10 символов, то создать новую строку с 3 восклицательными знаками в конце  ('!!!') и вывести на экран.
Если меньше 10, то вывести на экран второй символ строки
'''

stroka = input('Enter any string: ')
if len(stroka) > 10:
    new_stroka = stroka + '!!!'
    print(new_stroka)
else:
    print(stroka[1])