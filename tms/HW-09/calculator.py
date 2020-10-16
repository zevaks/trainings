import operator


str = '3+6-(4-2)+22-11-(6*3-5)-(2+6)*10-(4/2)'


def addition(*args):
    result = 0
    for argument in args:
        result += argument
    return result

def multiply(*args):
    result = 1
    for argument in args:
        result *= argument
    return result

def subtraction(*args):
    result = 0
    for argument in args:
        result -= argument
    return result

def division(arg, *args):
    for argument in args:
        arg = arg / argument
    return arg

# string to list
to_str = ''
for el in str:
    if el != ' ':
        to_str += el
lst = list(to_str)
print(lst)

# find all brakets positions
brackets_position = []
for bracket in range(len(lst)):
    if lst[bracket] == '(':
        brackets_position.append(bracket)
    elif lst[bracket] == ')':
        brackets_position.append(bracket)

print(brackets_position)

for el in brackets_position:
















