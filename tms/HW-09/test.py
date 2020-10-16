
str = [1,1,2,3,4,5,5,4,3,1,5,4]

dct = {}
j = 0

for i in str:
    dct[i] = str.count(i)

print(dct)
