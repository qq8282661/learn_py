# 创建generator,generator保存的是算法
g = (x for x in range(0, 3))
print(next(g))
print(next(g))
print(next(g))
# print(next(g)) //StopIteration
# 我们创建了一个generator后，基本上永远不会调用next()，而是通过for循环来迭代它，并且不需要关心StopIteration的错误。

# while 是循环,if 是条件判断


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n+1
    return 'done'


f = fib(6)
print(f)
for x in f:
    print(x)

# generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)


o = odd()
next(o)
next(o)
next(o)
# 杨辉三角
