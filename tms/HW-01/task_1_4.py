# Даны два действительных числа. Найти среднее арифметическое и среднее геометрическое этих чисел.
import math
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
arif = (a + b) / 2
geom = math.sqrt(a*b)
print('Среднее арифметическое: ' + str(arif), 'Cреднее геометрическое: ' + str(geom))
