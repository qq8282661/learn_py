def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


res = fact_iter(100, 1)
print(res)


def fact(n):
    return fact_iter(n, 1)


# python 没有尾递归优化
res1000 = fact(990)
print(res1000)
