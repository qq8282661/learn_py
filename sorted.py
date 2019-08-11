number = (3, 6, 9, 88, 45, 30)
number2 = sorted(number)
print(number2)
string = ['s', 'e', 'c', 'd', 'G', 'y', 'k']
string2 = sorted(string)
print(string2)
score = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
nSorted = sorted(score)
print(nSorted)


def fuc(t):
    return t[1]


sSorted = sorted(score, key=fuc)
print(sSorted)
