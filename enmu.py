from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

print(Month.Jan.value)

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

print(dir(Month))
