d = {'a': 1, 'b': 2, 'c': 3}
item = d.items()
#dict_items([('a', 1), ('b', 2), ('c', 3)])
print(type(item), item)
# 字典遍历
for key, value in item:
    print(key, value)
# list迭代
l = [1, 2, 3]

for key, value in enumerate(l):
    print(key, value)

# 同时引用了两个变量 !!d.items的本质
for key, value in [('a', 'b'), ("c", 'd'), ('e', 'f')]:
    print(key, value)

li = list(range(1, 10))
print(li)

lis = []
for x in range(1, 10):
    lis.append(x*x)

print(lis)

list1 = [x for x in range(10) if x % 2 == 0]
print(list1)
lista = ['a', 'b', 'c']
listb = ['x', 'y', 'z']
list2 = [a+b for a in lista for b in listb]
print(list2)
di={'x':'A','y':'B','z':'c'}
list3= [k+'='+v for k,v in di]