from deftest import myAbs

dict1 = {}
tuple1 = (1, 2, 3)
tuple2 = (1, [2, 3])
dict1[tuple1] = 0
set1 = set()
print(dict1)
set1.add(tuple1)
print(set1)

res = myAbs(-9)
print(res)
