'''
 Даны три слова.
 Выяснить, является ли хоть одно из них палиндромом ("перевертышем"),
 т. е. таким, которое читается одинаково слева направо и справа налево.
 (Определить функцию, позволяющую распознавать слова палиндромы.)[03-10.32]
'''

input_words = input('Enter list of words comma separated: ')
lsit_of_words = input_words.split(',')
for word in lsit_of_words:
    if word == word[::-1] and word != '' and word != ' ':
        print(f'Polindrom -> {word}')