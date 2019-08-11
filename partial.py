import functools

int2 = functools.partial(int, base=2)


print(int2("10"))

max10 = functools.partial(max, 10)

print(max10(5, 6, 7))
