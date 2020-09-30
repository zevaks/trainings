#запросить у пользоавтеля 5 имен, и вывести приветствие
list_of_names = []
for name in range(1,6):
    input_name = input('Enter ' + str(name) + 'th name: ')
    list_of_names.append(input_name)

for name in list_of_names:
    print(f"Hello, {name}!")

# переписать с map

